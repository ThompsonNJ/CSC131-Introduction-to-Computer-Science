#==========================================================================
# PROGRAM PURPOSE:... Ch3 M7
# AUTHOR:............ Thompson, Nick
# COURSE:............ CSC 131-004
# TERM:.............. Fall 2017
# COLLABORATION:..... Prof. Stoker; Stackover helped with "def m(cents)"
# WORK TIME(h:mm):... 10:15
#==========================================================================
# imports
import random

# program welcome
print("The purpose of this exercise is to enter the least number of coin values")

print("that add up to a displayed target value. \n")

print("Enter coins values as 1-penny, 5-nickel, 10-dime, and 25- quarter.")

print("Hit return after the last entered coin value.")

print("-------------------")

# def
def m(cents):
    if cents in d.keys():
        return d[cents]
    elif cents > 0:
        choices = [(m(cents - x)[0] + 1, m(cents - x)[1] + [x]) for x in coins if cents >= x]
        d[cents] = min(choices)
        return d[cents]
    else:
         d[0] = (0, [])
         return d[0]
        
# init
terminate =  False
empty_str = ""
coins = [1, 5, 10, 25]
d = {}
coin_count = 0


# start game
while not terminate:
    amount = random.randint(1,99)
    val = m(amount)
    print("Enter coins that add up to", amount, "cents, one per line.\n")
    game_over = False
    total = 0
    
    while not game_over:
        valid_entry = False
             
        while not valid_entry:
            if total == 0:
                entry = input("Enter first coin: ")
            else:
                entry = input("Enter next coin: ")

            if entry in ("1", "5", "10", "25"):
                valid_entry = True
                coin_count += 1
            elif entry == empty_str:
                valid_entry = True
            else:
                print("Invalid entry")
        
        # improvment to original code
        if entry == empty_str:
            if total == amount and coin_count == val[0]:
                print("Correct!")
                game_over = True
                
            elif total == amount and coin_count != val[0]:
                print("Sorry! you entered the correct amount, but used too many coins!")
                print (amount, "cents requires", val[0], "coins:", val[1])
                game_over = True

            else:
                print("Sorry - you only entered", total, "cents")
                print (amount, "cents requires", val[0], "coins:", val[1])
                game_over = True

        else:
            total = total + int(entry)
            if total > amount:
                print("Sorry - total amount exceeds", amount, "cents.")
                print (amount, "cents requires", val[0], "coins:", val[1])
                game_over = True


    # improvement to original code       
    entry = input("\nTry again (y/n)?: ")
    coin_count = 0

    if entry == "n":
        terminate = True

print("Thanks for playing! Goodbye!")
