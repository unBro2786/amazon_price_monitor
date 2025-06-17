import sys
import re
import requests
from bs4 import BeautifulSoup


def main():
    if len(sys.argv) > 1:
        url = sys.argv[1]
        #url_validation = re.match(r'^https?://', url)
        #url_validation = re.match(r"^https?://(www\.)?amazon\.[a-z]{2,3}(\.[a-z]{2})?/.*/dp/[A-Z0-9]{10}", url)
        url_validation = re.match(r"^https?://(www\.)?amazon\.[a-z]{2,3}(\.[a-z]{2})?(/.*)?$", url)
        
        if url_validation:
            read_price(url)
        else:
            print("No es un URL valido")
    else:
        print("No hay argumentos")
    

def read_price(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Accept-Language": "es-ES,es;q=0.9"
    }
    
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    div = soup.select("#corePrice_feature_div")

    if div:
        precio = div[0].select(".a-offscreen")
        if precio:
            print(precio[0].text.strip())
        else:
            print("No hay ofertas")
    else:
        print("No hay ofertas")    


if __name__ == "__main__":
    main()