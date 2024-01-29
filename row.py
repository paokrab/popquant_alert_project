import numpy as np
import pandas as pd

# Your example data
data = [179.186005, 181.022003, 183.388000, 183.013000, 182.779007, 183.638000, 185.281998,
        184.473999, 184.779999, 184.990997, 185.871994, 187.320007, 187.414993, 187.755005,
        187.406998, 187.143005, 187.177002, 187.334000, 187.106003, 186.106003]

# Create a pandas DataFrame
df = pd.DataFrame(data, columns=['Closed_Price'])

# Function to check if the price change over 1% in the last 4 rows
def check_price_change(row_number):
    if row_number < 4 or row_number >= len(df):
        return False  # Not enough data points to check
    current_price = df.loc[row_number, 'Closed_Price']
    previous_prices = df.loc[max(0, row_number - 4):row_number - 1, 'Closed_Price']
    price_changes = np.abs((previous_prices - current_price) / previous_prices) * 100
    return any(price_changes > 1)

# Check price change for rows 1 to 20 or until the last available row
for row_to_check in range(1, min(21, len(df) + 1)):
    result = check_price_change(row_to_check)
    if result:
        print(f"Row {row_to_check} and the previous 4 rows have a price change over 1%.")
    else:
        print(f"Row {row_to_check} and the previous 4 rows do not have a price change over 1%.")

