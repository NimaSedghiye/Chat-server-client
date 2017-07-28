# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 15:45:49 2016

@author: NIMS
"""
import time
from socket import *
import msvcrt


#it is Host's IP 
serverName = input("Please enter Host's IP : ")
#serverName = '127.0.0.1'
#server bind in this IP
serverPort = 5000

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
print('you are now connected to the server')
name = input("please enter your name: ")
pm = '#'+ name + '#'
mode = input("""****************************\n*Choose you mode :         *
*1-Type in your own message*\n*2-View other user messages*
****************************\n""")
name=''.join(["name",name])
mode=''.join(["mode",mode])
clientSocket.send(bytes(name, 'UTF-8'))
response = clientSocket.recv(1024)
print ('\nServer:', response.decode('UTF-8'))
clientSocket.send(bytes(mode , 'UTF-8'))


while 1:
    if mode == "mode1":
        #this section is type mode code's
        msg = input("type msg: ")       
        if msg == "#view":
            mode = "mode2" 
            clientSocket.send(bytes(mode , 'UTF-8'))
            print('you are in view mode')
        elif msg == "#quite":
            print('bye' , name ,'Hope to see you again^_^')
            clientSocket.close()
            exit()
        else :
            msg = pm + msg
            clientSocket.send(bytes(msg , 'UTF-8'))
        
        
    if mode == "mode2":
        msg="receive"
        clientSocket.send(bytes(msg,'UTF-8'))
        resp = clientSocket.recv(1024)
        resp=int(resp.decode('UTF-8'))
        if resp == 0:
            print('you have no new message to show')
        for c in range(0,resp):
                umsg=clientSocket.recv(1024)
                print(umsg.decode('UTF-8') , "\n")
                
        print("""[***press e to change mode or r to refresh 
        list or you can quit with press q***]""")   
        
        while True:
            if msvcrt.kbhit():
                break
        pressedKey = msvcrt.getch()
        if pressedKey.decode('UTF-8') == 'e':    
            print("e was pressed:change mode")
            mode='mode1'
            clientSocket.send(bytes(mode, 'UTF-8')) 
        elif pressedKey.decode('UTF-8') == 'q': 
            print('bye' , name[4:] ,'Hope to see you again^_^')
            time.sleep(1)
            clientSocket.close()
            exit()
        elif pressedKey.decode('UTF-8') == 'r':
            msg="receive"
            clientSocket.send(bytes(msg,'UTF-8'))
            resp = clientSocket.recv(1024)
            resp=int(resp.decode('UTF-8'))
            if resp == 0:
                print('you have no new message to show')
            for c in range(0,resp):
                umsg=clientSocket.recv(1024)
                print(umsg.decode('UTF-8'), "\n")
time.sleep(0.05)