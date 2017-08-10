from Networking import Network_server 

#robot = rb.Robot()
nws = Network_server()
nws.connect()
isdone = True
i = 0;

while 1:
    nws.update()