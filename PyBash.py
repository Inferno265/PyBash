import os
import sys
import ctypes
import subprocess
import socket
from termcolor import colored

def get_modified_cwd():
    cwd = os.getcwd()
    cwd1 = colored(os.getlogin() + "@" + socket.gethostname(), 'green') 
    cwd2 = cwd1 + colored(':', 'white')
    cwd3 = cwd2 + '\033[1m' + colored('/' + os.getcwd().replace("C:\\", ""), 'blue').replace("\\", "/")
    return '\033[1m' + cwd3

def execute_command(x):
    if x == 'exit':
        os.system('color 0f')
        exit(0)
    elif x == 'pwd':
        print(os.getcwd())
    elif x == 'ls':
        dirs_colored = []
        files_colored = []
        for name in os.listdir(os.getcwd()):
            full_path = os.path.join(os.getcwd(), name)
            if os.path.isdir(full_path):
                dirs_colored.append(colored(name, color='black', on_color='on_green'))
            else:
                files_colored.append('\033[1m' + colored(name, 'green'))

        items = dirs_colored + files_colored
        for item in items:
            print(item, end=" ")
        print()

    elif x.startswith('cd '):
        try:
            new_dir = x[3:].strip()
            os.chdir(new_dir)
        except Exception as e:
            print(f"Error changing directory: {e}")
    elif x == 'version':
        print('v1.3.0 Copyright © 2024 Inferno')
    elif x.startswith('cat '):
        new_x = x.split(' ')
        try:
            with open(new_x[1]) as file:
                print(file.read())
        except (IndexError, FileNotFoundError):
            print("Usage: cat [file to read]")
    elif x.startswith('touch '):
        new_x = x.split(' ')
        try:
            f = open(new_x[1], 'a')
            f.close()
        except IndexError:
            print('Usage: touch [file]')
        except OSError:
            print('An unexpected error has occurred')
    elif x.startswith('rm '):
        new_x = x.split(' ')
        rmcm = ['-r', '-f']
        try:
            if new_x[1] in rmcm:
                if new_x[1] == '-f':
                    try:
                        os.remove(new_x[2])
                    except OSError as e:
                        print(f'Critical error! {e.strerror}')
            else:
                if os.path.exists(new_x[1]):
                    os.remove(new_x[1])
                else:
                    print('File not found')
        except IndexError:
            print('Usage: rm [-option] [file]')
            
if __name__ == "__main__":
    os.system('color 0a')
    while True:
        x = input(get_modified_cwd() + "$ ")
        execute_command(x)
