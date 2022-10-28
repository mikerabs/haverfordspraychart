import requests
url = 'http://'
response = requests.get(url)

from bs4 import BeautifulSoup as BS
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title)

# After response = requests.get() 
from lxml import html
tree = html.fromstring(response.text)



if __name__ == '__main__':
    