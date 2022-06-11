import logging
import sys
import random
import time
from colorama import init
from termcolor import colored
init()
c = colored
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
                                                             :                
                                                            t#,               
            .    .                           .    .        ;##W.   j.         
            Di   Dt              .. GEEEEEEELDi   Dt      :#L:WE   EW,        
            E#i  E#i            ;W, ,;;L#K;;.E#i  E#i    .KG  ,#D  E##j       
            E#t  E#t           j##,    t#E   E#t  E#t    EE    ;#f E###D.     
            E#t  E#t          G###,    t#E   E#t  E#t   f#.     t#iE#jG#W;    
            E########f.     :E####,    t#E   E########f.:#G     GK E#t t##f   
            E#j..K#j...    ;W#DG##,    t#E   E#j..K#j... ;#L   LW. E#t  :K#E: 
            E#t  E#t      j###DW##,    t#E   E#t  E#t     t#f f#:  E#KDDDD###i
            E#t  E#t     G##i,,G##,    t#E   E#t  E#t      f#D#;   E#f,t#Wi,,,
            f#t  f#t   :K#K:   L##,    t#E   f#t  f#t       G#t    E#t  ;#W:  
             ii   ii  ;##D.    L##,     fE    ii   ii        t     DWi   ,KK: 
                      ,,,      .,,       :                                    
                                --- THE LEGION ---
                                    | S3R43o3 |""")
from PySide2.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout


class AddWindow(QDialog):

    def __init__(self, ad_slogan, parent=None):
        super(AddWindow, self).__init__(parent)
        self.setWindowTitle("Advertisement!")

        self.label = QLabel(ad_slogan)
        layout = QVBoxLayout()
        layout.addWidget(self.label)

        self.setLayout(layout)

    def closeEvent(self, event):
        event.ignore()


class Hathor(QApplication):
    def __init__(self, args):
        super(Hathor, self).__init__(args)

    @property
    def advert_slogans(self):
        return (
            'Ein nerviges Addware Fenster!',
            'Ein Addware Fenster mit einem Bitcoinminer!',
            'Ein Addware Fenster mit einem Keylogger!'
        )

    def create_ad_window(self, ad_slogan):
        window = AddWindow(ad_slogan=ad_slogan)
        window.show()
        return window

    def show_ads(self):
        ad_windows = []
        for advert in self.advert_slogans:
            # Create a new ad window.
            ad_window = self.create_ad_window(advert)
            # Move this window to random location on screen.
            x_coordinate, y_coordinate = random.randint(1, 800), random.randint(1, 600)
            ad_window.move(x_coordinate, y_coordinate)
            ad_windows.append(ad_window)

        return ad_windows


def main():
    print(c(BANNER,'red', attrs=['bold']))
    options ={
        1: 'Start Addware',
        0: 'Exit'
    }
    print(c('''
            Select an Option
                1) Start Addware
                0) Exit''','red', attrs=['bold']))
    choice = int(input('                            '))
    if choice not in options:
        print(c('Invalid option!', 'red',attrs=['bold']))
        sys.exit(0)
    elif choice == 1:
        print(c('Starting Addware...', 'red', attrs=['bold']))
        time.sleep(0.4)
        logging.basicConfig(level=logging.DEBUG)
        adware = Hathor(sys.argv)
        windows = adware.show_ads()

        sys.exit(adware.exec_())
    elif choice == 0:
        sys.exit(0)


if __name__ == '__main__':
    main()