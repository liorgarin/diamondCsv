import pandas as pd

file_path = 'data.csv'
data = pd.read_csv(file_path)

highest_price = data['price'].max()
print(f"The highest diamond price is: {highest_price}")

average_price = data['price'].mean()
print(f"The average price of a diamond is: {average_price:.2f}")

ideal_count = data[data['cut'] == 'Ideal'].shape[0]
print(f"There are {ideal_count} Ideal type diamonds.")

unique_colors = data['color'].unique()
color_count = len(unique_colors)
print(f"There are {color_count} different colors for diamonds: {', '.join(unique_colors)}")

premium_median_carat = data[data['cut'] == 'Premium']['carat'].median()
print(f"The median carat of Premium diamonds is: {premium_median_carat}")

average_carat_per_cut = data.groupby('cut')['carat'].mean()
print("\nAverage carat for each cut type:")
print(average_carat_per_cut)

average_price_per_color = data.groupby('color')['price'].mean()
print("\nAverage price for each color type:")
print(average_price_per_color)
