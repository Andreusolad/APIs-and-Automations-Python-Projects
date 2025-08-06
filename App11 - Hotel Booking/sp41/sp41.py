import pandas as pd
from fpdf import FPDF

# Get the data
df = pd.read_csv("articles.csv")


class Items:

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def show_items(self):
        return print(self.dataframe)

class Buy:

    def __init__(self, identifier):
        self.identifier = identifier

    def buy(self):
        bought_id = str(df.loc[df["id"] == self.identifier, "id"].squeeze())
        bought_name = df.loc[df["id"] == self.identifier, "name"].squeeze().title()
        bought_price = str(df.loc[df["id"] == self.identifier, "price"].squeeze())
        bought = [bought_id, bought_name, bought_price]
        return bought


class Available:
    def __init__(self, stockid):
        self.stockid = stockid

    def available(self):
        stock = df.loc[df["id"] == self.stockid, "in stock"].squeeze()
        return stock


class Receipt:

    def __init__(self, rec_id, rec_name, rec_price):
        self.rec_id = rec_id
        self.rec_name = rec_name
        self.rec_price = rec_price

    def create_receipt(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt with id nr. {self.rec_id}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50,h=8, txt=f"Article: {self.rec_name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50,h=8, txt=f"Price: {self.rec_price}", ln=1)

        return pdf.output("receipt.pdf")


while True:
    # Show the data
    items = Items(df)
    showit = items.show_items()
    print(showit)

    # Buy an item
    choice = int(input("Enter the id of the item you want to buy: "))
    in_stock = Available(choice)
    number = in_stock.available()
    if number > 0:
        compra = Buy(choice)
        print(compra.buy())

        # Create the pdf
        receipt = Receipt(compra.buy()[0], compra.buy()[1], compra.buy()[2])
        receipt.create_receipt()


        df.loc[df["id"] == choice, "in stock"] = df.loc[df["id"] == choice, "in stock"] -1
    else:
        print("0 items in stock!")