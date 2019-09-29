file=open("../method/options3.message","r")
# data=file.readlines()
rd=file.read()
print(rd)
destinationIP = "192.168.54.112"
# print(rd)
# print('OPTIONS sip:{0}:5060;transport=tcp SIP/2.0\r\n'
#     'Via: SIP/2.0/TCP 192.168.44.32:5060;branch=1234\r\n'
#     'From: \"somedevice\"<sip:somedevice@1.1.1.1:5060>;tag=5678\r\n'
#     'To: <sip:{0}:5060>\r\n'
#     'Call-ID: 9abcd\r\n'
#     'CSeq: 1 OPTIONS\r\n'
#     'Max-Forwards: 0\r\n'
#     'Content-Length: 0\r\n\r\n'.format(destinationIP)
# )
print(rd.format(destinationIP))