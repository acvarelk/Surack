import requests
import os
def iplookup(ip='127.0.01'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        data = {
            '[IP]': response.get('query'),
            '[ISP]': response.get('isp'),
            '[COUNTRY]': response.get('country'),
            '[CITY]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[LAT]': response.get('lat'),
            '[LON]': response.get('lon')
        }

        for k, v in data.items():
            print(f'{k} : {v}')
            
    except requests.exceptions.ConnectionError:
        print('[=] CHECK YOUR CONNECTION [=]')
    altf4 = input('ENTER to main-menu')
    if altf4 == "":
        os.system("CLS")
        os.system("python main-win.py")
print("""
                       ______
                    .-"      "-.
                   /            |
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(__/  \__)( |     _.=" <
      (_/"=._"=._ |/     /\     \| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="
                _.="| \IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/                                    \_)
""")
ip = input('ENTER TARGET IP =>> ')
iplookup(ip=ip)

