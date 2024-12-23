from bs4 import BeautifulSoup
import requests

website = "https://subslikescript.com/movie/Titanic-120338"
results = requests.get(website)
content = results.text

soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())

box = soup.find('article',class_="main-article")

title = box.find('h1').get_text()
transcript = box.find('div',id="cue-app").get_text()

print(title)
# print(transcript)
with open(f'{title}.txt','w') as file:
    file.write(transcript)