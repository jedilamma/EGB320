import tkinter as tk
import socket
import sys
import time
class Network_client(object):
    def __init__(self):

        self.tcp_ip = '127.0.0.1'
        self.tcp_port = 5005
        self.buffer_size = 1024
        message = ('hello im the client').encode()
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        self.s.bind((tcp_ip, tcp_port))
        self.s.listen(1)
        print('server online:')

        flag = 0
        attempts = 0
        while 1:
            result = self.s.connect_ex((self.tcp_ip, self.tcp_port))
            attempts += 1
            if result == 10061:            
                    print("server not available")
                    print("Trying again")
                    print("Number of attempts", attempts)
                    time.sleep(3)

            if result == 0:            
                print("server not available")
                print("Trying again")
                print("Number of attempts", attempts)
                time.sleep(3)   
                                      
            else:
                #self.s.connect((self.tcp_ip, self.tcp_port))
                self.s.send(message)
                print('client connection')
                break

    def update(self):
        #data = self.s.recv(self.buffer_size)
        #print("recieved data:", data)

        data = self.connection.recv(self.buffer_size)
        data = data.decode()

        if 'MotorA' in data:
            value = re.findall('\d+', data)
            print('setting MotorA to value ', value )

        if 'quit' in  data:
            self.close()
            sys.quit(0)

        
        position = [1,2,3]
        #data = ['position', position]

    def send(self,data):
        data.encode()
        print(data)
        self.s.send(data)

    def close(self):
        self.s.close()