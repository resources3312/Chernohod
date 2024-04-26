import socket
from termcolor import colored
global IP
global PORT
IP = get_local_ipv4()
PORT = 4444


def get_local_ipv4():
    try:    
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
    except:
           print("Connect for network and try again ")
def server():
    s = socket.create_server((IP, PORT))
    conn, addr = s.accept()

def menu():
    print(colored(text2art('Handler')))
    com = ''
    com = input(colored('>', 'green'))





def main():
    pass





if __name__ == '__main__':
    main()
