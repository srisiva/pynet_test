#!/usr/bin/env python
ipaddr=raw_input("Enter a IP addr:")
sipaddr=ipaddr.split('.')
print sipaddr
print "{:<12} {:<12} {:<12} {:<12}".format(*sipaddr)
#print '{0:<12}'.format(sipaddr[0])+'{0:<12}'.format(sipaddr[1])+'{0:<12}'.format(sipaddr[2])+'{0:<12}'.format(sipaddr[3])
