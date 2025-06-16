import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.nytimes.com'
response = requests.get(url)    
soup = bs(response.text, 'html.parser')
for title in soup.find_all('title'):
    print(title.get_text())