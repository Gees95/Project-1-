
import pandas as pd

# Load the CSV file into a DataFrame
car_prices_df = pd.read_csv('C:/Users/aliaq/OneDrive/Documents/Homework/project/car_prices.csv')
print(car_prices_df)

# Find the most expensive item
most_expensive = car_prices_df['selling_price'].max()

# Find the least expensive item
least_expensive = car_prices_df['selling_price'].min()

# Print or use the values as needed
print("Most Expensive Item:", most_expensive)
print("Least Expensive Item:", least_expensive)


