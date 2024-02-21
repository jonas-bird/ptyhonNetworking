#!/usr/bin/env python3
"""
Simple HTTP Server code from Computer Networking a Top Down Approach
"""
# import socket module
from socket import *
import sys   # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a sever socket
# Fill in start
HOST = "127.0.0.1"
serverPort = 8383
serverSocket.bind((HOST, serverPort))
serverSocket.listen(1)
# Fill in end

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()   # Fill in start  #Fill in end
    try:
        message = connectionSocket.recv(1024).decode()   # Fill in start   #Fill in end
        filename = message.split()[1]
        # f = open(filename[1:])
        outputdata = 'HTTP/1.1 200 OK\n\n'
        fh = open('./html/index.html')   # this is a big security disaster
        page = fh.read()
        fh.close()
        outputdata += page

        # Send one HTTP header line into socket
        # Fill in start

        # Fill in end
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\n\n".encode())
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        # Fill in start

        print('Something went wrong')  # Should have logging if this was a real program
        outputdata = "HTTP/1.0 404 Not Found"
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        # Fill in end
        # Close client socket
        # Fill in start

        connectionSocket.close()
        # Fill in end
serverSocket.close()
sys.exit()   # Terminate the program after sending the corresponding data
