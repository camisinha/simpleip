from requests import get

ip = get('https://api.ipify.org')

print('Your IP address is: {}'.format(ip.text))
