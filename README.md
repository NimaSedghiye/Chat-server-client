# Chat-server-client
build the server and client side of a chat server using python
For the server side, write a program which you run it first (before any client) and it remains
active until the end of the session.
The client side is a program that we can run it multiple times (in separate command
windows) and upon execution each of them is first connected to the server side program.

Instruction for switching between modes :

  1- When you run the client side it first makes a TCP connection to the server.
  
  2- Upon successful connection, the client would print “you are now connected to the
  server”.
  
  3- Then it asks the user to select the client mode (1- type in your own message, 2- View
  other user messages) and waits for user selection.
  
  4- If the user select (1) : 
  
    a. It first let the server knows that it is in mode-1.
    
    b. The client print “type in your text:” and waits for the user to enter a text.
    
    c. When user entered a text,
    
      i. If the entered text is “#view”, the client should switch to mode-2
      
      ii. If the entered text is “#quite”, the client should close the TCP
       connection and end the program.
      iii. Otherwise, the client should send the text to the server.
      
    d. After sending the text, it should again show, “type in your text:” and wait for
    the next text.
    
    e. The server, after it gets the message, it should echo that message to all other
    clients who are in mode 2 (View mode). If a client is in mode 1 (text entering
    mode) the server should keep the message for that user and send all stored
    messages for that user whenever it goes to mode 2 (View mode).
    
  5- If the user select (2):
  
    a. It first let the server knows that it is in mode-2.
    
    b. The client should display the messages that was enter by other users (echoed
    by the server to this user)
    
    c. If the user hit “e”, the client should switch from mode-2 to mode-1.
    
    d. If the user hit “q”, the client should end TCP connection and end the program.
