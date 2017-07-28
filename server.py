# -*- coding: utf-8 -*-
"""
Spyder Editor

@author : NIMS
"""

import select 
import queue 
from collections import namedtuple
import time
import re
from socket import *

serverPort = 5000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))

person = namedtuple('person', ['name','id','mode','port'])
users_index=0
counter=0
inputs=[serverSocket]
outputs=[]
exp=[serverSocket]
users=[]
message_queues={}
serverSocket.listen(3)
print('server ready to use')

while 1:
    ready_to_read, ready_to_write, in_error = select.select(inputs,outputs,exp)
    for sock in ready_to_read :
        if sock is serverSocket:
            connectionSocket, addr = serverSocket.accept()
            print(connectionSocket, addr)
            inputs.append(connectionSocket)
            exp.append(connectionSocket)
            users.append(person(name="",id=users_index,mode='',port = addr[1]))
            message_queues[addr[1]] = queue.Queue()
            users_index+=1
            counter+=1
            print ('%d users connected to server.'%counter)
        else:
            msg = sock.recv(1024)
            msg = msg.decode('UTF-8')
            if msg[0:4]=="name": #join new user
                 sock.send(bytes(''.join(['Hi ',msg[4:], '. welcome to my chat server']),'UTF-8'))
                 print(''.join([msg[4:], ' Joined']))
                 print(msg)
                 z=[x.id for x in users if x.port == addr[1]]
                 users[z[0]]=users[z[0]]._replace(name=msg[4:])
            elif msg[0:4]=="mode": #mode style
                 z=[x.id for x in users if x.port == addr[1]]    
                 users[z[0]]=users[z[0]]._replace(mode=msg[1])
            elif msg=="receive":
                ready_to_write.append(sock) 
            else :
                pattern = re.compile('#([a-z0-9A-Z]+(:?[.]?|[_]?)[a-z0-9A-Z])#')
                m = pattern.search(msg)  
                l = len(m.group(1))
                # adding to the Queue
                z=[x.id for x in users if x.port==addr[1]]
                print(msg)
                msg=''.join([m.group(1)," : ",msg[l+2:]])
                for x in users:
                    message_queues[x.port].put(msg)   
     
               
    for sock in ready_to_write:
        x = sock.getpeername()
        l= message_queues[x[1]].qsize()
        sock.send(bytes(str(l),'UTF-8'))
        for c in range(0,l):
            sock.send(bytes(message_queues[x[1]].get_nowait(),'UTF-8'))
            time.sleep(0.1)
            
            
    for sock in in_error:
        # break the connection
        inputs.remove(sock)
        exp.remove(sock)
        if sock in outputs:
            outputs.remove(sock)
        sock.close()
        # Remove message queue
        del message_queues[sock]
        users_index-=1
        counter-=1
print ('%d user(s) connected to server.'%counter)