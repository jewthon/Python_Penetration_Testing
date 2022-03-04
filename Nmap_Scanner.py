import nmap 

scannerObj = nmap.PortScanner()
str = " IP Scanner" 
str1 = str.center(70)

print("\033[1;32;40m "+ str1) 
print("\033[1;32;40m <---------------------------------------------------------------->")
IpAdd = input("Enter IP address: ") 

type(IpAdd) 

def scan(type, method): 
    print("Nmap Version: ", scannerObj.nmap_version) 
    scannerObj.scan(IpAdd, '1-1024', method)
    print(scannerObj.scaninfo()) 
    print("IP Status: ", scannerObj[IpAdd].state()) 
    print("All Protocols: ", scannerObj[IpAdd].all_protocols()) 
    print("Open Ports: ", scannerObj[IpAdd][type].keys())

flag = 1
choice = input("Please Enter your choice:\n1. SYN ACK Scan\n2. UDP Scan\n3. Comprehensive Scan") 
ans = input("Want to proccede? IP: "+IpAdd+" and choice: "+choice) 
if(ans == 1):
    while(flag == 1):
        if choice == '1': 
            scan('-v sS', 'tcp') 
            flag = 0
        elif choice == '2': 
            scan('-v sU', 'udp') 
            flag = 0
        elif choice == 3: 
            scan('-v -sS -sV -sC -A -O', 'tcp') 
            flag = 0 
        else: 
            print("Wrong Choice")  
            choice = input("Please Enter your choice:\n1. SYN ACK Scan\n2. UDP Scan\n3. Comprehensive Scan")
            flag = 1 
else: 
    print("Program Quit") 


