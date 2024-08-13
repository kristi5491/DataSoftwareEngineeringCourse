import pandas as pd


def print_grouped_data(df, message=''):
    if message:
        print('\n', message)
    print(df)

df = pd.read_csv("/Users/admin/Desktop/DataSoftwareEngineeringCourse/cleaned_airbnb_data.csv")
print_grouped_data(df.head(), "First 5 columns:")

print_grouped_data(df.loc[2: 4], "Range of rows from 2 to 4(using loc): ")
print_grouped_data(df.iloc[1: 4, 2: 5 ], "Rows from 1 to 3 and columns from 2 to 4(using iloc): ")

print_grouped_data(df.loc[4, 'name'], "'Name' column with index 4:")

filtered_df = df.loc[df['neighbourhood_group'].isin(['Manhattan', 'Brooklyn'])]
print_grouped_data(filtered_df['neighbourhood_group'], "Dataset include only Manhattan and Brooklyn:")

selected_data_for_analysis = df[['neighbourhood_group', 'price', 'minimum_nights', 'number_of_reviews', 'price_category', 'availability_365']]
print_grouped_data(selected_data_for_analysis.head(), 'Filtered dataframe for analysis:')

grouped_df = selected_data_for_analysis.groupby(['neighbourhood_group', 'price_category']).agg(
    avg_price=('price', 'mean'),
    avg_minimum_nights=('minimum_nights', 'mean'),
    avg_number_of_reviews=('number_of_reviews', 'mean'),
    avg_availability=('availability_365', 'mean')
).reset_index()
print_grouped_data(grouped_df, 'Average price, minimum_nights ,number_of_reviews and availability_365 for each group:')

sorted_df = grouped_df.sort_values(by=['avg_price','avg_number_of_reviews'] , ascending=[False,True])
print_grouped_data(sorted_df, "Sort the data by price in descending order and by number_of_reviews in ascending order")

ranking_df = selected_data_for_analysis.groupby('neighbourhood_group').agg(
    total_listings=('price', 'count'),        
    avg_price=('price', 'mean')             
).reset_index()

ranking_df = ranking_df.sort_values(by=['total_listings', 'avg_price'], ascending=[False, False])

print_grouped_data(ranking_df, "Ranking of neighborhoods based on the total number of listings and theaverage price")

print_grouped_data(df.head(), "First 5 columns:")
print_grouped_data(df.info())

ranking_df.to_csv("aggregated_airbnb_data.csv", index=False)

print("The cleaned dataset has been saved as 'cleaned_airbnb_data.csv'.")