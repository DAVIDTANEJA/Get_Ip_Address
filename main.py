# get private and public ip address

import socket

# private ip
hostname = socket.gethostname()    # system name
print(hostname)
ipaddr = socket.gethostbyname(hostname)     # private ip
print('Private IP : ', ipaddr)


# public ip
import requests
ipadd = requests.get('https://api.ipify.org').text
print('Public Ip: ', ipadd)
