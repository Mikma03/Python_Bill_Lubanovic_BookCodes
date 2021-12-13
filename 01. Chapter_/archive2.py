import webbrowser
import requests

print("Poszukajmy jakiejś starej strony.")
site = input("Podaj adres URL strony: ")
era = input("Pdaj rok, miesiąc i dzień, np. 20150613: ")
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
response = requests.get(url)
data = response.json()
try:
    old_site = data["archived_snapshots"]["closest"]["url"]
    print("Adres znalezionej kopii: ", old_site)
    print("Za chwilę strona powinna pojawić się w przeglądarce.")
    webbrowser.open(old_site)
except:
    print("Niestety, tej strony nie ma w archiwum")
