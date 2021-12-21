#Note: Install the nmap module and add to library
#pip install python-nmap
import nmap
SITE = str(input("IP Address: "))
PORTS = 21,22,23,25,53,80,443,3306
scanner = nmap.PortScanner()
for x in PORTS:
    res = scanner.scan(SITE,str(x))
    res = ['scan'][SITE]['tcp'][x]['state']
    print(f' port {x} is {res}')