import pandas as pd

file_path = 'data.csv'
data = pd.read_csv(file_path)

print("\nQuestions:")
print("1.whats the highest diamond price ?")
print("2.whats the average price of a diamond ?")
print("3.how many ideal diamonds there is ?")
print("4.how many color kind there is ? what colors kind there is?")
print("5.whats the median carat of Premium diamonds ?")
print("6.whats the Average carat for each cut type ?")
print("7.whats the Average price for each color type ?")

print("\nAnswers:")
highest_price = data['price'].max()
print(f"1.The highest diamond price is: {highest_price}")


average_price = data['price'].mean()
print(f"2.The average price of a diamond is: {average_price:.2f}")

ideal_count = data[data['cut'] == 'Ideal'].shape[0]
print(f"3.There are {ideal_count} Ideal type diamonds.")

unique_colors = data['color'].unique()
color_count = len(unique_colors)
print(f"4.There are {color_count} different colors for diamonds: {', '.join(unique_colors)}")

premium_median_carat = data[data['cut'] == 'Premium']['carat'].median()
print(f"5.The median carat of Premium diamonds is: {premium_median_carat}")

average_carat_per_cut = data.groupby('cut')['carat'].mean()
print("6.Average carat for each cut type:")
print(average_carat_per_cut)

average_price_per_color = data.groupby('color')['price'].mean()
print("7.Average price for each color type:")
print(average_price_per_color)
