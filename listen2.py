from scapy.all import *
import requests




def curl_dash1(dryrun=False):
    if dryrun:
        return
    try:
        key = os.environ['IFFFF']
    except:
        key = ""
    os.system('curl -X POST https://maker.ifttt.com/trigger/dash1/with/key/'+key)


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
        print "Toggle the light"
        curl_dash1()
      else:
        print "ARP Probe from unknown device: " + pkt[ARP].hwsrc

print sniff(prn=arp_display, filter="arp", store=0)

