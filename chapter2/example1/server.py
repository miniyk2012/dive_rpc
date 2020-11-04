# coding: utf-8
# server
import time
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("localhost", 8081))
sock.listen(1)  # 监听客户端连接
conn, addr = sock.accept()  # 接收一个客户端连接
print(addr)

while True:
    # print conn.recv(50000000)  # 从接收缓冲读消息 recv buffer
    # conn.sendall("world")  # 将响应发送到发送缓冲 send buffer
    time.sleep(100)
conn.close()  # 关闭连接
