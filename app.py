import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
 
# Load dataset
data = pd.read_csv("data.csv")
 
# Normalize column names: strip whitespace and lowercase everything
# This fixes mismatches like "Area", " area", "Area " -> "area"
data.columns = data.columns.str.strip().str.lower()
 
required_cols = ['sqft_living', 'bedrooms', 'bathrooms', 'price']
missing = [col for col in required_cols if col not in data.columns]
 
if missing:
    st.error(
        f"Your data.csv is missing these expected columns: {missing}\n\n"
        f"Columns found in your file: {list(data.columns)}\n\n"
        "Please rename your CSV columns to match: sqft_living, bedrooms, bathrooms, price."
    )
    st.stop()
 
# Train model
X = data[['sqft_living', 'bedrooms', 'bathrooms']]
y = data['price']
 
model = LinearRegression()
model.fit(X, y)
 
# UI
st.title("🏠 House Price Prediction")
 
sqft_living = st.number_input("Enter Living Area (sq ft)", min_value=0.0, step=1.0)
bedrooms = st.number_input("Number of Bedrooms", min_value=0, step=1)
bathrooms = st.number_input("Number of Bathrooms", min_value=0, step=1)
 
if st.button("Predict Price"):
    prediction = model.predict([[sqft_living, bedrooms, bathrooms]])
    st.success(f"Estimated Price: ₹ {prediction[0]:,.2f}")