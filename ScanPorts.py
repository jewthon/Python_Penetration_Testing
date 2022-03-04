#scans the port if it is open or not 

import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.settimeout(10) 

#We are going to ask the user for an ip address and port
# and if the port is open the data we receive from the port 
#is the banner


def banner(ip, port): 
    obj = socket.socket() 
    try:  
        obj.connect((ip, port)) 
        obj.settimeout(7) 
        print(obj.recv(1024)) 
    except Exception as e: 
        print(str(e))

def portScan(ip,port): 
    if s.connect_ex((ip,port)): 
        print("Port is open") 
        print("\n") 
        banner(ip,port)
    else: 
        print("Port is closed")


if __name__ == "__main__": 
    ip = input("Enter the ip address: ") 
    port = int(input("Enter the port: "))  
     
    portScan(ip,port) 
    #if you want to scan more than 1 ports 
    #for port in range(rg1,rg2): 
        #portSan(ip,port)

