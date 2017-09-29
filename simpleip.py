import requests

ip = requests.get('https://api.ipify.org')

print('Your IP address is: {}'.format(ip.text))
