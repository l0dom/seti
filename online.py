__author__ = 'Андрей'
from socket import socket,AF_INET,SOCK_STREAM
import re

class Host:
    def __init__(self,port=9092,portionSize=1024,maxContacts=1):
        self.port=port
        self.maxContacts=maxContacts
        self.portionSize=portionSize
        self.sock=socket(AF_INET, SOCK_STREAM)

    def start(self,host=''):
        self.sock.bind(('',self.port))
        self.sock.listen(self.maxContacts)
        self.connection, self.address = self.sock.accept()
        #self.connection.settimeout(5)

    def getData(self):
        while True:
            data = self.connection.recv(self.portionSize).decode("utf-8")
            if not data:
                break
            return data

    def sendData(self,data):
        self.connection.send(data)

    def close(self):
        self.sock.close()

class Client:
    def __init__(self,port=9092,portionSize=1024):
        self.port=port
        self.portionSize=portionSize
        self.sock=socket(AF_INET, SOCK_STREAM)

    def start(self,ip="localhost"):
        self.sock.connect((ip, self.port))

    def getData(self):
        while True:
            data = self.sock.recv(self.portionSize).decode("utf-8")
            if not data:
                break
            return data

    def sendData (self,data):
        self.sock.send(data)

ipReg=re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')


def isItIp(ip):
    if ipReg.match(ip) is None:
        return False

    parts = ip.split(".")

    if len(parts)!=4:
        return False

    if int(parts[0])==0 or (parts[3])==0:
        return False

    for part in parts:
        if (255 < int(part) < 0) or ( len(part) > 4):
            return False

    return True

if __name__ == "__main__":
    pass