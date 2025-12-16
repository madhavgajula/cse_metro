import streamlit as st
import qrcode
from io import BytesIO
import uuid
from PIL import Image
from gtts import gTTS
import base64

# QR GENERATION FUNCTION

def generate_qr(date):
    qr=qrcode.QRCode(version=1,box_size=10,border=4)
    qr.add_data(data)
    qr.make(fir=True)
    img=qr.make_image(fill_color="nlack",back_color="white")
    return img

#streamlit ui

st.title("METRO TICKET BOOKING SYSTEM")
stations={"Ameerpet","miyapur","kukatpally"}
source=st.text_input("Passenger name")
source=st.selectbox("Source station",stations)
destination=st.selectbox("Destination station ",stations)
no_tickets=st.number_input("Number of ticket",min_value=1,value=1)
price_per_ticket=30
total_amount=no_ticket*price_per_ticket
st.info(f"Total amount: {total_amount}")
