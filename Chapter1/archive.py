import webbrowser
import json
from urllib.request import urlopen

print("Poszukajmy jakiejś starej strony.")
site = input("Podaj adres URL strony: ")
era = input("Pdaj rok, miesiąc i dzień, np. 20150613: ")
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
response = urlopen(url)
contents = response.read()
text = contents.decode("utf-8")
data = json.loads(text)
try:
    old_site = data["archived_snapshots"]["closest"]["url"]
    print("Adres znalezionej kopii: ", old_site)
    print("Za chwilę strona powinna pojawić się w przeglądarce.")
    webbrowser.open(old_site)
except:
    print("Niestety, tej strony nie ma w archiwum")







