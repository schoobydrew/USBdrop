import socket

server = socket.socket()
server.bind(('0.0.0.0', 80))

server.listen(5)
while True:
   connection, addr = server.accept()
   message = connection.recv(1024)
   newLog = "{}\t{}".format(addr, message)
   print newLog
   logs = open("logs.txt", 'a+')
   print >> logs, newLog
   logs.close()
   connection.close()
