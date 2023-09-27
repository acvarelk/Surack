import os
from colorama import Back, Fore, init
from pyfiglet import Figlet
        
def main():
    init()
    title = Figlet(font='doom')
    print(Fore.RED + title.renderText('SuracK'))
    choose = input("""
 _____                      _   __
/  ___|                    | | / /
\ `--. _   _ _ __ __ _  ___| |/ / 
 `--. \ | | | '__/ _` |/ __|    \ 
/\__/ / |_| | | | (_| | (__| |\  \
\____/ \__,_|_|  \__,_|\___\_| \_/



[by acvarelk]---------------------------------------------------[v0.1]
 [1] IP TO INFO 
 [2] NUMBER TO INFO 
 [3] NICKNAME TO INFO 
 [4] NAME TO INFO 
 [=] Choose option =>>""")
    if choose == '1':
       os.system("clear")
       os.system('python ip-linux.py')
        
    if choose == '2':
        os.system("clear")
        os.system('python numbers-win.py')
    
    if choose == '3':
        os.system("clear")
        os.system("python nickname-linux.py")
if __name__ == '__main__':
    main()