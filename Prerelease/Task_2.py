# arrays hard coded - refer to Task_1.py

item_list = ['Phone', 'Laptop', 'Car', 'Trainers', 'Guitar']
item_number = [0, 1, 2, 3, 4]
description_list = ['iPhone X 128Gb White', 'Microsoft Surface Pro', 'Porsche Carrera Turbo', 'Adidas UltraBoost', 'Gibson SG']
reserve_price_list = [1000, 1500, 45000, 120, 2700]
number_of_bids = [0, 0, 0, 0 ,0]
current_highest_bid = [0, 0, 0, 0 , 0]

buyer_list = []
no_of_buyers = int(input('How many buyers are at the auction? '))
for i in range(no_of_buyers):
    buyer_list.append(i)

auction = True
while auction == True:
    found = False
    while found == False:
        item = input('Please enter an item: ')
        for i in range(5): # should be number_of_items
            if item == item_list[i]:
                print('Item found')
                print('Item:', item_list[i])
                print('Item number:', item_number[i])
                print('Description:', description_list[i])
                print('Current highest bid:', current_highest_bid[i])
                found = True
                item_index = i
                break
        if found == False:
            print('Item is not in the auction!')

    buyer_valid = False
    while buyer_valid == False:
        buyer_number = int(input('Please enter your buyer number: '))
        for i in range(no_of_buyers):
            if buyer_number == i:
                buyer_valid = True
                break
        if buyer_valid == False:
            print('Invalid buyer number!')

    bid_valid = False
    while  bid_valid == False:
        bid = int(input('Please enter a bid: '))
        if bid > current_highest_bid[item_index]:
            print('Your bid is successful!')
            current_highest_bid[item_index] = bid
            number_of_bids[item_index] = number_of_bids[item_index] + 1
            bid_valid = True
        else:
            print('Your bid is too low!\nPlease bid again')

    answer = input('Would you like to continue bidding? y/n')
    if answer == 'n':
        auction = False
print('\nAuction ended!')

print('number_of_bids:', number_of_bids)
print('current_highest_bid:', current_highest_bid)






