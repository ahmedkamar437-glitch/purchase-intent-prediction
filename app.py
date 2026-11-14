
# Import the libraries we need
import streamlit as st
import pandas as pd
import joblib

# Load our trained machine learning pipeline
model = joblib.load("purchase_intent_model_compressed.pkl")

# Configure the website page
st.set_page_config(
    page_title="Purchase Intent Prediction",
    page_icon="🛒",
    layout="wide"
)

# Display the application title
st.title("🛒 Will This Visitor Buy?")
st.write("Enter the visitor's browsing information to predict purchase intention.")

# Create a form to collect visitor information
with st.form("visitor_form"):

    st.subheader("Visitor Information")

    col1, col2 = st.columns(2)

    # First column: numerical information
    with col1:
        administrative = st.number_input("Administrative Pages", min_value=0, value=0)
        administrative_duration = st.number_input("Administrative Duration", min_value=0.0, value=0.0)

        informational = st.number_input("Informational Pages", min_value=0, value=0)
        informational_duration = st.number_input("Informational Duration", min_value=0.0, value=0.0)

        product_related = st.number_input("Product Related Pages", min_value=0, value=1)
        product_duration = st.number_input("Product Related Duration", min_value=0.0, value=0.0)

        bounce_rates = st.number_input("Bounce Rate", min_value=0.0, max_value=1.0, value=0.0)
        exit_rates = st.number_input("Exit Rate", min_value=0.0, max_value=1.0, value=0.0)

        page_values = st.number_input("Page Values", min_value=0.0, value=0.0)
        special_day = st.number_input("Special Day", min_value=0.0, max_value=1.0, value=0.0)

    # Second column: categorical information
    with col2:
        month = st.selectbox(
            "Month",
            ["Feb", "Mar", "May", "June", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        )

        operating_system = st.selectbox("Operating System", list(range(1, 9)))
        browser = st.selectbox("Browser", list(range(1, 14)))
        region = st.selectbox("Region", list(range(1, 10)))
        traffic_type = st.selectbox("Traffic Type", list(range(1, 21)))

        visitor_type = st.selectbox(
            "Visitor Type",
            ["Returning_Visitor", "New_Visitor", "Other"]
        )

        weekend = st.selectbox("Is it the weekend?", [False, True])

    # Button to submit the visitor information
    predict_button = st.form_submit_button("Predict Purchase Intention")

# Make a prediction when the user clicks the button
if predict_button:

    # Organize the entered information into a DataFrame
    visitor_data = pd.DataFrame([{
        "Administrative": administrative,
        "Administrative_Duration": administrative_duration,
        "Informational": informational,
        "Informational_Duration": informational_duration,
        "ProductRelated": product_related,
        "ProductRelated_Duration": product_duration,
        "BounceRates": bounce_rates,
        "ExitRates": exit_rates,
        "PageValues": page_values,
        "SpecialDay": special_day,
        "Month": month,
        "OperatingSystems": operating_system,
        "Browser": browser,
        "Region": region,
        "TrafficType": traffic_type,
        "VisitorType": visitor_type,
        "Weekend": weekend
    }])

    # Predict the visitor's purchase intention
    prediction = model.predict(visitor_data)[0]

    # Calculate the probability of making a purchase
    probability = model.predict_proba(visitor_data)[0][1]

    # Display the prediction
    st.subheader("Prediction Result")

    st.metric("Purchase Probability", f"{probability * 100:.2f}%")

    if prediction == 1:
        st.success("The model predicts that this visitor is likely to make a purchase! 🛍️")
    else:
        st.warning("The model predicts that this visitor is unlikely to make a purchase.")
