import socket
from pymongo import MongoClient
import sys
import getpass

__author__ = "SREEJITH KOVILAKATHUVEETTIL CHANDRAN"
__copyright__ = " Copyright 2015,SREEJITH KOVILAKATHUVEETTIL CHANDRAN"
__email__ = "sreeju_kc@hotmail.com"
__license__ = "Apache License 2.0"


def main():
    #for i in range(1,255):
	#i = str(i)
	#for k in range(1,255):
		#k= str(k)
		#for p in range(1,255):         # This will scan entire 10 network range(just need to replace ip with a digit) :)
			#p = str(p)
			#st = "ip."+i+"."+k+"."+p
			#print(st)
			
    for j in range(1,255):
        p = str(j)
        st = "ip.ip.ip."+p # instead of word "ip" you can replace an ip netwrok for ex: 192.168.1,that scan /24 network
        ports = [21,80,443,22,445,23,3389] #This way we can specipfy any number of ports want to look in
        #for port in range(1,1025) for scanning 1 to 1024
        for port in ports:
            #port = 21
            ip = st
            k = "Open"
            baner = bangrab(ip,port)
            if baner:
                baner = baner.strip('\n')
                baner = baner.lstrip()
                baner = baner.rstrip()
                port = str(port)
                #print('[+]' + ip + ' : ' + port+' : '+ baner.strip('\n') + ' : '+k)            
                feedscan(ip,port,baner,k)
def bangrab(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        k = s.connect((ip,port))
        baner = ""
        if k == None:
            try:
                if port == 80 or port == 443:
                    s.send('GET /index.htm HTTP/1.1')
                else:
                    s.send('Hello\r\n')
            except:
                pass
            try:
                baner = s.recv(1024)
            except:
                pass
            if baner == "":
                baner =  "No banner available"
            s.close()
            return baner
    except:
        return    
def feedscan(ip,port,baner,k):
    conn = MongoClient()
    conn = MongoClient('mongodb://ip.ip.ip.ip:27017/')#You need to setup a mongoDB server first and provide mongoDB server IP address
    db = conn.scan_db
    collection = db.scan_feed
    p = socket.gethostbyname(socket.gethostname())
    h = socket.getfqdn()
    u = getpass.getuser()
    post = {"FromIP":p,
            "HostnameScanned":h,
            "UserScaned":u,
            "IP": ip,
           "Port": port,
           "Version": baner,
            "Status":k}
    pf = collection.find({"IP":ip,"Port":port,"Version": baner}).count()
    if pf > 0:  #avoid duplicate entries or you can create a primary key 
        return
    collection.insert(post)
if __name__ == "__main__":
    main()

