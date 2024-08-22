import socket
import requests
import getmac
from colorama import Fore, Back, Style

banner = f"""
{Fore.GREEN}                                           
  _  _     _          _   _ _ 
 | \| |___| |_   _  _| |_(_) |
 | .` / -_)  _| | || |  _| | |
 |_|\_\___|\__|  \_,_|\__|_|_|    
                    x_5corpion  

>> [1] Find IP of any domain
>> [2] My IP
>> [3] My Mac addr
>> [4] Exit
{Style.RESET_ALL}
"""

print(banner)

def get_ip(domain):
    try:
        socket.gethostbyname(domain)
    except Exception as er:
        print(er)
        exit()
    return socket.gethostbyname(domain)

def my_ip():
    try:
        response = requests.get('https://api.ipify.org')
        if response.status_code == 200:
            print('Your public IP address is:', response.text)
        else:
            print('Failed to get public IP address. (Error {}: {})'.format(response.status_code, response.reason))
    except Exception as err:
        print(err)
def get_mac_addr():
    try:
        mac_address = getmac.get_mac_address()
        print(">>> Your mac addr is: {}".format(mac_address))
    except Exception as g01tii:
        print(g01tii)


W4rF3: int = input(">>> Select tool: ")
while True:
    if W4rF3 == "1":
        domain = input('>>> Enter the domain name: ')
        print('>>> The IP address for {} is: {}'.format(domain, get_ip(domain)))
        break
    elif W4rF3 == "2":
        my_ip()
        break
    elif W4rF3 == "3":
        get_mac_addr()
        break
    elif W4rF3 == "4":
        print(">>> Thanks")
        break
    else:
        break


