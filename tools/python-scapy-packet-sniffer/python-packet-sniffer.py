#!/usr/bin/python

from scapy.all import *
import socket
import datetime
import os
import time

def network_monitoring_for_visualization_version(pkt):
	time=datetime.datetime.now()
	#classifying packets into TCP
	if pkt.haslayer(TCP):
		print(str("[")+str(time)+str("]")+"  "+"TCP:{}".format(len(pkt[TCP]))+" Bytes"+"    "+"SRC-MAC:" +str(pkt.src)+"    "+ "DST-MAC:"+str(pkt.dst)+"    "+ "SRC-PORT:"+str(pkt.sport)+"    "+"DST-PORT:"+str(pkt.dport)+"    "+"SRC-IP:"+str(pkt[IP].src  )+"    "+"DST-IP:"+str(pkt[IP].dst  ))
	#classifying packets into UDP	
	if pkt.haslayer(UDP):
		print(str("[")+str(time)+str("]")+"  "+"UDP:{}".format(len(pkt[UDP]))+" Bytes "+"    "+"SRC-MAC:" +str(pkt.src)+"    "+"DST-MAC:"+ str(pkt.dst)+"    "+"SRC-PORT:"+ str(pkt.sport) +"    "+"DST-PORT:"+ str(pkt.dport)+"    "+"SRC-IP:"+ str(pkt[IP].src)+"    "+"DST-IP:"+ str(pkt[IP].dst))
	#classifying packets into ICMP
	if pkt.haslayer(ICMP):
		print(str("[")+str(time)+str("]")+"  "+"ICMP:{}".format(len(pkt[ICMP]))+" Bytes"+"    "+"IP-Version:"+str(pkt[IP].version)+"    "*1+"	 SRC-MAC:"+str(pkt.src)+"    "+"DST-MAC:"+str(pkt.dst)+"    "+"SRC-IP: "+str(pkt[IP].src)+ "    "+"DST-IP:  "+str(pkt[IP].dst))	

if __name__ == '__main__':
	sniff(prn=network_monitoring_for_visualization_version,iface="lan0")
