number_of_items = int(input("How many items are in the auction? "))

while number_of_items < 10:
    print('There must be a minimum of 10 items in the auction.\nPlease enter another number.')
    number_of_items = int(input("How many items are in the auction? "))

item_number = [0] * number_of_items
item_list = [''] * number_of_items
description_list = [''] * number_of_items
reserve_price_list = [0] * number_of_items
number_of_bids = [0] * number_of_items

for i in range(number_of_items):
    item_number[i] = i
    item_list[i] = input('Please enter an item: ')
    description_list[i] = input('Please enter a description: ')
    reserve_price_list[i] = int(input('Please enter a reserve price: '))

# test code
print(item_list, len(item_list))
print(item_number, len(item_number))
print(description_list, len(description_list))
print(reserve_price_list, len(reserve_price_list))
print(number_of_bids, len(number_of_bids))

