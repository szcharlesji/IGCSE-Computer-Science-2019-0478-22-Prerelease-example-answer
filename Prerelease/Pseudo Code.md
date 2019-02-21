```pseudocode
# Task1

n <- 0
DECLARE item_no : ARRAY[1:n] OF INTEGER
DECLARE description : ARRAY[1:n] OF STRING
DECLARE reserve_price : ARRAY[1:n] OF REAL
DECLARE num_of_bids : ARRAY[1:n] OF INTEGER

WHILE n < 10:
    OUTPUT "There should be at least 10 items"
    OUTPUT "How many items are there?"
    INPUT n
ENDWHILE

FOR i <- 1 TO n DO
    OUTPUT "Input the data for item", i + 1
    OUTPUT " ItemNo of item ="
	INPUT ItemNo
    item_no[i] <- ItemNo
    
    FOR j <- 1 TO i DO
        WHILE item_no[i] = item_no[j]:
            OUTPUT "The item number must be unique ! Input again"
            INPUT ItemNo
            item_no[i] <- ItemNo
            j <- 0
        ENDWHILE
    NEXT
	
	OUTPUT "Description of item ="
	INPUT description_of_item
	description[i] <- description_of_item
	OUTPUT "Reverse price of item ="
	INPUT reserve_price_of_item
	reserve_price[i] <- reserve_price_of_item
NEXT
    
# Task 2

DECLARE highest_bids : ARRAY[1:n] OF INTEGER
DECLARE buyer_code : ARRAY[1:n] OF INTEGER
search_code <- 0
current_buyer_code <- 0
new_bid <- 0
choice <- False

WHILE TRUE:
	OUTPUT "Enter the itemNo (-1 To Exit) ="
	INPUT search_code
	
    IF search_code = -1 THEN
        BREAK
    ENDIF
    FOR i <- 1 TO n DO:
        IF item_no[i] = search_code DO
            OUTPUT "Item number : ", item_no[i]
            OUTPUT "Description : ", description[i]
            OUTPUT "Current Highest Bid : ", highest_bids[i]
            OUTPUT "The buyer : ", buyer_code[i]
            OUTPUT "Would you like to bid for this item? Y/N ="
            INPUT choice
            
            IF choice = "y" DO
            	OUTPUT "Please enter your buyer code <- "
            	INPUT current_buyer_code
                OUTPUT "The Highest Bid Now Is <- ", highest_bids[i]
                OUTPUT "Please Enter Your Bid ="
                OUTPUT new_bid
                IF new_bid > highest_bids[i] DO
                    highest_bids[i] <- new_bid
                    num_of_bids[i] <- num_of_bids[i] + 1
                    buyer_code[i] <- current_buyer_code
                    OUTPUT "Success!!!"
                ELSE DO
                    OUTPUT "Your Bid Is not Accepted!!!"
                ENDIF
            ELSEIF choice = "n":
                OUTPUT "You've chosen not to bid for it"
        	ENDIF
        ENDIF
    NEXT
ENDWHILE

# Task 3

DECLARE item_sold : ARRAY[1:n] OF BOOLEAN
DECLARE display : ARRAY[1:4n]
DECLARE display_no_bids : ARRAY[1:2n]

counter_no_bids <- 0
counter_not_meet_reserve_price <- 0
counter <- 0
income <- 0
fee <- 0.0

FOR i <- 1 TO n DO
    IF highest_bids[i] >= reserve_price[i] DO
        item_sold[i] <- True
        income <- income + highest_bids[i]
        counter <- counter + 1
    ELSE DO
        item_sold[i] <- False
        display[i] <- "Item number ="
        display[i] <- item_no[i]
        display[i] <- "Final bid ="
		display[i] <- highest_bids[i]
        counter_not_meet_reserve_price <- counter_not_meet_reserve_price + 1
    ENDIF
    IF num_of_bids[i] = 0 DO
    	display_no_bids[i] <- "Item number ="
        display_no_bids[i] <- item_no[i]
        counter_no_bids <- counter_no_bids + 1
    ENDIF
ENDFOR

fee <- income * 0.1 + income
OUTPUT "Total Fee <- ", fee
OUTPUT "Item Not Sold", display
OUTPUT "Item received NO Bids", display_no_bids
OUTPUT "Number of Item Sold", counter
OUTPUT "Number of items that did not meet the reserve price", counter_not_meet_reserve_price
OUTPUT "Number of items with NO Bids", counter_no_bids
```