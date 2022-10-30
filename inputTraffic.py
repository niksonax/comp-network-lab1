from scapy.all import *

sport=10000
dport=80

# TCP fin
pkt=IP(src="10.18.48.2", dst="10.18.48.1")
FIN=pkt/TCP(sport=sport, dport=dport, flags="F")
send(FIN)

# UDP
udp = UDP(dport=dport,sport=sport)
send(pkt/udp)
