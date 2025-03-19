#!/usr/bin/env python

import scapy.all as scapy
import optparse
import subprocess
def get_values():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--range", dest="ip",help="Enter ipaddress range")
    (values,arguments)=parser.parse_args()
    if not values.ip:
        parser.error("Please input IPaddress for which the network has to be scanned, for more info use --help option")
    return values
def scan(ip):
    #print("hey")
    packet=scapy.ARP(pdst=ip)
    #print("hey1")
    broadcast =scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #print("hey2")
    arp_ether_request=broadcast/packet
    answered=scapy.srp(arp_ether_request,timeout=1,verbose=True)[0]

    print("Mac_Address\t\t\t\tIP_Address")
    for i in answered:
        print(str(i[1].hwsrc) + "\t\t" + str(i[1].psrc))
        print("----------------------------------------------------")
values1=get_values()
ip1=values1.ip
scan(ip1)