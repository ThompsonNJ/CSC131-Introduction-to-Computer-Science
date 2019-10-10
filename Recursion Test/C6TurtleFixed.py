time = 9635458
count = 0
print(time)

#while True:
for i in range (1, time):
    if i % 2 == 0:
        time = time / 2
        count += 1

print(count)
