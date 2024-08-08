import numpy as np
import datetime


transactions = [
    [1, 101, 2001, 2, 19.99, datetime.datetime(2023, 7, 1, 14, 30).timestamp()],
    [2, 101, 2002, 1, 9.99, datetime.datetime(2023, 7, 1, 15, 0).timestamp()],
    [3, 103, 2003, 3, 29.99, datetime.datetime(2023, 7, 2, 16, 0).timestamp()],
    [4, 104, 2004, 1, 49.99, datetime.datetime(2023, 7, 2, 17, 30).timestamp()],
    [5, 105, 2005, 2, 19.99, datetime.datetime(2023, 7, 3, 12, 30).timestamp()],
    [6, 106, 2006, 5, 99.99, datetime.datetime(2023, 7, 3, 13, 45).timestamp()],
    [7, 107, 2007, 1, 14.99, datetime.datetime(2023, 7, 4, 11, 0).timestamp()],
    [8, 108, 2008, 4, 39.99, datetime.datetime(2023, 7, 4, 14, 15).timestamp()],
    [9, 109, 2009, 3, 29.99, datetime.datetime(2023, 7, 5, 9, 0).timestamp()],
    [10, 110, 2010, 0, 24.99, datetime.datetime(2023, 7, 5, 10, 30).timestamp()],
]

transactions_array = np.array(transactions, dtype=object)

def print_array(array, message=''):
    if message:
        print(message)
    print(array)


def total_revenue(transaction):
    quantity  = transaction[:, 3]
    price = transaction[:, 4]
    return np.sum(quantity * price)

print_array(total_revenue(transactions_array), 'Total revenue:')

def unique_users(transaction):
    users = np.unique(transaction[:, 1])
    return users

print_array(unique_users(transactions_array),'Unique users:')

def most_purchased_prod(transaction):
    most_product_quantity = np.max(transaction[:, 3])
    ptoduct_id = transaction[most_product_quantity, 2]
    return ptoduct_id



print_array(most_purchased_prod(transactions_array), 'Most purchased product:')

def convert_price_to_int(transaction):
    transaction[:, 4] = transaction[:, 4].astype(int)
    return transaction

def check_data_types(transaction):
    data_types = [col.dtype for col in transaction.T]
    return data_types

new_transactions_array = convert_price_to_int(transactions_array)
print_array(check_data_types(new_transactions_array),'Data Types:')

def product_quantity_array(transaction):
    product_quantity = transaction[:, [2, 3]]
    return product_quantity

print_array(product_quantity_array(transactions_array), 'Product and Quantity array:')

def transaction_count(transaction):
    user_ids = transaction[:, 1]
    unique_users, counts = np.unique(user_ids, return_counts=True)
    user_transaction_counts = np.column_stack((unique_users, counts))
    return user_transaction_counts


transaction_counts = transaction_count(transactions_array)
print_array(transaction_count(transactions_array), 'User transaction counts:')

def masked_array(transaction):
    quantity = transaction[:, 3]
    mask = quantity > 0
    filtered_transactions = transaction[mask]
    return filtered_transactions

print_array(masked_array(transactions_array), 'Array without zero quantity:')

def increase_price(transaction):
    increased_prices = transaction.copy()  
    increased_prices[:, 4] *= 1.05
    return increased_prices

increased_prices = increase_price(transactions_array)
print_array(increased_prices, 'Price increased by 5%')

def filter_transactions(transaction):
    quantity = transaction[:, 3]
    mask = quantity > 1
    filtered_transactions = transaction[mask]
    return filtered_transactions

print_array(filter_transactions(transactions_array), 'Array with quantity > 1:')

def revenue_comparison(transaction, start_date1, end_date1, start_date2, end_date2):
    period1_transactions = transaction[(transaction[:, 5] >= start_date1) & (transaction[:, 5] <= end_date1)]
    period1_revenue = total_revenue(period1_transactions)

    period2_transactions = transaction[(transaction[:, 5] >= start_date2) & (transaction[:, 5] <= end_date2)]
    period2_revenue = total_revenue(period2_transactions)

    print(f"Revenue for Period 1 (from {start_date1} to {end_date1}): ${period1_revenue:.2f}")
    print(f"Revenue for Period 2 (from {start_date2} to {end_date2}): ${period2_revenue:.2f}")

    if period1_revenue > period2_revenue:
        print("Period 1 generated more revenue.")
    elif period1_revenue < period2_revenue:
        print("Period 2 generated more revenue.")
    else:
        print("Both periods generated the same revenue.")

    return period1_revenue, period2_revenue

period1_start = datetime.datetime(2023, 7, 1).timestamp()
period1_end = datetime.datetime(2023, 7, 3, 23, 59, 59).timestamp() 
period2_start = datetime.datetime(2023, 7, 4).timestamp()  
period2_end = datetime.datetime(2023, 7, 5, 23, 59, 59).timestamp() 

compare_rev= revenue_comparison(transactions_array, period1_start, period1_end, period2_start, period2_end)

def user_transactions(transaction, specific_user):
    user_transaction = transaction[transaction[:, 1] == specific_user]
    return user_transaction

print_array(user_transactions(transactions_array, 101), 'All transactions of user 101: ')

def specific_data_range(transaction, start_date, end_date):
    period_transactions = transaction[(transaction[:, 5] >= start_date) & (transaction[:, 5] <= end_date)]
    return period_transactions

spec_data_rang = specific_data_range(transactions_array, period2_start,period2_end)
print_array(spec_data_rang, f'All transactions from(from {period2_start} to {period2_end}):')

