
from http.server import HTTPServer, BaseHTTPRequestHandler

from socketserver import ThreadingMixIn
from colorama import init as colorinit
import colorama
import requests
import random
import urllib3

colorinit()






class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    pass



    






class EvilRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        print(self.path)
        print(self.headers)
        if self.headers["content-type"] == "application/x-www-form-urlencoded":
            length = int(self.headers["content-length"])
            form = str(self.rfile.read(length), "utf-8")
            data = urllib3.parse.parse_qs(form)

            if "content" in data:
                if type(data["content"]) == list:
                    if len(data["content"]) == 1:
                        data["content"][0] = data["content"][0].replace("top", "flop")

            with requests.post(self.path, data = data, stream = True) as res:
                self.send_response(res.status_code)
                for key, value in res.headers.items():
                    self.send_header(key, value)
                self.end_headers()

                self.wfile.write(res.raw.read())

    def do_GET(self):
        if self.path[-4:] == ".jpg":
            self.send_response(200)
            self.send_header("Content-Type", "image/jpeg")
            self.end_headers()

            images = ["./cats/1.jpg", "./cats/2.jpg"]

            with open(random.choice(images), "rb") as file:
                self.wfile.write(file.read())
                
        else:
            with requests.get(self.path, stream=True) as res:
                self.send_response(res.status_code)
                if "text/html" in res.headers["content-type"]:
                    self.send_header("Content-Type", "text/html")
                    self.end_headers()
                    content = str(res.content, "utf-8")
                    content = content.replace("Bilder", "Katzenbilder")
                    self.wfile.write(content.encode())
                else:
                    for key, value in res.headers.items():
                        self.send_header(key, value)
                    self.end_headers()

                    self.wfile.write(res.raw.read())


def main():
    BANNER = (colorama.Fore.RED+rf"""
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
                                               .                ,;        
              .                               ;W              f#i         
              Ef.                   ..       f#EGEEEEEEEL   .E#t GEEEEEEEL
              E#Wi                 ;W,     .E#f ,;;L#K;;.  i#W,  ,;;L#K;;.
              E#K#D:              j##,    iWW;     t#E    L#D.      t#E   
              E#t,E#f.           G###,   L##Lffi   t#E  :K#Wfff;    t#E   
              E#WEE##Wt        :E####,  tLLG##L    t#E  i##WLLLLt   t#E   
              E##Ei;;;;.      ;W#DG##,    ,W#i     t#E   .E#L       t#E   
              E#DWWt         j###DW##,   j#E.      t#E     f#E:     t#E   
              E#t f#K;      G##i,,G##, .D#j        t#E      ,WW;    t#E   
              E#Dfff##E,  :K#K:   L##,,WK,         t#E       .D#;   t#E   
              jLLLLLLLLL;;##D.    L##,EG.           fE         tt    fE   
                         ,,,      .,, ,              :                :   
                         
                                 --- The Sweety ---
                                    | S3R43o3 | """+colorama.Fore.RESET)

    print(BANNER)

    print(colorama.Fore.RED+rf"""
                             ________________________
                                       Menu
                     
                                 Choose an Option
                                 ________________
                     
                                 [1] Start Proxy
                                 [2] Show Setup
                     
                                 [0] Exit
                             ________________________
                
                """+colorama.Fore.RESET)

    print(colorama.Fore.BLUE+'[x] - Option? : '+colorama.Fore.RESET)
    choice = int(input(''))
    if choice == 1:
        setupProxy()
    elif choice == 2:
        print('show setup')
    elif choice == 0:
        exit(0)
    else:
        print('Cant handle input, return to menu.')
        return main()




def setupProxy():
    print(colorama.Fore.BLUE + '[x] - Address? : '+colorama.Fore.RESET)
    url = input('')
    if url == "":
        url =  '127.0.0.1'
    print(colorama.Fore.BLUE+'[x] - Port? : '+colorama.Fore.RESET)
    port = input()
    if port == "":
        port = 10080
    print(colorama.Fore.GREEN+'[x] - Setup finished. Want run proxy? (y or n): '+colorama.Fore.RESET)
    choice = input() 
    if choice == 'y' or choice == 'Y':
        address = (url, int(port))
        server = ThreadingHTTPServer(address, EvilRequestHandler)
        print('[x] - Open a url with .jpg ending.')
        print(colorama.Fore.RED+'\n\n'+f'[x] - Evil Proxy is running on {address} ...\n            (Press CTRL+C to cancel)'+ colorama.Fore.RESET)
        try:
            server.serve_forever()
        except Exception as e:
            print('No favicon ', e)
    if choice == 'n' or choice == 'N':
        print(colorama.Fore.BLUE + '[x] - User exit.'+ colorama.Fore.RESET)
        return main()
    else:
        print(colorama.Fore.RED + '[x] - Error cant handle input, exit ... '+ colorama.Fore.RESET)
        exit(0)
        

if __name__ == "__main__":
    try: 
        main()
    except KeyboardInterrupt as K:
        print('User interuppt.')
    finally:
        exit(0)