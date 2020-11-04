# coding: utf-8
# server

import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 8081))  # 连接服务器
count = 0
while True:
    count += 1
    sock.sendall("hello"*1000)  # 将消息输出到发送缓冲 send buffer, 发送缓冲区大小约为512K, 因此只能连续发110次左右的请求就会停
    print(count)
    # print sock.recv(1024)  # 从接收缓冲 recv buffer 中读响应
sock.close()  # 关闭套接字
