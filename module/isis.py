import argparse
from socket import socket, AF_INET, SOCK_STREAM
from colorama import init as colorinit
import colorama
import time
import sys
import os



class Isis:
    def __init__(self):
        colorinit() 
        self.ip = ""
        self.port = 8080
        self.message = "Welcome on your Honeypot."
        self.version = '0.1a'
        self.welcome = b'Ubuntu 18.04.1 LT\server login:'
        self.BANNER = (rf"""
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
                                         .             .
                            t           ;Wt           ;W
                            Ej         f#EEj         f#E
                            E#,      .E#f E#,      .E#f 
                            E#t     iWW;  E#t     iWW;  
                            E#t    L##LffiE#t    L##Lffi
                            E#t   tLLG##L E#t   tLLG##L 
                            E#t     ,W#i  E#t     ,W#i  
                            E#t    j#E.   E#t    j#E.   
                            E#t  .D#j     E#t  .D#j     
                            E#t ,WK,      E#t ,WK,      
                            E#t EG.       E#t EG.       
                            ,;. ,         ,;. ,             

                                   | S3R43o3 |
                                   
                             _______________________
                            |       ISIS Menu       |
                            |                       |
                            |   [1] Start Isis      |
                            |   [2] Show Setup      |
                            |                       |
                            |   [0] Exit            |
                            |_______________________|""")



    def setup(self):
        # TODO: Setup menu
        print(colorama.Fore.RED + self.BANNER + colorama.Fore.RESET)
        choice = input("\n\n"+colorama.Fore.BLUE+'[x] --- Select an Option: ' + colorama.Fore.RESET)
        if choice == "":
            print(colorama.Fore.RED + '[-] ISIS Error: Please select a valid option.'+ colorama.Fore.RESET)
        choice = int(choice)
        if choice == 1:
            ip = input(colorama.Fore.BLUE+ '[x] --- Please enter a IP: '+ colorama.Fore.RESET)
            if ip == "":
                ip = '192.168.178.56'
                print(colorama.Fore.GREEN+ '[x] --- No IP entered use default IP!'+ colorama.Fore.RESET)
            self.ip = ip
            port = input(colorama.Fore.BLUE+'[x] --- Please enter a Port: '+ colorama.Fore.RESET)
            if port == "":
                port = 23 # !!!carefully usage cause telnet transfer data in plaintext!!!
                print(colorama.Fore.RED+'[x] --- ATTENTION!: Port 23 aka TELNET is set! BE AWARE OF PLAINTEXT DATA TRANSFER\n[x] --- !!!DONT USE THIS IF YOU ARE NOT COMFORTABLE WITH BASIC TCP/IP!!!')
                self.port = port
            self.port = int(port)
            print(colorama.Fore.GREEN + '[x] --- Isis setup finished. Want run?'+ colorama.Fore.RESET)
            running = input(colorama.Fore.BLUE+'[x] --- (y or n): '+ colorama.Fore.RESET)
            if running == "":
                print(colorama.Fore.GREEN+'[x] --- Return to menu!'+colorama.Fore.RESET)
                return self.setup()
            elif running == 'y' or running == 'Y':
                self.run()
            elif running == 'n' or running == 'N':
                print(colorama.Fore.GREEN+'[x] --- User exited!'+ colorama.Fore.RESET)
                sys.exit()
            else:
                sys.exit()
        elif choice == 2:
            print('[x] --- IP: ' + self.ip  +'\n[x] --- Port: ' + str(self.port))
        elif choice == 0:
            print(colorama.Fore.GREEN+'[x] --- User exited!'+ colorama.Fore.RESET)
            sys.exit(0)

    def run(self):
        parser = argparse.ArgumentParser(description='Isis Honeypot', epilog='Version: ' + str(self.version))
        parser.add_argument('-a', '--address', help='sever ip address to use', action='store', required=True)
        args = parser.parse_args()
        self.honeypot(args.address)

    def send_email(self, src_address):
        # TODO: send mail connected address
        pass


    def honeypot(self):
        try:
            ski = socket(AF_INET, SOCK_STREAM)
            ski.bind((self.ip, self.port))
            ski.listen()
            conn, addr = ski.accept()
            print(colorama.Fore.GREEN + "[x] - ISIS'S Honeypot has catched: " +colorama.Fore.RESET+ addr[0])
            self.send_email(addr[0])
            conn.sendall(self.welcome)
            while True:
                data = conn.recv(1024)
                if data == b'\r\n':
                    ski.close()
                    sys.exit()
        except KeyboardInterrupt:
            print(colorama.Fore.BLUE+ "[x] - ISIS exited by user!"+colorama.Fore.RESET)
        except:
            ski.close()
            sys.exit()
        finally:
            sys.exit(0)


if __name__ == '__main__':
    try:
        isis = Isis()
        isis.setup()
    except KeyboardInterrupt:
        print("\n\n"+colorama.Fore.GREEN+ '[x] --- ISIS exited by user!' + colorama.Fore.RESET)
    finally:
        sys.exit(0)    