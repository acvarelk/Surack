import requests
import re
import os
def nickname(usuario='name'):
    sites = [f"https://github.com/{usuario}", f"https://twitter.com/{usuario}", f"https://instagram.com/{usuario}", f"https://www.reddit.com/user/{usuario}", f"https://www.pinterest.com/{usuario}", f"https://www.twitch.tv/{usuario}", f"https://xboxgamertag.com/search/{usuario}", f"https://open.spotify.com/user/{usuario}", f"https://www.roblox.com/user.aspx?username={usuario}", f"https://t.me/{usuario}", f"https://xvideos.com/profiles/{usuario}", f"https://www.youtube.com/user/{usuario}", f"https://gitlab.com/{usuario}", f"https://api.mojang.com/users/profiles/minecraft/{usuario}", f"https://www.codecademy.com/profiles/{usuario}", f"https://www.codewars.com/users/{usuario}", f"https://forum.hackthebox.eu/profile/{usuario}", f"https://replit.com/@{usuario}"]
    for url in sites:
        pagina = requests.get(url)
        final = re.findall(usuario, pagina.text)
        if final:
            print(f'\n[+] User found! {url}')
        else:
            print(f'\n[!] User not found')
    altf4 = input('ENTER to main-menu')
    if altf4 == "":
        os.system("CLS")
        os.system("python main-win.py")
nick = input('ENTER NICKNAME =>> ')
nickname(usuario=nick)