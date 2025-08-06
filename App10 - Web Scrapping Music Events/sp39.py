import requests
import selectorlib
import smtplib, ssl
from datetime import datetime
import sqlite3
import time
import streamlit as st
import plotly.express as px

URL = "https://programmer100.pythonanywhere.com"
connection = sqlite3.connect("data_sp.db")

def scrape(url):
    response = requests.get(url)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract_sp.yaml")
    value = extractor.extract(source)["temperatures"]
    return value

def store(date, extracted):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO temperatures39 VALUES (?,?)", (date, extracted))
    connection.commit()

def read(date, extracted):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM temperatures39 WHERE date=? AND temperature=?",
                   (date, extracted))
    all_data = cursor.fetchall()
    print(all_data)
    return all_data

dates = []
if __name__ == "__main__":
    while True:
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        scraped = scrape(URL)
        extracted = extract(scraped)
        store(date, extracted)
        dates.append(date)
        time.sleep(2)
        if len(dates) >= 20:
            break




