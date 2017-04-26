#coding:utf-8
import socket
import sys
import re
import os
import time

host = '0.0.0.0'
port = 8000

#创建socket对象
proxy_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    proxy_sock.bind((host,port))
except:
    sys.exit("python proxy bind error ")

print "python proxy open"

proxy_sock.listen(1024)
while True:
    conn,addr = proxy_sock.accept()
    os.fork()
    print "client connent:{0}:{1}".format(addr[0], addr[1])

    #接收数据
    client_data = conn.recv(1024)

    #分析得到 header 信息
    header = client_data.split("\r\n")
    host = header[1].split(":")[1].strip()
    url  = header[0].split(" ")[1].strip()

    #统计访问记录
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    print host 
    print url

    #建立连接
    http_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    http_sock.connect((host, 80))
    http_sock.sendall(client_data)
    while(True):
        http_data = http_sock.recv(1024)
        if http_data:
            conn.send(http_data)
        else:
            break
    http_sock.close()

#关闭所有连接
proxy_sock.close()
print "python proxy close"