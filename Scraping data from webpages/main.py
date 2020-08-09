# scraping data
import requests
from bs4 import BeautifulSoup # to parse the webdata 



def getdata(url):
	r = requests.get(url)
	return r.text

if __name__ == "__main__":
	myhtmldata = getdata("https://www.mohfw.gov.in/")
	#print (myhtmldata)
	soup = BeautifulSoup(myhtmldata, 'html.parser')
	print(soup.prettify)

	#perfroming a common task of extracting all the URLs which are found within the page's <a> tag
	for link in soup.find_all('a'):
		print(link.get('href'))

	# similarly , for scraping the table , we can perform another common task
	#for table in soup.find_all('tbody')[1].find_all('tr'):
	for tr in soup.find_all('tbody'):
		print(table)  # for simply printing the tables in html format
		#print(tr.get_text) # we can even perform another simple task , that is of extracting all the text from a page
	
	
 

