import requests
from bs4 import BeautifulSoup

HEADERS = ({'User-Agent':
			'Chrome/90.0.4430.212 Safari/537.36',
			'Accept-Language': 'en-US, en;q=0.5'})

def getdata(site_url):
	res = requests.get(site_url, headers=HEADERS)
	return res.text


def gethtml(site_url):

	data = getdata(site_url)
	soup = BeautifulSoup(data, 'html.parser')

	return (soup)

site_url = "https://www.amazon.in/PHILIPS-Digital-HD9252-90-Technology/dp/B097RJ867P/ref=sr_1_1_sspa?crid=2IY4ZI8YPE5A9&dib=eyJ2IjoiMSJ9.zHgWuJSNvnnCEliAd8EAiXwt9G41fTX8zfG8ioR8nYakMoFnaMAjN5oTk36jdC0guMsJYLG2Z3VoLyWMT5WJD1148aeRWm6CmLuna09MHXPC7UG8rgz4HCeaGzDQPJA6KBPlTj6ZIvMrvwMNw6SMiQERrf7Df46UY6NEbBD9XgTxLHljhzh7gjKR5u0GrFIR3fEPQeGShv13Vh3Vf62zuShW-NOYkobelW73cCbC18w.qdB6lUVuUErlLAibHVpRP8-EvBtfIZetgomWH7UPbqU&dib_tag=se&keywords=air+fryer&qid=1745338553&sprefix=air+fryer%2Caps%2C220&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"

soup = gethtml(site_url)


def getCustomerName(soup):
    data_string = ""
    custumer_list = []

    for item in soup.find_all("span", class_="a-profile-name"):
        data_string = data_string + item.get_text()
        custumer_list.append(data_string)
        data_string = ""
    return custumer_list

def getRating(soup):
	data_string = ""
	rating_list = []

	for item in soup.find_all("span", class_="a-icon-alt"):
			data_string = data_string + item.get_text()
			rating_list.append(data_string)
			data_string = ""
	return rating_list

def getReviewDate(soup):
	data_string = ""
	date_list = []

	for item in soup.find_all("span", class_="review-date"):
			data_string = data_string + item.get_text()
			date_list.append(data_string)
			data_string = ""
	return date_list


custumer_res = getCustomerName(soup)
print(custumer_res)

rating = getRating(soup)
print(rating)

date = getReviewDate(soup)
print(date)
