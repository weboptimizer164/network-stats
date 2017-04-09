#! /usr/bin/env python

sample_interval = 10
# interface="eth1"
from scapy.all import *
from collections import Counter
import json

# Counter is a *much* better option for what you're doing here. See
# http://docs.python.org/2/library/collections.html#collections.Counter
traffic = Counter()
# You should probably use a cache for your IP resolutions
hosts = {}

def human(num):
    for x in ['', 'k', 'M', 'G', 'T']:
        if num < 1024.: return "%3.1f %sB" % (num, x)
        num /= 1024.
    # just in case!
    return  "%3.1f PB" % (num)

def traffic_monitor_callback(pkt):
    if IP in pkt:
        pkt = pkt[IP]
        # You don't want to use sprintf here, particularly as you're
        # converting .len after that!
        # Here is the first place where you're happy to use a Counter!
        # We use a tuple(sorted()) because a tuple is hashable (so it
        # can be used as a key in a Counter) and we want to sort the
        # addresses to count mix sender-to-receiver traffic together
        # with receiver-to-sender
        traffic.update({tuple(sorted(map(atol, (pkt.src, pkt.dst)))): pkt.len})

def main():
    sniff(prn=traffic_monitor_callback, store=False,
          timeout=sample_interval)
    s2={}
    i=1
    # ... and now comes the second place where you're happy to use a
    # Counter!
    # Plus you can use value unpacking in your for statement.
    for (h1, h2), total in traffic.most_common(10):
        # Let's factor out some code here
        h1, h2 = map(ltoa, (h1, h2))
        for host in (h1, h2):
            if host not in hosts:
                try:
                    rhost = socket.gethostbyaddr(host)
                    hosts[host] = rhost[0]
                except:
                    hosts[host] = None
        # Get a nice output
        h1 = "%s (%s)" % (hosts[h1], h1) if hosts[h1] is not None else h1
        h2 = "%s (%s)" % (hosts[h2], h2) if hosts[h2] is not None else h2
        speed = (human(float(total)/sample_interval))+"/s"
        source = h1
        destination = h2
        s1 = {"Speed": speed, "Source": str(source), "Destination":str(destination)}
        s2[i]=s1
        i=i+1
        # print s1
    s2 = json.dumps(s2)
    # print s2
    return s2
        # print "%s/s: %s - %s" % (human(float(total)/sample_interval), h1, h2)