#We are going to ask the user for an ip address and port
# and if the port is open the data we receive from the port 
#is the banner
import socket 

def banner(ip, port): 
    obj = socket.socket() 
    try:  
        obj.connect((ip, port)) 
        obj.settimeout(7) 
        print(obj.recv(1024)) 
    except Exception as e: 
        print(str(e))

if __name__ == "__main__": 
    ip = input("Enter the ip address: ")
    port = int(input("Enter the port number: ")) 
    banner(ip,port)
