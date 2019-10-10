#==========================================================================
# PROGRAM PURPOSE:... Ch4 P7
# AUTHOR:............ Thompson, Nick
# COURSE:............ CSC 131-004
# TERM:.............. Fall 2017
# COLLABORATION:..... 
# WORK TIME(h:mm):... 3:00
#==========================================================================
# inputs
while True:
    while True:
        print("Please enter any amount of integer values\n\
for List One separated by a space (e.g. 1 2 3)\n\
If you do not wish to input any values, press return.")
            
        try:
            # loops through each element and converts str to list
            list_one = [int(x) for x in input().split()]                
        except ValueError:
            print("Sorry, I didn't understand that.")
        else:
            break
        
    while True:
        print("Please enter any amount of integer values\n\
for List Two separated by a space (e.g. 3 4 5 6)\n\
If you do not wish to input any values, press return.")

        try:
             # loops through each element and convers str to list
            list_two = [int(y) for y in input().split()]
        except ValueError:
            print("Sorry, I didn't understand that.")
        else:
            break
        
    # init
    list_overlap = set(list_one).intersection(list_two)

    # program start

    if len(list_one) == len(list_two):
        print("List One and List Two contain the same amount of elements.")
    elif len(list_one) > len(list_two):
        print("List One contains",len(list_one) - len(list_two), "more element(s) than List Two.")
    elif len(list_one) <
    len(list_two):
        print("List One contains",len(list_two) - len(list_one), "fewer element(s) than List Two.")

    print("The sum of all elements in List One is:",sum(list_one),)

    print("The sum of all elements in List Two is:",sum(list_two),)

    if sum(list_one) == sum(list_two):
        print("The sum of List One and List Two equal the same value which is:", sum(list_one))
    elif sum(list_one) != sum(list_two):
        print("The sum of List One and List Two do not equal the same value.")

    print("The sum of all elements in List One and List Two is:",sum(list_one) + sum(list_two),)

    if len(list_overlap) > 0:
      print("The elements that appear in both lists are: {}".format(list_overlap))
    else:
      print("The lists contain none of the same elements.")

    print("-------------------------------------------------------------------------------")

# original solution was:
    # while True:
        # while True:
            # try:
                # list_one = []
                # list_one_input = input("Please enter any amount of integer values\n\
    # for List One separated by a space (e.g. 1 2 3): ")
                # for x in list_one_input.split():
                    # list_one.append(int(x))
                # while list_one_input == "":       # this line was to prevent users from entering nothing. I decided against this because even if the user inputs 0,
                                                    # they would still have entered an element. Because of this, allowing a user input of "" seems fine.

                    # list_one_input = input("Sorry! Your input can't be nothing!\n\
    # Please enter any amount of integer values\n\
    # for List One separated by a space (e.g. 1 2 3): ")
        # while True:
            # same as list one, but with different variables.

# solution worked, but was too unorganized.
# I feel like this could have been done better using a function, but because I used one on the last assignment I decided against it.
# I used set(list_one) & set(list_two), but I wanted to further dive down list comprehensions
