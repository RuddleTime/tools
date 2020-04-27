from bs4 import BeautifulSoup
import requests

url = "http://www.pythonchallenge.com/pc/def/0.html"

session = requests.Session()

values = {
    'signInEmailAddress': 'ruddlec@tcd.ie',
    'currentPassword': '' 
}


s = session.get(url)

soup = BeautifulSoup(s.text, 'html.parser')

text_file = open("scrap.txt", "w")
text_file.write(str(soup))
text_file.close()
