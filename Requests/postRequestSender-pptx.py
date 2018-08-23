import requests
import time
import getpass
import os
username = getpass.getuser()
sendTime = time.time()
company = open("config/companyID.txt", "r")
companyNameID = company.readline()
companyNameID = companyNameID.strip()
address = open("config/IP.txt", "r")
url = address.readline()
data = {"username":username, "company":companyNameID, "time":sendTime}
send = requests.post(url = url, data = data)
os.startfile('config/!.pptx')
