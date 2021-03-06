import os
import sys
import time


def curl_lock(dryrun=False):
    if dryrun:
        return
    try:
        key = os.environ['IFFFF']
    except:
        key = ""
    os.system('curl -X POST https://maker.ifttt.com/trigger/lockdoor/with/key/'+key)

def curl_unlock(dryrun=False):
    if dryrun:
        return
    key = os.environ['IFFFF']
    os.system('curl -X POST https://maker.ifttt.com/trigger/fart/with/key/'+key)

def notify_lock(dryrun=False):
    if dryrun:
        return
    key = os.environ['IFFFN']
    os.system('curl -X POST https://maker.ifttt.com/trigger/notifylocked/with/key/'+key)

def notify_unlock(dryrun=False):
    if dryrun:
        return
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

        if 'issue-title-link' in x:
            nextline = True

    f.close() # ALWASYS CLOSE THIS

    print "found", len(saveline), "events"

    cute = ""
    for x in saveline:
        cute += x.strip() + ", "

    print cute

    # print ''.join(saveline).split('\n')
    return saveline


# returns True when locked
# returns NONE for error
# accepts previous value in run
def makeDecision(saveline, prevlocked, dryrun=False):
    nickhome = None
    benhome = None
    reslocked = False

    found = []

    # loop Ben
    for x in saveline:
        strip = x.strip()
        if "aa" == strip:
            benhome = True
            found.append(strip)
            break
        if "ab" == strip:
            benhome = False
            found.append(strip)
            break

    # loop
    for x in saveline:
        strip = x.strip()
        if "ba" == strip:
            nickhome = True
            found.append(strip)
            break
        if "bb" == strip:
            nickhome = False
            found.append(strip)
            break

    print "deciding using", found


    if benhome is None or nickhome is None:
        print "PANICK, something went wrong"
        return None

    print "Ben is home", benhome
    print "Nick is home", nickhome

    # hand wave,
    newlockstate = not (benhome or nickhome)

    # should notify
    shouldnotify = newlockstate != prevlocked

    if( newlockstate ):
        print "LOCKING DOOR"
        curl_lock(dryrun)
        if shouldnotify:
            notify_lock(dryrun)
        print "done with notify"
        reslocked = True # return true for locked
    else:
        print "UNLOCKING DOOR"
        curl_unlock(dryrun)
        if shouldnotify:
            notify_unlock(dryrun)
        print "done with notify"
        reslocked = False  # return false for not locked

    return reslocked


sleep_seconds = 45
print "Start"
# lastrun = reslocked  # start assuming it's open


# curl_unlock()
# print "*",
# time.sleep(5)
curl_lock()  # locked or true
print "*",
# time.sleep(5)
# curl_unlock()# unlocked or false
# print "*",
# time.sleep(5)
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

    # delete files
    delete_files()
    
    # final global sleep
    time.sleep(sleep_seconds)


print "NEVER REACHES THIS"
