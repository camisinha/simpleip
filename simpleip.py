from requests import get

print('Your IP address is: {}'.format(get('https://api.ipify.org').text))
