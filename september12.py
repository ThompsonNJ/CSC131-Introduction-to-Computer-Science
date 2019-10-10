LC1 = [x*2 for x in (1,2,3)]
LC2 = [x**2 for x in [1,2,3]]
len(LC1) == len(LC2)
even_sq = []
for x in range(1,11):
    if x % 2 == 0:
        even_sq.append(x*x)

    #even_sq = [x*x for x in range (1,11) if x % 2 == 0]
        
