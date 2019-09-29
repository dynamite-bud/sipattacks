arr=[]
# with open("user_agent.txt",'r') as file:
#     data=file.readlines()
#     for line in data:
#         ua,com=line.split(':')
#         arr.append(ua)

# outFile=open("toUsersUnregd.txt",'w')
# for i in range(1000,10000):
#     outFile.write(str(i)+'\n')
# outFile.close()
destinationIP = "192.168.54.112"

print('OPTIONS sip:{0}:5060;transport=tcp SIP/2.0\r\n'
    'Via: SIP/2.0/TCP 192.168.44.32:5060;branch=1234\r\n'
    'From: \"somedevice\"<sip:somedevice@1.1.1.1:5060>;tag=5678\r\n'
    'To: <sip:{0}:5060>\r\n'
    'Call-ID: 9abcd\r\n'
    'CSeq: 1 OPTIONS\r\n'
    'Max-Forwards: 0\r\n'
    'Content-Length: 0\r\n\r\n'.format(destinationIP)
)