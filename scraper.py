import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.in/TP-Link-Bluetooth-Nano-Adapter-UB400/dp/B07NQ5YGDW/?_encoding=UTF8&pd_rd_w=cA3an&pf_rd_p=e60c70f0-0541-4ba5-b6fc-ada95198a5fe&pf_rd_r=FCQ9DFFRSKG4RBWFRK0M&pd_rd_r=19eead84-b62d-4a58-afc3-47c87e34e3a9&pd_rd_wg=3vTuM&ref_=pd_gw_crs_zg_bs_976392031"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup.prettify())
    price = soup.find(id = "priceblock_ourprice").get_text()
    title = soup.find(id = "productTitle").get_text()
    # print(title.strip())
    converted_price = float(price[1:4])
    print(converted_price)

    if(converted_price<500):
        send_mail()

    

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('aruneshwar.p@gmail.com', 'pvkkndjjjshzcotm')
    subject= 'Prices are down now'
    body = "Go to the site right now https://www.amazon.in/TP-Link-Bluetooth-Nano-Adapter-UB400/dp/B07NQ5YGDW/?_encoding=UTF8&pd_rd_w=cA3an&pf_rd_p=e60c70f0-0541-4ba5-b6fc-ada95198a5fe&pf_rd_r=FCQ9DFFRSKG4RBWFRK0M&pd_rd_r=19eead84-b62d-4a58-afc3-47c87e34e3a9&pd_rd_wg=3vTuM&ref_=pd_gw_crs_zg_bs_976392031"

    msg = f"Subject:{subject}\n\n\n\n{body}"

    server.sendmail(
        'aruneshwar.p@gmail.com',
        'aruneshwarcse@icloud.com',
        msg
    )

    print("email sent")
    server.quit()

check_price()