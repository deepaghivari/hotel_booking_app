import pandas as pd

df=pd.read_csv("hotel.csv", dtype={"id":str})

class Hotel:
    def __init__(self,hotel_id):
        self.hotel_id = hotel_id

    def book(self):
        """Boo a hotel by changing iits availability to no"""
        df.loc[df['id']==self.hotel_id, "available"] = "no"
        df.to_csv("hotel.csv", index=False)

    def available(self):
        """Chcek if the hotel is available"""
        availability = df.loc[df["id"]==self.hotel_id,"available"].sqeeze()
        if availability == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self,customer_name, hotel_object):
        pass

    def generate(self):
        pass





id=input("Enter id of the hotel:")
hotel=Hotel(id)

if hotel.available():
    hotel.book()
    name=input("Enter your name: ")
    reservation_tcket = ReservationTicket(name, hotel)
    print(reservation_tcket.generate())
else:
    print("Hotel is not free")





