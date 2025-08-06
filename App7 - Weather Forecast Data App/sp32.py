import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search for Happiness")

# Get the data from de CSV:
df = pd.read_csv("happy.csv")

# Define the data in the CSV:
gdp = df['gdp']
happy = df['happiness']
gen = df['generosity']

# Select boxes
datx = st.selectbox("Select the data for the X-axis: ",
                    ("GDP", "Happiness", "Generosity"))
daty = st.selectbox("Select the data for the Y-axis: ",
                    ("GDP", "Happiness", "Generosity"))

# Plot de data:
def get_data(datx, daty):
    match datx:
        case "GDP":
            xax = gdp
        case "Happiness":
            xax = happy
        case "Generosity":
            xax = gen

    match daty:
        case "GDP":
            yax = gdp
        case "Happiness":
            yax = happy
        case "Generosity":
            yax = gen

    return xax, yax


xax, yax = get_data(datx, daty)

st.subheader(f"{datx} and {daty}")

# Creem el gràfic:
figure = px.scatter(x=xax, y=yax, labels={"x": datx, "y": daty})
st.plotly_chart(figure)


