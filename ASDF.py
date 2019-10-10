# imports
import random

# program welcome
print("The purpose of this exercise is to enter the least number of coin values")

print("that add up to a displayed target value. \n")

print("Enter coins values as 1-penny, 5-nickel, 10-dime, and 25- quarter.")

print("Hit return after the last entered coin value.")

print("-------------------")

# init
terminate = False
empty_str = ""

# start game
while not terminate:
    amount = random.randint(1, 99)
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

            if entry in (empty_str, "1", "5", "10", "25"):
                valid_entry = True
            else:
                print("Invalid entry")

            # finds the minimum # of coins needed to
            coins = [1, 5, 10, 25]
            d = {}

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
                
            for x in range(1, 100):
                val = m(x)
                
            # improvment to original code
            if entry == empty_str:
                if total == amount:
                    print("Correct!")
                    game_over = True
                    if game_over:
                        entry = input("\nWould you like to play again (y/n)?: ")
    
                    if entry == "n":
                        terminate = True
            else:
                print("Sorry - you only entered", total, "cents")
                print(x, "cents requires", val[0], "coins:", val[1])
                game_over = True

        else:
            total = total + int(entry)
            if total > amount:
                print("Sorry - total amount exceeds", amount, "cents.")
                game_over = True

            if game_over:
                entry = input("\nTry again (y/n)?: ")

                if entry == "n":
                    terminate = True

print("Thanks for playing! Goodbye!")
