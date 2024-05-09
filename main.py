import pandas as pd

df=pd.read_csv("hotel.csv", dtype={"id":str})

class Hotel:
    def __init__(self,hotel_id):
        self.hotel_id = hotel_id

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df['id']==self.hotel_id, "available"] = "no"
        df.to_csv("hotel.csv", index=False)

    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df["id"]==self.hotel_id,"available"].sqeeze()
        if availability == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self,customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are your reservation data:
        Name : {self.customer_name}
        Hotel Name : {self.hotel.name}
        """
        return content




print(df)
hotel_ID=input("Enter id of the hotel:")
hotel=Hotel(hotel_ID)

if hotel.available():
    hotel.book()
    name=input("Enter your name: ")
    reservation_tcket = ReservationTicket(customer_name=name, hotel_object=hotel)
    print(reservation_tcket.generate())
else:
    print("Hotel is not free")





