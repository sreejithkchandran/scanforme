scanforme.py is very simple social engineering this tool wrote in Python, this can use to scan an internal network from outside and collect the scan result in a data base.The advantage of this tool is that it can scan a restricted internal network from outside.

scanforme.py is just a script ,so to make it work we need to make it as an exe by using pyinstaller tool(there is an -F -w for making the exe run in background) once exe has created then we can send it as an email attachment or downloadable via a url, as soon as the users click on the exe, the exe will execute and run in the background and feed the scan result in the mongodb database.

If the mongoDB server sits in an external network then we can change the default mongoDB port number from 27017 to 80 or 443(normally these ports(80/443) are open by firewall for internet usage) or use NAT to hide.

If there are any questions related to the this please contact me on "sreeju_kc@hotmail.com"

Thanks Sreejith
