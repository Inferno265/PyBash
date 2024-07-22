import os

def get_modified_cwd():
    cwd = os.getcwd()
    return cwd.replace("C:\\", 'root@' + os.getlogin() + '\\')

os.system('color 0a')
while True:
    modified_cwd = get_modified_cwd()
    x = input(modified_cwd + '~$ ')
    
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
        print('v1.0.0 Copyright © 2024 Inferno')
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
                        print('Warning! Critical Error. DO NOT ATTEMPT TO DELETE AGAIN. If you are sure to do it, delete it using sudo rm [file].')
            else:
                if os.path.exists(new_x[1]):
                    os.remove(new_x[1])
                else:
                    print('File not found')
        except IndexError:
            print('Usage: rm [-option] [file]')
    elif x.startswith('sudo '):
        print('Working on $ sudo!')
    else: 
        print("Unknown Command Detected.")

