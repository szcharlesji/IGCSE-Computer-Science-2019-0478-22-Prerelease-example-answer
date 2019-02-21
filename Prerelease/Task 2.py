# Task1
n = 0
item_no = [0] * n
description = [""] * n
reserve_price = [0] * n
num_of_bids = [0] * n

while n < 10:
    print("There should be at least 10 items")
    n = int(input("Number of items? ="))

for i in range(0, n):
    print("Input the data for item", i + 1)
    item_no[i] = int(input("ItemNo of item ="))

    for j in range(0, i):
        while item_no[i] == item_no[j]:
            print("The item number must be unique !")
            item_no[i] = int(input("ItemNo of item ="))
            j = 0
    description[i] = input("Description of item =")
    reserve_price[i] = int(input("Reverse price of item ="))

# Task 2

highest_bids = [0] * n
buyer_code = [0] * n
search_code = 0
current_buyer_code = 0
new_bid = 0
choice = False

while True:
    search_code = int(input("Enter the itemNo (-1 To Exit) ="))

    if search_code == -1:
        break

    for i in range(0, n):
        if item_no[i] == search_code:
            print("Item number : ", item_no[i])
            print("Description : ", description[i])
            print("Current Highest Bid : ", highest_bids[i])
            print("The buyer : ", buyer_code[i])
            choice = str(input("Would you like to bid for this item? Y/N ="))

            if choice.lower() == "y":
                current_buyer_code = int(input("Please enter your buyer code = "))
                print("The Highest Bid Now Is = ", highest_bids[i])
                new_bid = int(input("Please Enter Your Bid = "))

                if new_bid > highest_bids[i]:
                    highest_bids[i] = new_bid
                    num_of_bids[i] = num_of_bids[i] + 1
                    buyer_code[i] = current_buyer_code
                    print("Success!!!")
                else:
                    print("Your Bid Is not Accepted!!!")
            elif choice.lower() == "n":
                print("You've chosen not to bid for it")
