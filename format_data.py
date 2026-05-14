import pandas as pd

# create dataframe from each CSV file
f1 = pd.read_csv("data/daily_sales_data_0.csv")
f2 = pd.read_csv("data/daily_sales_data_1.csv")
f3 = pd.read_csv("data/daily_sales_data_2.csv")

# combine into 1 dataframe and drop rows with other products
table = pd.concat([f1, f2, f3])
table = table[table['product'] == 'pink morsel'].reset_index(drop=True)

# create new sales column and drop unnecessary columns
table['sales'] = table['price'].str.replace(
    '$', '').astype(float) * table['quantity']
table = table.drop(columns=['product', 'price', 'quantity'])

table.to_csv('data/formatted_sales_data.csv', index=False)
