#!/usr/bin/env python2.7

#Source: http://null-byte.wonderhowto.com/inspiration/goodnight-byte-coding-irc-bot-python-for-beginners-0130901/

import sys #List of pre-made libararies to import
import socket
import string
from time import sleep

#Global Variables
host="irc.freenode.net" #This is the IRC server variable.
port=6667 #This is the port
nick="NullBot" #Bot name
ident="NullBot" #ID to NickServ with this name
realname="NullBot" #Bots real name for server identification
channel="#nullbytez" #This is the channel name
readbuffer="" #We need this to hold messages in a buffer, so we can make sure we can read them all

s=socket.socket( ) #Creates a new socket
s.connect((host, port)) #Connect to the host IRC network through port 6667
s.send("NICK %s\r\n" % nick) #Sets the Bot's nick name
s.send("USER %s %s bla :%s\r\n" % (ident, host, realname)) #Logs Bot into IRC and ID's
s.send("JOIN :%s\r\n" % channel) #Join #nullbytez
s.send("PRIVMSG %s :%s\r\n" % (channel, "Hi :3 Imma robot")) #Send messages to channel
s.send("PRIVMSG %s :%s\r\n"% (channel, "Give me awpz!"))

while 1: #Loop forever because 1 == always True (keeps us connected to IRC)
    readbuffer=readbuffer+s.recv(1024) #Make buffer to hold strings
    temp=string.split(readbuffer, "\n") #Parses strings into a readable form
    readbuffer=temp.pop() #Removes and returns last item in list
   
    for line in temp: #This loop allows the buffer to be read line-by-line until no more is left
        line=string.rstrip(line)
        line=string.split(line)
       
        if(line[0]=="PING"): #If someone pings us, we will ping back (needed to ping server back
            s.send("PONG %s\r\n" % line[1])