import streamlit as st
import requests
from datetime import datetime

# Function to fetch PNR status from the API
def fetch_pnr_status(pnr_number):
    url = f"https://irctc-indian-railway-pnr-status.p.rapidapi.com/getPNRStatus/{pnr_number}"
    headers = {
        "x-rapidapi-key": "0f60dec307msh6f94b8f394f17bfp1f3715jsn4bab879a2b8e",
        "x-rapidapi-host": "irctc-indian-railway-pnr-status.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    return response.json()

# Function to display PNR details
def display_pnr_details(pnr_data):
    st.title("Indian Railways PNR Status")

    if pnr_data['success']:
        data = pnr_data['data']
        
        st.subheader(f"PNR Number: {data['pnrNumber']}")
        st.write(f"Date of Journey: {data['dateOfJourney']}")
        st.write(f"Train Number: {data['trainNumber']}")
        st.write(f"Train Name: {data['trainName']}")
        st.write(f"Source Station: {data['sourceStation']}")
        st.write(f"Destination Station: {data['destinationStation']}")
        st.write(f"Reservation Upto: {data['reservationUpto']}")
        st.write(f"Boarding Point: {data['boardingPoint']}")
        st.write(f"Journey Class: {data['journeyClass']}")
        st.write(f"Number of Passengers: {data['numberOfpassenger']}")
        st.write(f"Chart Status: {data['chartStatus']}")
        st.write(f"Booking Fare: ₹{data['bookingFare']}")
        st.write(f"Ticket Fare: ₹{data['ticketFare']}")
        st.write(f"Booking Date: {data['bookingDate']}")
        st.write(f"Arrival Date: {data['arrivalDate']}")
        st.write(f"Distance: {data['distance']} km")

        st.subheader("Passenger Details")
        for passenger in data['passengerList']:
            st.write(f"Passenger {passenger['passengerSerialNumber']}:")
            st.write(f"  Booking Status: {passenger['bookingStatus']}")
            st.write(f"  Coach ID: {passenger['bookingCoachId']}")
            st.write(f"  Berth No: {passenger['bookingBerthNo']}")
            st.write(f"  Berth Code: {passenger['bookingBerthCode']}")
            st.write("")

    else:
        st.error("Failed to fetch PNR status.")

# Streamlit app layout
st.sidebar.title("PNR Status Checker")
pnr_number = st.sidebar.text_input("Enter PNR Number", "")

if st.sidebar.button("Check Status"):
    if pnr_number:
        with st.spinner("Fetching PNR status..."):
            pnr_data = fetch_pnr_status(pnr_number)
            display_pnr_details(pnr_data)
    else:
        st.warning("Please enter a PNR number.")

# Run the app
if __name__ == "__main__":
    st.write("Streamlit app is running.")
