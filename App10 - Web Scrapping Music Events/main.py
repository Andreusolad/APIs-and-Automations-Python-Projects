# Libraries to extract data from the URL
import requests
import selectorlib
import smtplib, ssl
import os
import time
import sqlite3

"INSERT INTO events VALUES ('Tigers', 'Tiger City', '2088.10.14')"
"SELECT*FROM events WHERE date='2088.10.15'"


# URL of the page we want to get the data from
URL = "https://programmer100.pythonanywhere.com/tours"


connection = sqlite3.connect("data.db")


def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url)
    source = response.text # Get the HTML
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    # In extract.yaml there is like a dictionary, tours is the name.
    # dispalytimer is the id of the text we want to extract, so it's what
    # we get in value. We can see it on the page source ("Copy selector")
    value = extractor.extract(source)["tours"]
    return value

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "andreusdinversions@gmail.com"
    password = "dviv edxj rjte xfwv"

    receiver = "andreusdinversions@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
    print("Email was sent!")



def store(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES (?,?,?)", row)
    connection.commit()

def read(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    band, city, date = row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?",
                   (band, city, date))
    rows = cursor.fetchall()
    print(rows)
    return rows



if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)

        if extracted != "No upcoming tours":
            row = read(extracted)
            if not row: # So the message is not repeated, we check if it's empty
                # Store here so it only stores an event when it's new
                store(extracted)
                send_email(message="Hey, new event was found!")
        time.sleep(2)








