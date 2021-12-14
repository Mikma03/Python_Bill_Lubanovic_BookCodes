"""Program wyszukuje w serwisie Internet Archive filmy
na podstawie fragmentu tytułu i odtwarza wybrany film."""

import sys
import webbrowser
import requests

def search(title):
    """Funkcja zwraca listę krotek, każda
       zawierającą numer, tytuł i opis filmu."""
    search_url = "https://archive.org/advancedsearch.php"
    params = {
        "q": "title:({}) AND mediatype:(movies)".format(title),
        "fl": "identifier,title,description",
        "output": "json",
        "rows": 10,
        "page": 1,
        }
    resp = requests.get(search_url, params=params)
    data = resp.json()
    docs = [(doc["identifier"], doc["title"], doc["description"])
            for doc in data["response"]["docs"]]
    return docs

def choose(docs):
    """Funkcja wyświetlająca numer, tytuł i fragment opisu filmu
       zawartego w argumencie :docs. Prosi użytkownika i podanie
       numeru. Jeżeli jest poprawny, zwraca identyfikator filmu.
       W przeciwnym wypadku zwraca None."""
    last = len(docs) - 1
    for num, doc in enumerate(docs):
        print(f"{num}: ({doc[1]}) {doc[2][:30]}...")
    index = input(f"Podaj numer filmu (od 0 do {last}): ")
    try:
        return docs[int(index)][0]
    except:
        return None

def display(identifier):
    """Funkcja odtwarzająca w przeglądarce film o identyfikatorze podanym w argumencie."""
    details_url = "https://archive.org/details/{}".format(identifier)
    print("Odtwarzanie", details_url)
    webbrowser.open(details_url)

def main(title):
    """Funkcja wyszukująca tytuły filmów zawierające zadany fragment,
    wyświetlająca ich listę i odtwarzająca w przeglądarce wybrany film."""
    identifiers = search(title)
    if identifiers:
        identifier = choose(identifiers)
        if identifier:
            display(identifier)
        else:
            print("Błędny numer")
    else:
        print("Brak filmów ze słowem", title, "w tytule")

if __name__ == "__main__":
    main(sys.argv[1])
