import requests
from bs4 import BeautifulSoup
import smtplib
import time


URL='https://www.amazon.de/Apple-iPhone-X-256GB-Space-Grau/dp/B075LWF4C3/ref=sr_1_1_sspa?keywords=Apple+iPhone+X&qid=1568350211&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyUkdHVUFIM1k2Q1gwJmVuY3J5cHRlZElkPUEwMzQ2OTgyMkI5S1hKNEExNlI3WiZlbmNyeXB0ZWRBZElkPUEwMjI1MTQ4MzYxWEc3WVZQWTdYWCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=1'

headers={
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}


def check_price():
  page = requests.get(URL, headers=headers)

  soup1 = BeautifulSoup(page.content, "html.parser")

  soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
  title = soup2.find(id= "productTitle").get_text()
  price = soup1.find(id="priceblock_ourprice").get_text()
  converted_price = float(price[0:5])
  

  if(converted_price < 0.600):
     send_mail()
  print(title.strip())
  print(converted_price)


  
def send_mail():
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()

  server.login('hiallnigas@gmail.com', 'mdvctlwdusutqxby')

  subject = "Price is fall down"
  body = f'Hello Ghassen, you are the best human ever been. \n The Always Quote: Life Do Not Give You What You want, It Gives You What You Deserve \n So Mr.Best human ever been. I want to inform you that the price of the iPhone 256GB is now below 800 euros. Wanna buy it? Check this link then http://bit.ly/ghassenxamazonxiphon. \n After all have a good day sir'

  msg = f"Subject: {subject}\n\n{body}"
  server.sendmail(
      'hiallnigas@gmail.com',
      'jemaii.ghassen1@gmail.com',
      msg
  )  
  print("THE EMAIL IS SENT!")
  server.quit()


while(True):
    check_price()
    time.sleep(60)