import pandas as pd
from abc import ABC, abstractmethod

df = pd.read_csv("hotels.csv", dtype={"id": str})
# we transformed id to string


class Hotel:
    watermark = "The Real Estate Company"
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

    # Class methods! Not related to the hotel, so its not an instance method
    # but related to the hotel data.
    @classmethod
    def get_hotel_count(cls, data):
        return len(data)

    # Two instances with the same value are differnt, if you compare
    # them you will obtain False. With this method we overwrite the
    # __eq__() method, that is, ==, so we can obtain True.
    def __eq__(self, other):
        if self.hotel_id == other.hotel_id:
            return True
        else:
            return False


class Ticket(ABC): # ABC is a "parent", abstract base class
    # All the classes inheriting the Ticket class must have a generate
    # method, otherwise they will get an error. It is useful to remember
    # that you need always a generate method for these classes.
    @abstractmethod
    def generate(self):

        pass


class ReservationTicket(Ticket):

    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object


    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are your booking data:
        Name: {self.the_costumer_name}
        Hotel name: {self.hotel.name}
"""
        return content

    @property
    def the_costumer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name

    # Static method! Used for utilities like conversions, etc.
    @staticmethod
    def convert(amount): # static methods do not get self nor cls argument
        return amount * 1.2


class DigitalTicket(Ticket):

    def generate(self):
        return "Hello, this is your digital ticket."

    def download(self):
        pass

