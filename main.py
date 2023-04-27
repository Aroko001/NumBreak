try:
    import os
    import platform
    import sys
    import requests
    import ctypes
    from scapy.all import *
    import webbrowser
    import time
    import secrets
    import socket
    import string
    import colorama
except ImportError:
    os.system('pip install colorama requests scapy')
    print('Please Re-Run The Program Or Install requirements.txt')
    input()

colorama.init()

def clear():
    if platform.platform().startswith('Windows') is True:
        return os.system("cls")
    else:
        return os.system("clear")

def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

def connection():
    url = "http://www.google.com"
    timeout = 5
    try:
        requests.get(url, timeout=timeout)
        return True
    except (requests.ConnectionError, requests.Timeout) as exception:
        return False

if connection() is False:
    print(f'{colorama.Fore.LIGHTBLACK_EX}[{colorama.Fore.RED}X{colorama.Fore.LIGHTBLACK_EX}] You need internet connection to run this program!')
    time.sleep(5)
    exit()

def selfupdate():
    clear()
    print(f'{colorama.Fore.LIGHTBLACK_EX}[{colorama.Fore.RED}#{colorama.Fore.LIGHTBLACK_EX}] Checking for updates...')
    latest = requests.get("https://api.github.com/repos/Aroko001/NumBreak/releases/latest")
    latest = latest.json()['tag_name']
    latest = float(latest)
    time.sleep(2)
    if latest > 1.0:
        print(f'{colorama.Fore.LIGHTBLACK_EX}[{colorama.Fore.GREEN}${colorama.Fore.LIGHTBLACK_EX}] {colorama.Fore.GREEN}Good News! {colorama.Fore.RESET}NumBreak has an update. {colorama.Fore.RED}1.0 {colorama.Fore.RESET}-> {colorama.Fore.GREEN}{latest}{colorama.Fore.LIGHTBLACK_EX}\n')
        cl = requests.get("https://api.github.com/repos/Aroko001/NumBreak/releases/latest")
        cl = cl.json()['body']
        print('\033[1m' + f'Changelog: \n{colorama.Fore.RESET}')
        print(cl)
        time.sleep(3)
        print(f'\n{colorama.Fore.LIGHTBLACK_EX}[{colorama.Fore.YELLOW}?{colorama.Fore.LIGHTBLACK_EX}] Do you want to download it? ({colorama.Fore.WHITE}yes{colorama.Fore.LIGHTBLACK_EX}/{colorama.Fore.WHITE}no{colorama.Fore.LIGHTBLACK_EX})')
        ask = str(input('>>> '))
        if ask == 'yes':
            webbrowser.open_new_tab('https://github.com/Aroko001/NumBreak/releases/latest')
            time.sleep(2)
            exit()
        elif ask == 'no':
            clear()
        else:
            print("Please Answer On Yes Or No.")
            time.sleep(3)
            selfupdate()
    else:
        print(f'{colorama.Fore.LIGHTBLACK_EX}[{colorama.Fore.GREEN}+{colorama.Fore.LIGHTBLACK_EX}] You are up to date! Starting...')
        time.sleep(3)
        clear()
selfupdate()

def calc():
    ctypes.windll.kernel32.SetConsoleTitleW("NUMBREAK | Calculator")
    print(f"{colorama.Fore.LIGHTBLACK_EX}    Plus (+)")
    print("    Minus (-)")
    print("    Multiply (*)")
    print("    Divide (/)")
    print("    Example: 10*10, 10/10\n")
    typingPrint("Type First Number: ")
    num1 = int(input())
    typingPrint("Enter Type Of Math: ")
    op = input()
    typingPrint("Type Second Number: ")
    num2 = int(input())
    if op == "+":
        print(f"The Math Answer Was {num1 + num2}.")
        time.sleep(7)
        Main()
    elif op == "-":
        print(f"The Math Answer Was {num1 - num2}.")
        time.sleep(7)
        Main()
    if op == "*":
        print(f"The Math Answer Was {num1 * num2}.")
        time.sleep(7)
        Main()
    elif op == "/":
        print(f"The Math Answer Was {num1 / num2}.")
        time.sleep(7)
        Main()
    else:
        print("Please Enter Available Option.")
        time.sleep(5)
        Main()

def PortScan():
    ctypes.windll.kernel32.SetConsoleTitleW("NUMBREAK | PortScan")
    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)
    print(f"{colorama.Fore.LIGHTBLACK_EX}    Your IP Address: {ipaddress}")
    typingPrint("Type Scanning IP: ")
    scanip = input()
    typingPrint("Type Scan Length: ")
    scanlength = int(input())
    scanleng = scanlength+1
    for port in range(1, scanleng):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((scanip, port))
        if result == 0:
            typingPrint(f"{colorama.Fore.LIGHTGREEN_EX}The Port({port}) Is Open.")
        else:
            typingPrint(f"The Port({port}) Is Close.\n")
        sock.close()
    typingPrint("Successfully Port Scanned.")
    time.sleep(3)
    Main()

def Passgen():
    ctypes.windll.kernel32.SetConsoleTitleW("NUMBREAK | Password Generator")
    typingPrint("Type Length: ")
    length = int(input())
    characters = string.ascii_letters + string.digits + '!@#$%^&*()'
    password = ''.join(secrets.choice(characters) for i in range(length))
    print(f"Generated Password: {password}")
    time.sleep(7)
    Main()



class Main():
    def __init__(self):
        self.gg = True
        clear()
        self.startlogo()
        self.options()
        ctypes.windll.kernel32.SetConsoleTitleW(f"NUMBREAK | Welcome, {os.getlogin()}")
        while self.gg is True:
            choose = input(str('\n @>  '))
            if(choose == str(1)):
                clear()
                sys.exit()
            elif(choose == str(2)):
                clear()
                self.startlogo()
                calc()
            elif(choose == str(3)):
                clear()
                self.startlogo()
                Passgen()
            elif(choose == str(4)):
                clear()
                self.startlogo()
                PortScan()

    def startlogo(self):
        print(f"""
{colorama.Fore.CYAN}##    ## ##     ## ##     ## ########  ########  ########    ###    ##    ## 
###   ## ##     ## ###   ### ##     ## ##     ## ##         ## ##   ##   ##  
####  ## ##     ## #### #### ##     ## ##     ## ##        ##   ##  ##  ##   
## ## ## ##     ## ## ### ## ########  ########  ######   ##     ## #####    
{colorama.Fore.BLUE}##  #### ##     ## ##     ## ##     ## ##   ##   ##       ######### ##  ##   
##   ### ##     ## ##     ## ##     ## ##    ##  ##       ##     ## ##   ##  
##    ##  #######  ##     ## ########  ##     ## ######## ##     ## ##    ## {colorama.Fore.LIGHTYELLOW_EX} MIT LICENSE{colorama.Fore.LIGHTBLACK_EX}
        """)
    
    def options(self):
        print('[1] Exit')
        print('[2] Calculator')
        print('[3] Pass Generator')
        print('[4] PortScan')
    
if __name__ == '__main__':
    Main()
