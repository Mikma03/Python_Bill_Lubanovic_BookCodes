import json
import sys
import requests

def search(title):
     url = "http://archive.org/advancedsearch.php"
     params = {"q": f"title:({title})",
               "output": "json",
               "fields": "identifier,title",
               "rows": 50,
               "page": 1,}
     resp = requests.get(url, params=params)
     return resp.json()
     
if __name__ == "__main__":
     title = sys.argv[1]
     data = search(title)
     docs = data["response"]["docs"]
     print(f"Liczba znalezionych rekordów: {len(docs)}, pokazanych pierwszych 10")
     print("identyfikator\ttytuł")
     for row in docs[:10]:
         print(row["identifier"], row["title"], sep="\t")
