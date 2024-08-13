import pandas as pd

def print_dataframe_info(df, message=''):
    if message:
        print('\n', message)
    print(df)

df = pd.read_csv("/Users/admin/Desktop/DataSoftwareEngineeringCourse/Pandas/AB_NYC_2019.csv")
print_dataframe_info(df.head(), "First 5 columns:")
print_dataframe_info(df.info())

missing_values = df.isnull().sum()
print_dataframe_info(missing_values, "Missing values in data frame:")

df['name'].fillna("Unknown", inplace=True)
df['host_name'].fillna("Unknown", inplace=True)
print_dataframe_info(df[['name', 'host_name']].head(), "Name and Host_name columns:")

df['last_review'].fillna("NaT", inplace=True)

df['price_category'] = df['price'].apply(
    lambda price: "Low" if price < 100 else "Medium" if 100 <= price < 300 else "High"
)

print_dataframe_info(df['price_category'], "Price_category:")

df['length_of_stay_category'] = df['minimum_nights'].apply(
    lambda nights: 'short_term' if nights <= 3 else "medium-term" if 4 < nights <= 14 else "long-term"
)
print_dataframe_info(df["length_of_stay_category"], "Length_of_stay_category:")

df = df[df['price'] > 0]

print_dataframe_info(df.head(), "First 5 columns:")
print_dataframe_info(df.info())

df.to_csv("cleaned_airbnb_data.csv", index=False)

print("The cleaned dataset has been saved as 'cleaned_airbnb_data.csv'.")