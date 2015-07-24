#!/usr/bin/env python
import sys
import socket
import httplib
from time import sleep

def nextdomain(domain):
    try:
        conn = httplib.HTTPConnection(domain, timeout=2)
        conn.request("HEAD","/")
        res = conn.getresponse()
        if (res.status == 200 ):
            print domain, res.status, res.reason
        elif (res.status == 301 ):
            print domain, res.status, res.reason, res.msg['location']
        elif (res.status == 302 ):
            print domain, res.status, res.reason, res.msg['location']
        elif (res.status == 307 ):
            print domain, res.status, res.reason, res.msg['location']
        else:
            print domain, res.status, res.reason
    except socket.error, e:
         print domain, "ERR can not connect, connection refused"
    except socket.gaierror, e:
         print domain, "ERR can not connect, nodename nor servname provided, or not known"
    except socket.timeout, e:
         print domain, "ERR connection timed out"

def readdomainsfromstdin():
    lines = sys.stdin.readlines()
    for line in range(len(lines)):
        lines[line] = lines[line].replace('\n','')
        nextdomain(lines[line])
        sleep(0.5)

if (len(sys.argv) >= 2):
    nextdomain(sys.argv[1])
else:
    readdomainsfromstdin()