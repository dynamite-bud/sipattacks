from scapy.all import *




sourcePort = 31113
destinationIp = "192.168.54.112"
sourceIp = "192.168.54.75"

ip=IP(src=sourceIp, dst=destinationIp)
# TCP SYN
TCP_SYN=TCP(sport=sourcePort, dport=5060, flags="S", seq=100)
TCP_SYNACK=sr1(ip/TCP_SYN)

# TCP SYN+ACK
myAck = TCP_SYNACK.seq + 1
TCP_ACK=TCP(sport=sourcePort, dport=5060, flags="A", seq=101, ack=myAck)
send(ip/TCP_ACK)

myPayload=(
    'OPTIONS sip:{0}:5060;transport=tcp SIP/2.0\r\n'
    'Via: SIP/2.0/TCP 192.168.44.32:5060;branch=1234\r\n'
    'From: \"somedevice\"<sip:somedevice@1.1.1.1:5060>;tag=5678\r\n'
    'To: <sip:{0}:5060>\r\n'
    'Call-ID: 9abcd\r\n'
    'CSeq: 1 OPTIONS\r\n'
    'Max-Forwards: 0\r\n'
    'Content-Length: 0\r\n\r\n').format(destinationIp)
#print(myPayload)
TCP_PUSH=TCP(sport=sourcePort, dport=5060, flags="PA", seq=101, ack=myAck)
send(ip/TCP_PUSH/myPayload)
