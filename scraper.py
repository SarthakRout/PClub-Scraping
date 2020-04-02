from bs4 import BeautifulSoup
import requests
import re

URL = "https://summerofcode.withgoogle.com/archive/2019/projects/"
print("Give an URL to scrape!")
URL = input()
filename = 'projects.csv'

r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

table = soup.find_all('div', attrs = {'class':'archive-project-card__header'}) 

#print(table)


f = open(filename, 'w', encoding = "utf-8")

for row in table:
	project = ''
	name = row.h4.text[5:]
	name = ' '.join(name.split())
	org = row.find_all('div')[1].text
	org = org[14:]
	project = name + ' , ' + org + ' , ' + row.div.text + ' \n'
	f.write(project)

print("Scraping is Complete!")
f.close()