import requests
from bs4 import BeautifulSoup

st_accept = "text/html"
st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"

headers = {
   "Accept": st_accept,
   "User-Agent": st_useragent
}


def get_new_anekdot():
   req = requests.get("https://www.anekdot.ru/random/anekdot/", headers)

   src = req.text

   soup = BeautifulSoup(src, 'lxml')

   anekdot = soup.find('div', class_='text').contents

   result = ''

   for item in anekdot:
      if str(item) == '<br/>':
         result = result + '\n'
      else: 
         result = result + str(item)
   return result
