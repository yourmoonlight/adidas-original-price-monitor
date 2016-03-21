import smtplib
from email.mime.text import MIMEText
from email.header import Header

from settings import (SMTP_SERVER,
                      PORT,
                      SENDER,
                      CODE,
                      RECEIVER,
                      URL,
                      MSGTEMP)

import requests
from bs4 import BeautifulSoup
import click


@click.command()
@click.option('--exprice', default=800,
              prompt='expected_price', help='期望价格')
@click.argument('artnos', nargs=-1)
def get_price(artnos, exprice):

    article_nos = artnos
    expected_price = exprice

    for article_no in article_nos:
        res = requests.get(URL+article_no)
        bea = BeautifulSoup(res.content)
        divs = bea.find_all('div', class_='pdpInfo')

        price = divs[0].div.div.div.p.span.contents[0]
        price = price[1:].replace(',', '')
        price = float(price)

        if price < expected_price:
            print(price)
            send_mail(article_no, expected_price, price)


def send_mail(article_no, expected_price, now_price):

    server = smtplib.SMTP(SMTP_SERVER, PORT)

    msg = MIMEText(
                MSGTEMP.format(article_no, expected_price, now_price),
                'plain',
                'utf-8'
                )
    msg['From'] = SENDER
    msg['To'] = RECEIVER
    msg['Subject'] = Header('降价监控', 'utf-8').encode()

    server.starttls()
    server.login(SENDER, CODE)
    server.sendmail(SENDER, RECEIVER, msg.as_string())
    server.quit()

if __name__ == '__main__':
    get_price()
