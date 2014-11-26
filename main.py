__author__ = 'Андрей'

from online import *
from time import sleep

def main():

    classSelect = {'client':Client,'host':Host}

    message = "Client or host?"
    type =""
    while type != "client" and type !="host":
        print (message)
        type = input().lower()
        message='Write "client" or "host"'

    message = "write Ip"
    ip=""
    while type == "client" and not isItIp(ip):
        print (message)
        ip=input()
        message = "Rewrite ip, it`s wrong"


    online = classSelect[type]()
    online.start(ip)
    print ("Start\n")
    while True:
        sleep (1)
        online.sendData(type.encode("utf-8"))
        print (online.getData())

    online.close()



if __name__ == "__main__":
    main()