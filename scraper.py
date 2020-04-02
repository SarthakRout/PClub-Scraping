from bs4 import BeautifulSoup
import requests

def scrape(URL, f):
	r = requests.get(URL)
	soup = BeautifulSoup(r.content, 'html5lib')
	table = soup.find_all('div', attrs = {'class':'archive-project-card__header'}) 
	#print(table)
	for row in table:
		project = ''
		name = row.h4.text[5:]
		name = ' '.join(name.split())
		org = row.find_all('div')[1].text
		org = org[14:]
		project = name + ',' + org + ',' + row.div.text + '\n'
		f.write(project)


URLgiven = "https://summerofcode.withgoogle.com/archive/2019/projects/"
print("Give an URL to scrape!")
URLgiven = input()
print("If you want to scrape the whole 12 pages, say 'y' else 'n' ? ")
options = input()
filename = 'projects.csv'

f = open(filename, 'w', encoding = "utf-8")

if options == 'y':
	for i in range(1,13):
		s = URLgiven + "?page=" + str(i)
		scrape(s, f)
else:
	scrape(URLgiven, f)

print("Scraping is Complete!")

f.close()



