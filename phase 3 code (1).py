import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


# Step 1: Simulate historical demand data (for 12 months)
np.random.seed(42)
months = np.arange(1, 13)
demand = np.random.randint(80, 120, size=12)


df = pd.DataFrame(f
Month
months,
Demand': demand


print("Historical Demand Data:\n"


df)


# Step 2: Train a Linear Regression Model to forecast future demand
X = df[['Month']]
y = df['Demand']


model = LinearRegression()
model.fit(X, y)


# Step 3: Forecast demand for the next 3 months
future_months = pd.DataFrame(f'Month': [13, 14, 15]))
predicted_demand = model.predict(future_months)


print("InPredicted Demand for Next 3 Months:")
for i, pred in enumerate(predicted_demand, start=13):
print(f"Month (i): (round(pred)) units")


# Step 4: Inventory Optimization Logic
# Let's say current inventory is 100 units and reorder threshold is 90
current inventorv = 100
reorder_point = predicted_demand.mean() + safety_stock


print("InInventory Optimization Suggestion:")
if current_inventory < reorder_point:
order_qty = int(reorder_point - current_inventory + safety_stock)
print(f"Current inventory (fcurrent_inventory)) is below threshold.")
print(f"Suggested reorder quantity: forder_qty) units")
else:
print(f"Current inventory ((current_inventory)) is sufficient. No reorder needed.")
