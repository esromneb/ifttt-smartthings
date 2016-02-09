import os
import sys
import time


def curl_lock():
    key = os.environ['IFFFF']
    os.system('curl -X POST https://maker.ifttt.com/trigger/lockdoor/with/key/'+key)

def curl_unlock():
    key = os.environ['IFFFF']
    os.system('curl -X POST https://maker.ifttt.com/trigger/fart/with/key/'+key)

def notify_lock():
    key = os.environ['IFFFN']
    os.system('curl -X POST https://maker.ifttt.com/trigger/notifylocked/with/key/'+key)

def notify_unlock():
    key = os.environ['IFFFN']
    os.system('curl -X POST https://maker.ifttt.com/trigger/notifyunlocked/with/key/'+key)	

def delete_files():
    path = ['issues', 'issues.1', 'issues.2', 'issues.3']
    for delme in path:
        try:
            os.remove(delme)
        except OSError:
            pass
delete_files()

def download():
    # blocking
    os.system('wget https://github.com/esromneb/legendary-carnival/issues')

    # os.system('cat issues | grep "ba"')

    try:
        f = open('issues', 'r')
    except IOError:
        print "OH SHIT NO DOWNload"
        return None
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


    print "found", len(saveline), "events"
    return saveline


# returns True when locked
# returns NONE for error
# accepts previous value in run
def makeDecision(saveline, prevlocked):
    nickhome = None
    benhome = None
    reslocked = False


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
        return None

    print "Ben is home", benhome
    print "Nick is home", nickhome

    if( benhome or nickhome ):
        print "UNLOCKING DOOR"
        curl_unlock()
        notify_unlock()
        print "done with notify"
        reslocked = False  # return false for not locked
    else:
        print "LOCKING DOOR"
        curl_lock()
        notify_lock()
        print "done with notify"
        reslocked = True # return true for locked

    return reslocked


sleep_seconds = 8
print "Start"
# lastrun = reslocked  # start assuming it's open

curl_unlock()
print "*",
time.sleep(5)
curl_lock()  # locked or true
print "*",
time.sleep(5)
curl_unlock()# unlocked or false
print "*",
time.sleep(5)
lastrun = False


print ""
print "done with init sequence"

while True:
    saveoutside = download()

    if saveoutside is None:
        print "problem with downloader"
        time.sleep(sleep_seconds)  # failbot sleep on own and try again
        continue

    thisrun = makeDecision(saveoutside, lastrun)

    # update
    lastrun = thisrun
    
    # final global sleep
    time.sleep(sleep_seconds)


print "NEVER REACHES THIS"
