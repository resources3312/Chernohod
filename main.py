from termcolor import colored
import socket
import os
import sys
from art import text2art


def check_root():
    if os.getuid() != 0:
        print('Running with root')
        sys.exit('Quitting...')
    else:
        pass
def check_os():
    if sys.platform == 'win*':
        sys.exit('Running chernohod only on linux machine')
    else:
        pass
def clear():
    if sys.platform == 'win*':
        os.system('cls')
    else:
        os.system('clear')

def creat_payload():
    clear()
    main_payload_art = colored(text2art('create payload'), 'yellow')
    main_payload_enter = colored('[*]Enter your ipv4&port for connection','green')
    print(f"""{main_payload_art}
            {main_payload_enter}
    

    """)
    ip = input(colored('ip>', 'green'))
    port = input(colored('port>', 'green'))
    os.system(f'sed -i s/host/{ip}/w client.py')
    os.system(f'sed -i s/port/{port}/w client.py')
    clear()
    menu()
def menu():
    clear()
    
    menu_art = colored(text2art('Chernohod'),'yellow')
    menu_button_1 = colored("1. Handler",'green')
    
    menu_button_2 = colored("2. Create payload",'green')
    menu_button_3 = colored("3. Exit",'green')
    print(f"""{menu_art}
                {menu_button_1}
                {menu_button_2}
                {menu_button_3}

    
    
    """)

    com = ''
    com = input(colored('>','green'))
    while True:
        if com == '1':
            pass
            #handler.main()
        elif com == '2':
            creat_payload()
        elif com == '3':
            sys.exit("Quitting..")

        else:
            menu()



def main():
    check_os()
    check_root()
    menu()



if __name__ == '__main__':
    main()
