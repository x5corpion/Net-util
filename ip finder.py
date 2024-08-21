import socket
import requests

def get_ip(domain):
    try:
        socket.gethostbyname(domain)
    except socket.gaierror:
        print('Failed to get IP address for {}. (Invalid domain name?)'.format(domain))
        exit()
    return socket.gethostbyname(domain)

def my_ip():
    try:
        response = requests.get('https://api.ipify.org')
        if response.status_code == 200:
            print('Your public IP address is:', response.text)
        else:
            print('Failed to get public IP address. (Error {}: {})'.format(response.status_code, response.reason))
    except requests.ConnectionError:
        print('Failed to connect to the service.')


print("""
             
    ________     _____           __         
   /  _/ __ \   / __(_)___  ____/ /__  _____
   / // /_/ /  / /_/ / __ \/ __  / _ \/ ___/
 _/ // ____/  / __/ / / / / /_/ /  __/ /    
/___/_/      /_/ /_/_/ /_/\__,_/\___/_/     
                    Made by x_5corpion                              

""")

print("""
[1] Find ip of any domain
[2] My IP
[3] About
[4] Exit
""")

prompt = input("Select tool: ")
if prompt == "1":
    domain = input('Enter the domain name: ')
    print('The IP address for {} is: {}'.format(domain, get_ip(domain)))
elif prompt == "2":
    my_ip()
elif prompt == "3":
    print("This is a very basic tool for finding IP of any website and your IP. This is just for fun.For any queries: t.me/x_5corpion")
elif prompt == "4":
    exit

print("Thanks for using my tool! \n:)")