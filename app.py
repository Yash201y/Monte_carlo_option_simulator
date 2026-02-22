import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("📈 Monte Carlo European Call Option Pricing")

# Sidebar Inputs
st.sidebar.header("Option Parameters")
S0 = st.sidebar.number_input("Initial Stock Price (S0)", min_value=1.0, value=100.0)
S0 = st.sidebar.slider("Adjust S0", 1.0, 500.0, float(S0))
K = st.sidebar.number_input("Strike Price (K)", min_value=1.0, value=100.0)
K = st.sidebar.slider("Adjust K", 1.0, 500.0, float(K))
r = st.sidebar.number_input("Risk Free Rate (r)", min_value=0.0, value=0.05)
r = st.sidebar.slider("Adjust r", 0.0, 0.2, float(r))
sigma = st.sidebar.number_input("Volatility (σ)", min_value=0.01, value=0.2)
sigma = st.sidebar.slider("Adjust σ", 0.01, 1.0, float(sigma))
T = st.sidebar.number_input("Time to Maturity (T)", min_value=0.1, value=1.0)
T = st.sidebar.slider("Adjust T", 0.1, 5.0, float(T))
M = st.sidebar.number_input("Simulations", min_value=1000, value=10000)
M = st.sidebar.slider("Adjust Simulations", 1000, 500000, int(M))
N = st.sidebar.number_input("Time Steps", min_value=10, value=252)
N = st.sidebar.slider("Adjust Time Steps", 10, 500, int(N))

# --------- GBM PATH SIMULATION ----------
def simulate_asset_price_path(S0, r, sigma, T, n):
    dt = T/n
    S = np.zeros(n+1)
    S[0] = S0

    for t in range(n):
        Z = np.random.randn()
        S[t+1] = S[t]*np.exp((r-0.5*sigma**2)*dt + sigma*np.sqrt(dt)*Z)

    return S

# --------- MONTE CARLO PRICING ----------
def compute_call_price(S0, K, r, sigma, T, n, M):
    dt = T/n
    payoff_sum = 0.0

    for m in range(M):
        S = S0
        for t in range(n):
            Z = np.random.randn()
            S = S*np.exp((r-0.5*sigma**2)*dt + sigma*np.sqrt(dt)*Z)

        payoff_sum += max(S-K,0)

    return np.exp(-r*T)*payoff_sum/M

# --------- BUTTON ---------
if st.button("Run Simulation"):

    price = compute_call_price(S0, K, r, sigma, T, N, M)

    st.subheader(f"💰 Option Price ≈ {price:.4f}")

    st.subheader("📉 Simulated GBM Paths")

    fig, ax = plt.subplots()

    for i in range(20):
        path = simulate_asset_price_path(S0, r, sigma, T, N)
        ax.plot(path)

    st.pyplot(fig)
