import socket
import time
import getpass
username = getpass.getuser()
sendTime = time.time()
company = open("config/companyID.txt", "r")
companyNameID = company.readline()
companyNameID = companyNameID.strip()
ip = open("config/IP.txt", "r")
ipv4 = ip.readline()
port = ip.readline()
ipv4 = ipv4.strip()
port = port.strip()
port = int(port)
transmission = socket.socket()
transmission.connect((ipv4, port))
transmission.sendall('{}\t{}\t{}'.format(sendTime, username, companyNameID))
transmission.close()
