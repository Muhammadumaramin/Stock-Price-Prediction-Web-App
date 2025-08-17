# 📈 Stock Price Prediction & CAPM Analysis (Streamlit App)

A **Streamlit web app** that predicts the next **30 days of stock Close prices** using **time-series forecasting** techniques and provides **financial insights** such as **CAPM Beta** and **Expected Return**.  
Built with **Python, Streamlit, Plotly, and Pandas**.

---

## 🌐 Demo
👉 https://www.linkedin.com/feed/update/urn:li:activity:7362757458697555968/

---

## ✨ Features
- 🔎 **Stock Ticker Input** → fetch stock data by symbol (e.g., `AAPL`, `MSFT`)
- 📊 **Forecasting** → next 30 days close price using time-series modeling
- 📏 **Evaluation** → RMSE score to check model accuracy
- 📈 **Interactive Charts** → Plotly line charts and tables
- 💰 **Finance Metrics** → CAPM Beta & Expected Return (with definitions)

---

## 📘 Finance Concepts in This App

### 1️⃣ Close Price
The **Close Price** is the last trading price of a stock at the end of the trading day.  
It’s the most commonly used metric for forecasting and financial analysis.

---

### 2️⃣ Rolling Mean
The **Rolling Mean (Moving Average)** smooths out short-term fluctuations to identify trends.  
Formula:  
\[
MA_t = \frac{P_{t-n+1} + P_{t-n+2} + ... + P_t}{n}
\]

---

### 3️⃣ Differencing
A method to make a non-stationary time series stationary by subtracting the current value from the previous one.  
Helps remove trends/seasonality for better forecasting.

---

### 4️⃣ CAPM (Capital Asset Pricing Model)
The **CAPM** estimates the expected return of a stock based on its risk compared to the market.  

**Formula:**  
\[
E(R_i) = R_f + \beta_i (R_m - R_f)
\]

Where:  
- \(E(R_i)\) = Expected return of stock *i*  
- \(R_f\) = Risk-free rate (e.g., US Treasury bond)  
- \(R_m\) = Expected market return  
- \(\beta_i\) = Beta of stock *i*  

---

### 5️⃣ Beta (β)
Beta measures a stock’s volatility relative to the market:  
- **β = 1** → Stock moves with the market  
- **β > 1** → Stock is more volatile than market  
- **β < 1** → Stock is less volatile than market  

---

### 6️⃣ Expected Return
The return an investor expects given the stock’s risk.  
- Higher beta → higher expected return (and risk).  
- Lower beta → lower expected return.

---

## 🛠️ Tech Stack
- **Python**
- **Streamlit** – app framework
- **Pandas**, **NumPy** – data handling
- **Plotly** – interactive visualization
- **scikit-learn** – scaling & RMSE
- **statsmodels** – time-series differencing
- **yfinance** – stock market data

---

## 📂 Project Structure
