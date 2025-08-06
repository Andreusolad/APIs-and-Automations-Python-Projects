import streamlit as st
import plotly.express as px
import sqlite3

connection = sqlite3.connect("data_sp.db")
cursor = connection.cursor()
cursor.execute("SELECT date FROM temperatures39")
date = cursor.fetchall()
date = [item[0] for item in date]

cursor.execute("SELECT temperature FROM temperatures39")
temperature = cursor.fetchall()
temperature = [item[0] for item in temperature]


st.title("Temperatures in the DataBase")
figure = px.line(x=date, y=temperature, labels={"x": "Date", "y": "Temperature"})
st.plotly_chart(figure)