##time = 9635458
##count = 0
##
##for i in range(1, time):
##    if i % 2 == 0:
##        time = time / 2
##        count += 1       
##
##print("It would take {:,} years using Moore's law".format(count))
##time = 9635458
##time = time / 2
##print(time)

time = 9635458
count = 0

while count < time:
    time = time / 2
    print(time)
    count += 2
    print(count)

print("It would take {:,} years using Moore's law".format(count))
