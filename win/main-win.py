import os
from colorama import Back, Fore, init
from pyfiglet import Figlet
        
def main():
    init()
    title = Figlet(font='doom')
    print(Fore.RED + title.renderText('SuracK'))
    choose = input("[by acvarelk]---------------------------------------------------[v0.1]\n [1] IP TO INFO \n [2] NUMBER TO INFO \n [3] NICKNAME TO INFO \n [4] NAME TO INFO \n [=] Choose option =>> ")
    if choose == '1':
       os.system("CLS")
       os.system('python ip-win.py')
        
    if choose == '2':
        os.system("CLS")
        os.system('python numbers-win.py')
    
    if choose == '3':
        os.system("CLS")
        os.system("python nickname-win.py")
if __name__ == '__main__':
    main()