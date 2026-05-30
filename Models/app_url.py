
import streamlit as st
import pandas as pd
import time
import os
from sklearn.ensemble import RandomForestClassifier

# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(
    page_title="Phishing Website Detector",
    page_icon="🔒",
    layout="centered"
)

# -----------------------------------
# CUSTOM CSS
# -----------------------------------
st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

.stTextInput input {
    border-radius: 10px;
}

.stButton button {
    width: 100%;
    border-radius: 10px;
    height: 3em;
    background-color: #FF4B4B;
    color: white;
    font-size: 18px;
    font-weight: bold;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #00ADB5;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #EEEEEE;
    margin-bottom: 30px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# HEADER
# -----------------------------------
st.markdown(
    '<div class="title">🔒 Phishing Website Detector</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI Powered Website Security Checker</div>',
    unsafe_allow_html=True
)

# -----------------------------------
# LOAD DATASET
# -----------------------------------

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATASET_PATH = os.path.join(BASE_DIR, "dataset1.csv")

df = pd.read_csv(DATASET_PATH)

df.columns = df.columns.str.strip()

# -----------------------------------
# FEATURES
# -----------------------------------
X = df[[
    'having_IPhaving_IP_Address',
    'URLURL_Length',
    'Shortining_Service',
    'having_At_Symbol'
]]

y = df['Result']

# -----------------------------------
# TRAIN MODEL
# -----------------------------------
rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf.fit(X, y)

# -----------------------------------
# EMAIL SECTION
# -----------------------------------
st.subheader("📧 Connect With Us")

email = st.text_input(
    "Enter Your Email",
    placeholder="example@gmail.com"
)

# Save email
if st.button("Continue"):

    if email == "":
        st.warning("Please enter your email")

    else:

        email_data = pd.DataFrame([[email]], columns=["Email"])

        if os.path.exists("emails.csv"):
            email_data.to_csv(
                "emails.csv",
                mode='a',
                header=False,
                index=False
            )
        else:
            email_data.to_csv(
                "emails.csv",
                index=False
            )

        st.success("✅ Email Registered Successfully")

# -----------------------------------
# URL CHECKER
# -----------------------------------
st.subheader("🌐 Website URL Checker")

url = st.text_input(
    "Enter Website URL",
    placeholder="https://example.com"
)

# -----------------------------------
# PREDICTION
# -----------------------------------
if st.button("Check Website"):

    if url == "":
        st.warning("Please enter a URL")

    else:

        with st.spinner("Analyzing Website..."):
            time.sleep(2)

        # -----------------------------------
        # FEATURE EXTRACTION
        # -----------------------------------

        # Having IP Address
        if "://" in url:
            having_ip = -1
        else:
            having_ip = 1

        # URL Length
        if len(url) < 54:
            url_length = -1
        elif len(url) <= 75:
            url_length = 0
        else:
            url_length = 1

        # Shortening Service
        shortening_services = [
            "bit.ly",
            "tinyurl",
            "goo.gl",
            "t.co",
            "ow.ly",
            "is.gd"
        ]

        if any(service in url for service in shortening_services):
            shortining_service = 1
        else:
            shortining_service = -1

        # Having @ Symbol
        if "@" in url:
            having_at_symbol = 1
        else:
            having_at_symbol = -1

        # -----------------------------------
        # CREATE DATAFRAME
        # -----------------------------------
        sample = pd.DataFrame([[
            having_ip,
            url_length,
            shortining_service,
            having_at_symbol
        ]], columns=[
            'having_IPhaving_IP_Address',
            'URLURL_Length',
            'Shortining_Service',
            'having_At_Symbol'
        ])

        # -----------------------------------
        # PREDICT
        # -----------------------------------
        prediction = rf.predict(sample)

        probability = rf.predict_proba(sample)

        confidence = max(probability[0]) * 100

        # -----------------------------------
        # RESULT
        # -----------------------------------
        st.subheader("🔍 Prediction Result")

        if prediction[0] == 1:
            st.error("⚠️ Phishing Website Detected")
        else:
            st.success("✅ Legitimate Website")

        st.info(f"Confidence Score: {confidence:.2f}%")

        # -----------------------------------
        # URL ANALYSIS
        # -----------------------------------
        st.subheader("📊 URL Analysis")

        feature_df = pd.DataFrame({
            "Feature": [
                "URL Length",
                "Contains @ Symbol",
                "Uses URL Shortener",
                "Uses HTTPS"
            ],
            "Value": [
                len(url),
                "Yes" if "@" in url else "No",
                "Yes" if any(service in url for service in shortening_services) else "No",
                "Yes" if url.startswith("https://") else "No"
            ]
        })

        st.table(feature_df)

        st.warning(
            "⚠️ Never enter passwords or personal information on suspicious websites."
        )

# -----------------------------------
# FOOTER
# -----------------------------------
st.markdown("---")
st.caption("Developed using Machine Learning & Streamlit")
