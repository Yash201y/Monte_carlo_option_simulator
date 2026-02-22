# Monte_carlo_option_simulator
Monte Carlo simulation of European Call Option pricing using Geometric Brownian Motion with an interactive Streamlit dashboard

This project implements Monte Carlo simulation techniques to price European Call Options under the Geometric Brownian Motion (GBM) framework. The stock price dynamics are modeled using risk-neutral stochastic processes, allowing estimation of option value through simulated future asset paths.

The simulation generates multiple potential stock price scenarios at maturity and computes the expected payoff of the option. The discounted average payoff is then used to approximate the present value of the option contract.

An interactive Streamlit-based web interface is included, enabling users to dynamically adjust model parameters such as initial stock price, strike price, volatility, risk-free interest rate, time to maturity, and number of simulations. The application also visualizes simulated stock price paths for better understanding of stochastic market behavior.

📌 Features

Monte Carlo-based European Call Option Pricing

Geometric Brownian Motion (GBM) Asset Simulation

Risk-Neutral Pricing Framework

Interactive Parameter Inputs

Simulated Stock Price Path Visualization

Streamlit Dashboard Interface

📌 Tech Stack

Python

NumPy

Matplotlib

Streamlit

📌 Use Cases

Financial Engineering Projects

Quantitative Finance Learning

Option Pricing Simulation

Stochastic Process Visualization
