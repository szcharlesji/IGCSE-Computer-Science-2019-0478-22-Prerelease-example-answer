# Task 1
item_identifier_list = []
item_price_list = []
item_name_list = []
item_description_list = []

number_of_items = int(input("Please enter how many items you need."))

for i in range(number_of_items):
    while True:
        item_identifier = int(input("Please enter an unique number for the current item."))
        if item_identifier in item_identifier_list:
            print("Please enter an unique item number")
            continue
        else:
            break
    item_identifier_list.append(item_identifier)
    price_of_items = int(input("Please enter the reserve price for each item"))
    item_price_list.append(price_of_items)
    item_name = str(input("Please enter name for it"))
    item_name_list.append(item_name)
    item_description = str(input("Please enter the item description."))
    item_description_list.append(item_description)


# Task 2
total_bid_info = []
item_being_sold_list = []
item_identifier_sold = []
buyer_won_bid_list = []
item_not_sold = []


for i in range(number_of_items):
    being_sold = False
    print("Item number:", item_identifier_list[i])
    print("Reserve Price:", item_price_list[i])
    print("Name:", item_name_list[i])
    print("Description:", item_description_list[i])


    bid_info = []

    current_item_price = 0

    continue_or_not = True
    while continue_or_not:
        bid = input("Please enter how much you would like to offer for the item you want to buy")
        if str(bid) == "skip":
            continue_or_not = False
            if len(bid_info) != 0:
                buyer_won_bid_list.append(input("Enter the buyer number with the highest bid."))
                being_sold = True
        elif int(bid) <= int(current_item_price):
            print("That is less than the current price")
        else:
            current_item_price = bid
            bid_info.append(current_item_price)


    if len(bid_info) == 0:
        print("No bids")
    else:
        if current_item_price >= item_price_list[i]:
            total_bid_info.append(bid_info)
            item_being_sold_list.append(item_name_list[i])
            item_identifier_sold.append(i)

    if not being_sold:
        item_not_sold.append(item_name_list[i])


print("\nNumber of item has bid on:", len(total_bid_info))
print("They are:", item_being_sold_list)

# Task 3

for i in total_bid_info:
    highest_bid = i[-1]
    fee = int(highest_bid) / 10

    print("\nHighest bid for ", item_being_sold_list[total_bid_info.index(i)], " is ", highest_bid)
    print("The fee is ", fee)
print("These items are sold.\n")


for i in item_not_sold:
    print(i, "has not been sold.")
