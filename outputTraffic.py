from scapy.all import *

sport=10000
dport=80

# ICMP output
pkt = IP(dst="10.18.48.2", src="10.18.48.1")
send(pkt/ICMP())

# TCP output
pkt = IP(dst="10.18.48.2", src="10.18.48.1")
trans = TCP(sport=sport, dport=dport)
send(pkt/ICMP())