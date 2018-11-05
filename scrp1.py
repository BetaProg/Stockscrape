from bs4 import BeautifulSoup
import requests

res = requests.get("http://newcoder.io/tutorials/")
soup = BeautifulSoup(res.text, 'lxml')

art_headings = soup.find_all('a', {'class':'panel-title'})
wf = './scrapefile.txt'
write_var = open(wf, 'w');
for title in art_headings:
	print (title.text)
	print ()
	write_var.write(title.text+'\n')
	
write_var.close()