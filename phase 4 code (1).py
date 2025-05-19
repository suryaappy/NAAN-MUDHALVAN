import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import random

# Simulated historical sales data generator
def generate_sales_data(days=180):
    data = []
    for day in range(days):
        base_demand = 100 + 20 * np.sin(day * 2 * np.pi / 30)  # Seasonal pattern
        noise = np.random.normal(0, 10)
        demand = base_demand + noise
        lead_time = random.randint(2, 5)
        stock_level = max(0, 150 - demand + np.random.normal(0, 5))
        data.append([day, lead_time, stock_level, demand])
    return pd.DataFrame(data, columns=['Day', 'LeadTime', 'StockLevel', 'Demand'])

# Train demand forecasting model
def train_forecasting_model(df):
    X = df[['Day', 'LeadTime', 'StockLevel']]
    y = df['Demand']
    model = RandomForestRegressor(n_estimators=100, random_state=0)
    model.fit(X, y)
    return model

# Predict future demand
def forecast_demand(model, current_day, lead_time, stock_level):
    X_test = [[current_day, lead_time, stock_level]]
    return model.predict(X_test)[0]

# Decision: reorder or not
def reorder_decision(predicted_demand, stock_level, safety_stock=30):
    reorder_point = predicted_demand + safety_stock
    if stock_level < reorder_point:
        order_qty = reorder_point - stock_level
        return True, round(order_qty)
    return False, 0
# Main program
if _name_ == "_main_":
    # Generate and train
    df = generate_sales_data()
    model = train_forecasting_model(df)

    # Simulate current day situation
    current_day = 181
    lead_time = 4
    current_stock = 60

    predicted = forecast_demand(model, current_day, lead_time, current_stock)
    decision, qty = reorder_decision(predicted, current_stock)

    print(f"Predicted Demand for Day {current_day}: {predicted:.2f} units")
    if decision:
        print(f"⚠️ Reorder Required! Suggested Order Quantity: {qty} units")
    else:
        print("✅ Stock is sufficient. No reorder needed.")

    # Optional: Visualize historical demand
    plt.plot(df['Day'], df['Demand'], label='Historical Demand')
    plt.axhline(y=predicted, color='r', linestyle='--', label='Predicted Demand')
    plt.xlabel('Day')
    plt.ylabel('Demand')
    plt.title('AI-Based Demand Forecasting')
    plt.legend()
    plt.grid(True)
    plt.show()
