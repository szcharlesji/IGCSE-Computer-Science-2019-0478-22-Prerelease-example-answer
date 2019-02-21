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
