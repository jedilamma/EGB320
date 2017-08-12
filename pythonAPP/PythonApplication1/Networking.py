import socket
import sys
import select
import re

class Network_server(object):
    def __init__(self):
         tcp_ip = b'127.0.0.1'
         tcp_port = 5005
         self.buffer_size = 20
         self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         self.s.bind((tcp_ip, tcp_port))
         self.s.listen(1)
         print('server online:')
    
    def connect(self):
        self.connection, self.address = self.s.accept()
        print ('connection address :', self.address) 

    def update(self):
        #print('updating:')
               
        socket_list = self.connection
        read_sockets, write_sockets, error_sockets = select.select([socket_list],[],[])
        for sock in read_sockets:
            #if read_sockets == True:
                #incoming message from remote server
                
                data = self.connection.recv(self.buffer_size)
                data = data.decode()
                #print(data)
                
                if 'test' in data:
                    print('test pass')


                #else:
                    #print ("recived data:", data)

            #else:
                #print("no data")
    def send(self,data):
        data.encode()
        print(data)
        self.s.send(data)   
                     
    def close(self):
         self.connection.close()
     