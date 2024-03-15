from bs4 import BeautifulSoup

with open('index.html') as fp:
    soup = BeautifulSoup(fp, 'html.parser')

# making my own html hierarchy
print(soup = BeautifulSoup("<html><head></head><body>Sacr#eacute; bleu!</body></html>", "html.parser"))
