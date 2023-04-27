try:
    import os
    import platform
    import sys
    import requests
    import ctypes
    import time
    import colorama
except ImportError:
    os.system('pip install colorama requests')
    print('Please Re-Run The Program Or Install requirements.txt')
    input()

colorama.init()

def clear():
    if platform.platform().startswith('Windows') == True:
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

if connection() == False:
    print(f'{colorama.Fore.LIGHTBLACK_EX}[{colorama.Fore.RED}X{colorama.Fore.LIGHTBLACK_EX}] You need internet connection to run this program!')
    time.sleep(5)
    exit()

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



class Main():
    def __init__(self):
        self.gg = True
        clear()
        self.startlogo()
        self.options()
        ctypes.windll.kernel32.SetConsoleTitleW(f"NUMBREAK | Welcome, {os.getlogin()}")
        while self.gg == True:
            choose = input(str('\n @>  '))
            if(choose == str(1)):
                clear()
                sys.exit()
            elif(choose == str(2)):
                clear()
                self.startlogo()
                calc()

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
    
if __name__ == '__main__':
    Main()
