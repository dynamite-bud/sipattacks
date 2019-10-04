import random, string, socket


"""
REGISTER sip:[[to_user]]@[[server_ip]] SIP/2.0
Via: SIP/2.0/UDP [[client_ip]]:[[client_port]];branch=[[branch_value]];rport
Max-Forwards: 70
To: [[to_user]] <sip:[[to_user]]@[[server_ip]]>
From: [[from_user]] <sip:[[from_user]]@[[server_ip]]>;tag=[[tag_value]]
Call-ID: [[call_id]]
CSeq: 1 REGISTER
Contact: <sip:[[from_user]]@[[client_ip]]:[[client_port]]>
Expires: 3600
User-Agent: [[user_agent]]
Content-Length: 0


to_user:7050
server_ip:192.168.54.112
client_ip: 192.168.11.12
client_port: 31113
to_user:7050
from_user:7050           ##only in case of register...
call_id: random
7016@192.168.54.112



0000   b6 d5 2e 7c 71 22 a4 4c c8 4e b0 2d 08 00 45 00
0010   02 4c 94 cd 40 00 40 11 b5 c7 c0 a8 36 4b c0 a8
0020   36 70 13 c4 13 c4 02 38 e0 e2 52 45 47 49 53 54
0030   45 52 20 73 69 70 3a 31 39 32 2e 31 36 38 2e 35
0040   34 2e 31 31 32 20 53 49 50 2f 32 2e 30 0d 0a 56
0050   69 61 3a 20 53 49 50 2f 32 2e 30 2f 55 44 50 20
0060   31 39 32 2e 31 36 38 2e 35 34 2e 37 35 3a 35 30
0070   36 30 3b 72 70 6f 72 74 3b 62 72 61 6e 63 68 3d
0080   7a 39 68 47 34 62 4b 50 6a 32 31 64 35 36 31 30
0090   64 2d 32 36 61 36 2d 34 30 35 33 2d 38 32 38 31
00a0   2d 36 30 62 33 64 31 31 30 61 66 31 35 0d 0a 52
00b0   6f 75 74 65 3a 20 3c 73 69 70 3a 31 39 32 2e 31
00c0   36 38 2e 35 34 2e 31 31 32 3b 6c 72 3e 0d 0a 4d
00d0   61 78 2d 46 6f 72 77 61 72 64 73 3a 20 37 30 0d
00e0   0a 46 72 6f 6d 3a 20 3c 73 69 70 3a 37 30 30 32
00f0   40 31 39 32 2e 31 36 38 2e 35 34 2e 31 31 32 3e
0100   3b 74 61 67 3d 39 34 62 39 34 32 38 37 2d 36 61
0110   35 39 2d 34 37 31 35 2d 39 38 32 37 2d 62 32 63
0120   64 38 30 30 64 39 30 33 38 0d 0a 54 6f 3a 20 3c
0130   73 69 70 3a 37 30 30 32 40 31 39 32 2e 31 36 38
0140   2e 35 34 2e 31 31 32 3e 0d 0a 43 61 6c 6c 2d 49
0150   44 3a 20 64 66 35 61 61 32 38 33 2d 34 38 32 34
0160   2d 34 62 36 31 2d 38 31 63 35 2d 61 64 62 63 65
0170   39 37 66 34 39 35 63 0d 0a 43 53 65 71 3a 20 31
0180   33 34 38 37 20 52 45 47 49 53 54 45 52 0d 0a 55
0190   73 65 72 2d 41 67 65 6e 74 3a 20 70 6a 73 69 70
01a0   20 70 79 74 68 6f 6e 0d 0a 43 6f 6e 74 61 63 74
01b0   3a 20 3c 73 69 70 3a 37 30 30 32 40 31 39 32 2e
01c0   31 36 38 2e 35 34 2e 37 35 3a 35 30 36 30 3b 6f
01d0   62 3e 0d 0a 45 78 70 69 72 65 73 3a 20 33 30 30
01e0   0d 0a 41 6c 6c 6f 77 3a 20 50 52 41 43 4b 2c 20
01f0   49 4e 56 49 54 45 2c 20 41 43 4b 2c 20 42 59 45
0200   2c 20 43 41 4e 43 45 4c 2c 20 55 50 44 41 54 45
0210   2c 20 49 4e 46 4f 2c 20 53 55 42 53 43 52 49 42
0220   45 2c 20 4e 4f 54 49 46 59 2c 20 52 45 46 45 52
0230   2c 20 4d 45 53 53 41 47 45 2c 20 4f 50 54 49 4f
0240   4e 53 0d 0a 43 6f 6e 74 65 6e 74 2d 4c 65 6e 67
0250   74 68 3a 20 20 30 0d 0a 0d 0a

"""


def get_rand_call_id():
        prefix = ''.join(random.sample(string.digits + string.lowercase, 27))
        return "{0}{1}".format(str(prefix), str(random.randrange(10000, 99999)))

def get_rand_branch():
        prefix = ''.join(random.sample(string.digits, 10))
        return "z9hG4bK-{0}".format(str(prefix))

def get_rand_tag():
	prefix = random.randint(100000,999999)
	return "{0}".format(str(prefix))

def fill_packet_data(text):
	rand1=rand2=0
	while(rand1==rand2):
	    rand1=int(random.randint(7000,8000))
	    rand2=int(random.randint(7000,8000))	
	var_dict = {'[[server_ip]]':"192.168.54.223",
	  '[[server_port]]': "5090",
	  '[[client_ip]]': "192.168.51.135",
	  '[[client_port]]': "8192",
	  '[[from_user]]': str(rand2),
	  '[[to_user]]': str(rand1),
	  '[[user_agent]]': "StarTrinity.SIP 2018-03-16 7.47 UTC",
	  '[[expire_duration]]': "3600",
	  '[[call_id]]': get_rand_call_id(),
	  '[[branch_value]]': get_rand_branch(),
	  '[[tag_value]]': get_rand_tag()}

	for key, value in var_dict.items():
	    text = text.replace(key, value)
	return text


"""
print(get_rand_call_id())
print(get_rand_branch())
print(get_rand_tag())"""


def genPacket(method):
	with open("./method/{0}.message".format(method),"r") as data:
		pkt_data=data.read()
	
	pkt_data = fill_packet_data(pkt_data)

	#pkt = IP(src="192.168.54.75", dst="192.168.54.112") / UDP(sport=int(31113), dport=int(5060)) / pkt_data
	return pkt_data


"""
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.settimeout(5)
#s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.connect(("192.168.54.112",5060))
pkt_data=genPacket("register")
print(pkt_data)
s.sendall(pkt_data)
buff,srcaddr=s.recvfrom(8192)
print(srcaddr)
print(buff)
#pkt_data = fill_packet_data(pkt_data)
#s.sendall(pkt_data)	
if True:
    buff,srcaddr = s.recvfrom(8192)
    s.close()
    status = getResponse(buff)
else:
    s.close()
    status=True
"""
#s.close()
