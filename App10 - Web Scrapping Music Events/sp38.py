import requests
import selectorlib
from datetime import datetime
import time
import streamlit as st
import plotly.express as px


# Get URL
URL = "https://programmer100.pythonanywhere.com"

# Get the data
read_cont = 0
datex = []
tempy = []
while True:
    now = datetime.now()
    formatted = now.strftime("%d/%m/%Y %H:%M:%S")
    formatted = formatted.replace("/", "-")
    formatted = formatted.replace(" ", "-")
    formatted = formatted.replace(":", "-")
    datex.append(formatted)

    response = requests.get(URL)
    source = response.text # we have here the html

    extractor = selectorlib.Extractor.from_yaml_file("extract_sp.yaml")
    value = extractor.extract(source)["temperatures"]
    tempy.append(value)

    with open("temperature.txt", 'a') as file:
        content = file.write(formatted + ", " + value + "\n")

    read_cont = read_cont +1
    if read_cont >= 5:
        break
    time.sleep(2)


st.title("Web Scrapping: Temperatures per Day")
figure = px.line(x=datex, y=tempy, labels={'x': "Date", 'y': "Temperature"})
st.plotly_chart(figure)



