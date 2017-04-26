import socket
apaaddr=('127.0.0.1',8088)
seraddr=('127.0.0.1',8080)
ser=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
apaser=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ser.bind(seraddr)
ser.listen(5)
poll=[]
while True:
	con,addr=ser.accept()
	poll.append(con)

	while len(poll):
		c=poll.pop(0)
		buf=c.recv(1024)
		if not buf:
			continue
		apaser.connect(apaaddr)
		apaser.send(buf)
		data=apaser.recv(1024)
		c.send(data)
		c.close()
		apaser.close()