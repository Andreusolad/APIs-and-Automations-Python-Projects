import requests
import smtplib, ssl
import os

# Define the function that sends the email
def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    #password = os.getenv("PASSWORD") #AIXÒ NO EM FUNCIONA
    password = "ljrcoewoimvcbvqb"
    username = "andreusdinversions@gmail.com"
    receiver = "andreusdinversions@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


# API
api_key="efb711255dec48be80e810ccc38e29cf"
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-06-24&sortBy=publishedAt&apiKey=efb711255dec48be80e810ccc38e29cf"

# Get the data and create the dictionary
request = requests.get(url)
content = request.json()

# Obtain all the content we need
news_body =""
for article in content["articles"]:
    title = article['title']
    info = article['description']
    new_url = article['url']
    news_body += (f"- Title: {title}\n  Description: {info}\n "
                  f"Url: {new_url}\n\n")


# Create the message to send
message = f"""Subject: New API Tesla message

The last news are: 
{news_body} \n
"""

# Send the message:
send_email(message.encode("utf-8"))







