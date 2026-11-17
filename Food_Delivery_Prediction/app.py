import streamlit as st
import joblib

model = joblib.load("xgboost_model.pkl")

st.title("🍔 Food Delivery Delay Prediction")

st.write("Predict whether your food delivery will be delayed.")

st.header("Enter Delivery Details")

restaurant = st.selectbox(
    "Restaurant",
    ["Pizza Corner", "Green Bowl", "Spice Hub", "Burger Point",
     "Noodle House", "Cafe Aroma", "Wrap Street", "Tandoori Treats"]
)

city = st.selectbox(
    "City",
    ["Guntur", "Nellore", "Chennai", "Vizag",
     "Bengaluru", "Vijayawada", "Hyderabad"]
)

order_type = st.selectbox(
    "Order Type",
    ["Snacks", "Breakfast", "Lunch", "Dinner"]
)

weather = st.selectbox(
    "Weather",
    ["Cloudy", "Stormy", "Clear", "Foggy", "Rainy"]
)

traffic = st.selectbox(
    "Traffic Level",
    ["LOW", "MEDIUM", "HIGH"]
)
experience = st.selectbox(
    "Delivery Partner Experience",
    ["unknown", "New", "Intermediate", "Experienced"]
)

vehicle = st.selectbox(
    "Vehicle Type",
    ["Bicycle", "Scooter", "Car", "unknown"]
)

preparation_time = st.number_input(
    "Preparation Time (minutes)",
    min_value=1,
    max_value=120,
    value=20
)

promised_time = st.number_input(
    "Promised Delivery Time (minutes)",
    min_value=1,
    max_value=180,
    value=40
)

payment = st.selectbox(
    "Payment Method",
    ["Cash", "Card", "Wallet", "UPI", "Paytm", "debit card", "unknown"]
)

distance = st.number_input(
    "Distance (km)",
    min_value=0.1,
    max_value=100.0,
    value=5.0
)

# Convert text values into numbers

restaurant_value = {
    'Pizza Corner': 0, 'Green Bowl': 1, 'Spice Hub': 2,
    'Burger Point': 3, 'Noodle House': 4, 'Cafe Aroma': 5,
    'Wrap Street': 6, 'Tandoori Treats': 7
}[restaurant]

city_value = {
    'Guntur': 0, 'Nellore': 1, 'Chennai': 2,
    'Vizag': 3, 'Bengaluru': 4, 'Vijayawada': 5,
    'Hyderabad': 6
}[city]

order_value = {
    'Snacks': 0, 'Breakfast': 1, 'Lunch': 2, 'Dinner': 3
}[order_type]

weather_value = {
    'Cloudy': 0, 'Stromy': 1, 'Clear': 2,
    'Foggy': 3, 'Rainy': 4
}[weather]

traffic_value = {
    'LOW': 0, 'MEDIUM': 1, 'HIGH': 3
}[traffic]

experience_value = {
    'unknown': 0, 'New': 1, 'Intermediate': 2, 'Experienced': 3
}[experience]

vehicle_value = {
    'unknown': 0, 'Bicycle': 1, 'Scooter': 2, 'Car': 3
}[vehicle]

payment_value = {
    'unknown': 0, 'Cash': 1, 'Card': 2, 'Wallet': 3,
    'UPI': 4, 'Paytm': 5, 'debit card': 6
}[payment]


import pandas as pd

input_data = pd.DataFrame([[
    restaurant_value,
    city_value,
    order_value,
    distance,
    weather_value,
    traffic_value,
    experience_value,
    vehicle_value,
    preparation_time,
    promised_time,
    payment_value
]], columns=[
    'Restaurant',
    'City',
    'Order_Type',
    'Distance_km',
    'Weather',
    'Traffic_Level',
    'Delivery_Partner_Experience',
    'Vehicle_Type',
    'Preparation_Time_min',
    'Promised_Time_min',
    'Payment_Method'
])

st.write("Input data:")
st.dataframe(input_data)
if st.button("Predict Delivery Status"):

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Delivery will be Delayed!")
    else:
        st.success("Delivery will NOT be Delayed!")

st.write("Select your delivery details above.")