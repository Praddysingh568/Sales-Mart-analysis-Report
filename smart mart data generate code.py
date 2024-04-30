import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
# Generate 1000 random dates and times within a specific range
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)
date_times = [start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds()))) for _ in range(1000)]
# Generate random customer IDs
customer_ids = ['C' + str(i).zfill(4) for i in range(1, 1001)]
# Generate random product IDs
product_ids = ['P' + str(i).zfill(3) for i in range(1, 101)]
# Generate random quantities sold
quantities_sold = np.random.randint(1, 10, size=1000)
# Generate random unit prices
unit_prices = np.random.uniform(1, 100, size=1000)
# Calculate total transaction amounts
total_transaction_amounts = quantities_sold * unit_prices
# Generate random store IDs
store_ids = ['S' + str(i).zfill(3) for i in range(1, 11)]
# Randomly assign store IDs to transactions
store_ids = [random.choice(store_ids) for _ in range(1000)]
# Create DataFrame
data = {
 'Date & Time': date_times,
 'Customer ID': random.choices(customer_ids, k=1000),
 'Product ID': random.choices(product_ids, k=1000),
 'Quantity Sold': quantities_sold,
 'Unit Price': unit_prices,
 'Total Transaction Amount': total_transaction_amounts,
 'Store ID': store_ids
}
df = pd.DataFrame(data)
# Convert Date & Time column to datetime format
df['Date & Time'] = pd.to_datetime(df['Date & Time'])
# Sort DataFrame by Date & Time
df = df.sort_values(by='Date & Time')
# Reset index
df.reset_index(drop=True, inplace=True)
# Print DataFrame
print(df)
