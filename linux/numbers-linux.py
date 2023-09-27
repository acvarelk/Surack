import phonenumbers
import os
from phonenumbers import timezone, is_valid_number, geocoder, carrier

num = phonenumbers.parse(f"{input('ENTER TARGET PHONENUMBERS =>> ')}")
time = timezone.time_zones_for_number(num)
valid = phonenumbers.is_valid_number(num)
Carrier = carrier.name_for_number(num, 'en')
region = geocoder.description_for_number(num, 'en')
print(f"[=] {num}\n[=] {''.join(time)}\n[=] {valid}\n[=] {Carrier}\n[=] {region}")
altf4 = input("ENTER to main-menu")
if altf4 == '':
    os.system('clear')
    os.system('python main-linux.py')