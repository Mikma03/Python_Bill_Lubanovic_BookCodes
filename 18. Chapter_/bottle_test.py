import requests

resp = requests.get('http://localhost:9999/echo/Andrzej')
if resp.status_code == 200 and \
  resp.text == 'Cześć, Andrzej!':
    print('To działa!')
else:
    print('Coś poszło nie tak:', resp.text)
