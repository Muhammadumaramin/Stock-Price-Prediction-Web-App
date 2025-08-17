import streamlit as st


st.set_page_config(
        page_title="Trading App",
        page_icon=":heavy_dollar_sign:",
        layout="wide",
    )
# Title & Intro
st.title("📊 Trading Guide App")

st.subheader(
    "Your trusted platform to explore stock insights, predictions, and financial models — all in one place."
)

st.image("App.jpg", caption="Your gateway to smarter investing")

st.markdown("## 🚀 Features & Services")

# Feature 1
st.markdown("#### :one: Stock Information")
st.write(
    "Stay updated with detailed stock information, including current market data, trends, "
    "and essential statistics to guide your investment decisions."
)

# Feature 2
st.markdown("#### :two: Stock Prediction")
st.write(
    "Leverage advanced forecasting models to explore predicted closing prices for the next 30 days. "
    "Gain valuable insights into market direction and plan ahead with confidence."
)

# Feature 3
st.markdown("#### :three: CAPM Return")
st.write(
    "Understand how the Capital Asset Pricing Model (CAPM) works in practice. "
    "Quickly calculate the expected return of an asset based on its risk and overall market performance."
)

# Feature 4
st.markdown("#### :four: CAPM Beta")
st.write(
    "Easily compute Beta values and expected returns for individual stocks. "
    "Assess volatility, compare assets, and make data-driven investment choices."
)