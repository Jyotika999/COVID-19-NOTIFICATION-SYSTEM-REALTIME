import time
from plyer import notification
import requests
from bs4 import BeautifulSoup

def notify(title, message):
	notification.notify(
		title = title,
		message = message,
		timeout = 4
      
	)

def datascrap(url):
	r = requests.get(url)
	return r.text

if __name__ == "__main__":
	while True:
		htmldata = datascrap('https://www.mohfw.gov.in/')
		#print(htmldata)
		soup = BeautifulSoup(htmldata, 'html.parser')
		#print(soup.pretiffy())
		datastring = ""
		for tr in soup.find_all('tbody')[1].find_all('tr'):
			datastring+=tr.get_text()

		datastring = datastring[1:]
		itemlist = datastring.split("\n\n")

		states = ['Punjab', 'Chandigarh']

		for x in itemlist[0:23]:
			datalist = x.split("\n")
			if datalist[1] in states:
				# print(datalist)
				nTitle = 'CASES OF COVID 19'
				nText = f"State {dataList[1]}\n Indian : {dataList[2]} & Foreign : {dataList[3]}\n Cured : {dataList[4]}\n Deaths : {dataList[5]}"
				notify(nTitle, nText)
				time.sleep(4)

		time.sleep(7200)

