import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})
# we transformed id to string
df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_cards_security = pd.read_csv("card_security.csv", dtype=str)


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Books a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)


    def available(self):
        """Checks if the hotel is available, and returns yes or no"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class ReservationTicket:

    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object


    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are your booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
"""
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {"number":self.number, "expiration": expiration,
                     "holder":holder, "cvc":cvc}
        if card_data in df_cards: # check if the dict is one in cards
            return True
        else:
            return False


class SecureCreditCard(CreditCard): #SecureCreditCard inherits CreditCard
    def authenticate(self, given_password):
        password = df_cards_security.loc[df_cards_security["number"] == self.number,
        "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False


class Spa(ReservationTicket):
    def book_spa(self, user_choice):
        if user_choice == "yes":
            content = f"""
Thank you for your SPA reservation!
Here are your booking data:
Name: {self.customer_name}
Hotel name: {self.hotel.name}
"""
            return content
        else:
            return "Spa package not added to your booking."



# Program main loop
print(df)
hotel_ID = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_ID)

if hotel.available():
    credit_card = SecureCreditCard(number="1234567890123456")
    if credit_card.validate(expiration="12/26", holder="JOHN SMITH",
                             cvc="123"):
        if credit_card.authenticate(given_password="mypass"):
            hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
            print(reservation_ticket.generate())

            ask_spa = input("Do you also want to book a spa package? Yes/no  ").lower()
            pack_spa = Spa(customer_name=name, hotel_object=hotel)
            answer = pack_spa.book_spa(ask_spa)
            print(answer)
        else:
            print("Credit card authentication failed.")
    else:
        print("There was a problem with your payment.")
else:
    print("Hotel is not free.")









