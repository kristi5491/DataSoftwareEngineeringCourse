import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

df = pd.read_csv("/Users/admin/Desktop/DataSoftwareEngineeringCourse/cleaned_airbnb_data.csv")

neighbourhood_counts = df['neighbourhood_group'].value_counts().reset_index()
neighbourhood_counts.columns = ['neighbourhood_group', 'count']
new_barplot = sns.barplot(x='neighbourhood_group', y='count', data=neighbourhood_counts, palette='viridis', width=0.4)
new_barplot.set_xlabel('Neighbourhood Group')
new_barplot.set_ylabel('Number of Listings')
new_barplot.set_title('Distribution of Listings across Different Neighbourhood Groups')
plt.figure() 


new_boxplot = sns.boxplot(x='neighbourhood_group', y='price', data=df, palette='viridis', width = 0.4)
new_boxplot.set_xlabel('Neighbourhood Group')
new_boxplot.set_ylabel('Price')
new_boxplot.set_title('Distribution of Price within Each Neighbourhood Group')
plt.figure() 


avg_availability = df.groupby(['neighbourhood_group', 'room_type'])['availability_365'].mean().reset_index()
avg_avalib = sns.barplot(x='room_type', y='availability_365',hue='room_type', data=avg_availability,palette='viridis', width = 0.4)
avg_avalib.set_xlabel('Neighbourhood Group')
avg_avalib.set_ylabel('Average Availability (365 days)')
avg_avalib.set_title('Average Availability for Each Room Type Across Neighbourhood Groups')
plt.figure() 


for room_type in df['room_type'].unique():
    subset = df[df['room_type'] == room_type]
    plt.scatter(subset['price'], subset['number_of_reviews'], label=room_type)

sns.regplot(x='price', y='number_of_reviews', data=df, scatter=False, color='black')
plt.title('Correlation Between Price and Number of Reviews by Room Type')
plt.xlabel('Price')
plt.ylabel('Number of Reviews')


grouped_reviews = df.groupby(['neighbourhood_group', 'last_review'])['number_of_reviews'].sum().reset_index()
plt.figure(figsize=(10, 6))
for group, subset in grouped_reviews.groupby('neighbourhood_group'):
    subset['rolling_avg'] = subset['number_of_reviews'].rolling(window=7, min_periods=1).mean()
    plt.plot(subset['last_review'], subset['rolling_avg'], label=group)

plt.gca().xaxis.set_major_locator(mdates.MonthLocator())  # Set the interval for the date labels
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.title('Trend of Number of Reviews Over Time by Neighbourhood Group')
plt.xlabel('Date of Last Review')
plt.ylabel('Number of Reviews (Rolling Average)')
plt.legend(title='Neighbourhood Group')
plt.grid(True)
plt.xticks(rotation=45)  
plt.gca().xaxis.set_visible(False)
plt.tight_layout()

neighborhood_data = df.groupby('neighbourhood').agg(
    mean_price=('price', 'mean'),
    mean_availability=('availability_365', 'mean')
).reset_index()

# Create a heatmap using seaborn
plt.figure(figsize=(12, 8))
pivot_table = neighborhood_data.pivot(index='neighbourhood', columns='mean_price', values='mean_availability')
sns.heatmap(pivot_table, cmap='coolwarm', annot=True, fmt='.1f', linewidths=.5)

# Set labels and title
plt.xlabel('Mean Price')
plt.ylabel('Neighborhood')
plt.title('Price vs Availability Heatmap by Neighborhood')


review_counts = df.groupby(['neighbourhood_group', 'room_type'])['number_of_reviews'].sum().unstack()
review_counts.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='viridis')
plt.title('Number of Reviews for Each Room Type Across Neighbourhood Groups')
plt.xlabel('Neighbourhood Group')
plt.ylabel('Number of Reviews')
plt.legend(title='Room Type')
plt.grid(axis='y')








plt.show()

