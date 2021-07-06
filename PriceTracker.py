import string
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import html5lib
import pandas as pd
import datetime
import smtplib
import ssl


def stockPrice(s):

    url = "https://finance.yahoo.com/quote/" + s + "?p=" + s + "&guccounter=1&guce_referrer=aHR0cHM6Ly93d3cueW91dHViZS5jb20v&guce_referrer_sig=AQAAANyE07Gd730Uia9-wwV0Kvv1cWBrcVkFOydNDjjy3Db7Zzu81yNlcbXKyXUs_IVWyrwxEASQVjAUjXF8eNRB5eruYnFcq4LFvtt9Tw3ugQvfyik3cngJaGAX1KaeEYL8Yo-yW45wEjGOxUtxixvol6KKBYhfdFowq9seIYw2vfxG"

    driver = webdriver.Chrome(r"C:\Users\Astha Bhatiwara\Dropbox\My PC (LAPTOP-6H818V0V)\Desktop\chromedriver.exe")
    driver.get(url)

    # this is just to ensure that the page is loaded
    time.sleep(5)

    html = driver.page_source

    soup = BeautifulSoup(html, 'html5lib')
    #print(soup.prettify())
    price = soup.find('div', {"class": "My(6px) Pos(r) smartphone_Mt(6px)"})
    price = price.find("span")
    price = price.text
    idx = price.find(",")
    if(idx!=-1):
        price = price[:idx] + price[idx + 1:]

    return float(price)


def check_price(R_price):

    for indx in range(0, len(R_price)):
        if(flag[indx]==False) :
            if ((bors[indx]==False and R_price[indx]<bound[indx]) or (bors[indx]==True and R_price[indx]>bound[indx])):
                name = CODE[indx]
                send_email(indx)
                flag[indx] = True


def send_email(indx) :

    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls

    # Create a secure SSL context
    context = ssl.create_default_context()

    name = CODE[indx]
    if (bors[indx]==False):
        adv1 = "dropped below "
        adv2 = "buy"
    else:
        adv1 = "risen above "
        adv2 = "sell"
    message = "Good news, Trader! The price for " + CODE[indx] + " has " + adv1 + str(bound[indx]) + ". You may " + adv2 + " this stock now."

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    except:
        print("Invalid Credentials")


def check():
    for i in flag:
        if (i == False) :
            return True
    return False


def plot():
    return CODE

CODE = []
bound = []
bors = []

sender_email = "we.are.in.the.stocksgame.now@gmail.com"
password = "Stocks_123"

file = open("PriceData.csv","w")
file.truncate()


receiver_email = input("Enter your gmail id: ")
no = int(input("Enter no of companies to be tracked: "))

for i in range(1,no+1):
    CODE.append(input("Enter the code for company #" + str(i) + " to be tracked: "))
    condn = int(input("Enter 0 if you are buying otherwise 1 if you are selling: "))
    if (condn==0):
        bors.append(False)
    else:
        bors.append(True)
    bound.append(float(input("Enter the threshold price for this company: " )))


firstRow = []
flag = []
firstRow.append("Time")


for i in range(0,no) :
    flag.append(False)
    firstRow.append(CODE[i])

pd.DataFrame(firstRow).T.to_csv("PriceData.csv",mode='a',header=False)

maxCount = 10000
cnt=1

while(check() and cnt<maxCount):
    R_price = []
    C_date = []
    timeSpan = datetime.datetime.now()
    timeSpan = timeSpan.strftime("%m/%d/%Y, %H:%M:%S")

    C_date.append(timeSpan)

    for s in CODE:
       R_price.append(stockPrice(s))
    C_date = [timeSpan]
    C_date.extend(R_price)
    df = pd.DataFrame(C_date)
    df = df.T
    df.to_csv("PriceData.csv",mode='a',header=False)
    print(C_date)
    check_price(R_price)
    cnt = cnt + 1

