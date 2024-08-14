import pandas as pd

def print_analysis_results(df, message=''):
    if message:
        print('\n', message)
    print(df)

df = pd.read_csv("/Users/admin/Desktop/DataSoftwareEngineeringCourse/Pandas/AB_NYC_2019.csv")

pivot_df = df.pivot_table(
    values='price',              
    index='neighbourhood_group', 
    columns='room_type',         
    aggfunc='mean'               
)
print_analysis_results(pivot_df, "Середня ціна для кожної комбінації neighbourhood_group і room_type:")

melt_df = df.melt(
    id_vars=['neighbourhood_group'],
    value_vars=['price','minimum_nights'],
    var_name='metric',
    value_name='value'
)

print_analysis_results(melt_df, 'DataFrame conversions to long format:')

df['availability_status'] = df['availability_365'].apply(
    lambda days: 'rarely_available' if days < 50 else 'occasionally_available' if 50 < days < 200 else 'highly_available'
)
print_analysis_results(df['availability_status'], 'Availability Status column:')

print_analysis_results(df['availability_status'].value_counts(), "Distribution by category:")
print_analysis_results(df.groupby('availability_status')['price'].mean(), "Average price by availability status:")

pivot_table = df.pivot_table(
    values=['price', 'number_of_reviews'],
    index='neighbourhood_group',
    columns='availability_status',
    aggfunc='mean'
)
print_analysis_results(pivot_table, 'Pivot table showing average price and reviews by neighbourhood and availability status:')

print_analysis_results(df['price'].mean(), 'Mean of price:')
print_analysis_results(df['minimum_nights'].mean(), 'Mean of minimum_nights:')
print_analysis_results(df['number_of_reviews'].mean(), 'Mean of number_of_reviews:')

print_analysis_results(df['price'].median(), 'Median of price:')
print_analysis_results(df['minimum_nights'].median(), 'Median of minimum_nights:')
print_analysis_results(df['number_of_reviews'].median(), 'Median of number_of_reviews:')

print_analysis_results(df['price'].std(), "standard deviation of price:")
print_analysis_results(df['minimum_nights'].std(), "standard deviation of minimum_nights:")
print_analysis_results(df['number_of_reviews'].std(), "standard deviation of number_of_reviews:")

print(df['last_review'])
df['last_review'] = pd.to_datetime(df['last_review'], errors='ignore')
print(df['last_review'].isna().sum())
df.set_index(df['last_review'], inplace=True)
print_analysis_results(df.sample(20), "DataFrame with 'last_review' as index:")

monthly_trends = df.resample('M').agg({
    'price':'mean',
    'number_of_reviews':'sum'
})
print_analysis_results(monthly_trends, "Monthly trends in prices and number of reviews:")

df['month'] = df['last_review'].dt.month
seasonal_patterns = df.groupby(['month']).agg({
    'price':'mean',
    'number_of_reviews':'mean',
    'availability_365':'mean'
})
print_analysis_results(seasonal_patterns, "seasonal patterns:")

df.to_csv("time_series_airbnb_data.csv", index=False)
print("The cleaned dataset has been saved as 'time_series_airbnb_data.csv'.")

