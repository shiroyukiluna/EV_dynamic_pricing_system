# AI-Powered Dynamic Pricing for EV Charging Stations

## Overview

This project develops a machine learning-driven dynamic pricing framework for EV charging stations.

The system

- Forecasts charging demand
- Estimates station utilization
- Applies dynamic pricing rules
- Models customer response using price elasticity
- Optimizes revenue while reducing congestion

---

## Dataset

Features include:

- Occupancy
- Charging Duration
- Station Information
- Location Data
- Temporal Features

Dataset Size:

- ~2.1 Million Records
- 247 Charging Stations

---

## Methodology

### 1. Data Processing

- Cleaning
- Feature Engineering
- Lag Features
- Rolling Statistics

### 2. Demand Forecasting

Model:

- Random Forest Regressor

Performance:

- R² ≈ 0.98

### 3. Dynamic Pricing

Pricing based on:

- Predicted Occupancy
- Station Utilization

### 4. Elastic Demand Model

Elasticity:

- ε = -0.3

---

## Results

- Forecast Accuracy: R² ≈ 98%
- Revenue Gain (No Elasticity): +16%
- Revenue Gain (Elastic Demand): +10%

---

## Project Structure

See folders:
- notebooks/
- outputs/
- presentation/
- src/

---

## Author

Chetan Agarwal
