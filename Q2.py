t = 10
a = [9, 15, 54, 369, 634, 1053, 2954, 4234, 5424, 9531]
b = []

for i in range(0, t):
    b.append(0)

for i in range(0, t):
    j = 1
    while (j <= a[i]):
        b[i] += j
        j += 1
    print("%d] %d" %(i+1, b[i]))
