import os
import sys
import time


def curl_lock():
    os.system('curl -X POST https://maker.ifttt.com/trigger/lockdoor/with/key/')

def curl_unlock():
    os.system('curl -X POST https://maker.ifttt.com/trigger/fart/with/key/')

path = ['issues', 'issues.1', 'issues.2', 'issues.3']
for delme in path:
    try:
        os.remove(delme)
    except OSError:
        pass


# blocking
os.system('wget https://github.com/esromneb/legendary-carnival/issues')

# os.system('cat issues | grep "ba"')

try:
    f = open('issues', 'r')
except IOError:
    print "OH SHIT NO DOWNload"
    exit(0)
    #return

nextline = False

saveline = []


for x in f:
    if nextline:
        saveline.append(x)
        nextline = False

    # print x,

    if 'issue-title-link' in x:
        nextline = True

# print "saved this:"
# print saveline

print "found", len(saveline), "events"

# saveline.reverse()

# print saveline

nickhome = None
benhome = None



# loop Ben
for x in saveline:
    if "aa" in x:
        benhome = True
        break
    if "ab" in x:
        benhome = False
        break

# loop
for x in saveline:
    # print x
    if "bb" in x:
        nickhome = True
        break
    if "ba" in x:
        nickhome = False


if benhome is None or nickhome is None:
    print "PANICK, something went wrong"

print "Ben is home", benhome
print "Nick is home", nickhome

if( benhome or nickhome ):
    print "LOCKING DOOR"
    curl_unlock()
else:
    print "UNLOCKING DOOR"
    curl_lock()





print "done"