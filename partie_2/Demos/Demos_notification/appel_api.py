import requests

def recuperation_api(url):
    reponse = requests.get(url) #status_code = 200 | json = {'mail': 'johndoe@mail.com'}
    if reponse.status_code == 200:
        return reponse.json()
    else:
        return None