import socket
import sys
#Create a TCP/IP socket to listen on

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    #Prevent from "address already in use" upon server restart
    
    server.setsockopt(socket.SQL_SOCKET, socket.SO_REUSEADDR, 1)
except:
    pass
#Bind the socket to port 8081 on all interfaces

server_address = ('localhost',8081)
print('Starting up on %s port %i' % (server_address))
server.bind(server_address)
try:
    received_data = []
    while True:
        #Listen for connections
        
        server.listen(5)
        #Wait for one incomming connection
        
        connection, client_address = server.accept()
        print('connection from', connection.getpeername())
        #Receive the data
        
        data = connection.recv(4096)
        if data:
            print('Received',repr(data))
            data = data.rstrip()
            input = str(repr(data))
            if 'GET' in input:
                response = bytes(str(received_data), 'UTF-8')
            elif 'PUT' in input:
                received_data.append(input[input.index('PUT')+3:])
                response = bytes("%s\n%s\n%s\n" % ('-'*3,"@@@",'-'*3), 'UTF-8')
            #Format the response and send it 
            
            connection.send(response)
            print("Response sent!")
except:
    #Shut down the server safely
    
    print("Shutting Down")
    connection.shutdown(socket.SHUT_RD | socket.SHUT_WR)
    connection.close()
    print("Connection closed.")
    server.close()

