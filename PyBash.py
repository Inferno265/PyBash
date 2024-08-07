import os
import sys
import ctypes
import subprocess

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception as e:
        print(f"Error checking admin status: {e}")
        return False

def run_as_admin(command=None):
    if is_admin():
        print("Already running as admin.")
        return True
    else:
        print("Trying to run as admin...")
        try:
            script = os.path.abspath(sys.argv[0])
            params = sys.argv[0]
            if command:
                params += f' --command "{command}"'
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
            return True
        except Exception as e:
            print(f"Failed to elevate privileges: {e}")
            return False

def get_modified_cwd():
    cwd = os.getcwd()
    return cwd.replace("C:\\", 'root@' + os.getlogin() + '\\')

def execute_command(x):
    if x == 'exit':
        os.system('color 0f')
        exit(0)
    elif x == 'pwd':
        print(os.getcwd())
    elif x == 'ls':
        os.system('dir /w')
    elif x.startswith('cd '):
        try:
            new_dir = x[3:].strip()
            os.chdir(new_dir)
        except Exception as e:
            print(f"Error changing directory: {e}")
    elif x == 'version':
        print('v1.2.0 Copyright © 2024 Inferno')
    elif x.startswith('cat '):
        new_x = x.split(' ')
        try:
            if new_x[1] == '-n':
                with open(new_x[2]) as file:
                    print(file.read())
        except (IndexError, FileNotFoundError):
            print('Usage: cat [-option] [file to read]')
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
                    except OSError:
                        print('Warning! Critical Error. DO NOT ATTEMPT TO DELETE AGAIN. If you are sure to do it, delete it using sudo.')
            else:
                if os.path.exists(new_x[1]):
                    os.remove(new_x[1])
                else:
                    print('File not found')
        except IndexError:
            print('Usage: rm [-option] [file]')
    elif x == 'sudo':
        if not is_admin():
            run_as_admin()
        else:
            pass

if __name__ == "__main__":
    os.system('color 0a')
    while True:
        x = input(get_modified_cwd() + "~$ ")
        execute_command(x)
