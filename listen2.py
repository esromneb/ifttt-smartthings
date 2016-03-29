from scapy.all import *
import requests




def curl_dash1(dryrun=False):
    if dryrun:
        return
    try:
        key = os.environ['IFFFN']
    except:
        key = ""
    os.system('curl -X POST https://maker.ifttt.com/trigger/dash1/with/key/'+key)
    print ""

def toggle_st():
    url = 'YOUR_API_ENDPOINT'
    headers = {"Authorization": "Bearer YOUR_API_TOKEN"}
    data = '{"command":"toggle"}'
    print "about to post", data
    r = requests.put(url, data=data, headers=headers)

def arp_display(pkt):
  if pkt[ARP].op == 1: #who-has (request)
    if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
      if pkt[ARP].hwsrc == '74:c2:46:cd:56:19': #'00:0c:43:00:5a:ca': # Mac & Cheese
        print "Toggle the light (Cottenelle)"
        curl_dash1()
      elif pkt[ARP].hwsrc == 'a0:02:dc:ec:c3:e8':
        print "Gillete (doing nothing)"
      else:
        print "ARP Probe from unknown device: " + pkt[ARP].hwsrc

print "using a key with length", len(os.environ['IFFFN'])
print sniff(prn=arp_display, filter="arp", store=0)

