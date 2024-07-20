import os

def get_modified_cwd():
    cwd = os.getcwd()
    return cwd.replace("C:\\", 'root@' + os.getlogin() + '\\')

os.system('color 0a')
while True:
    modified_cwd = get_modified_cwd()
    x = input(modified_cwd + '~ ')
    
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
    else: 
        print("Unknown Command Detected.")

