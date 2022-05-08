t = 10
a = [9, 15, 54, 369, 634, 1053, 2954, 4234, 5424, 9531]
b = [2, 6, 6, 15, 20, 34, 50, 89, 123, 9999]
count = 1
quote = [0] * 10

for i in range(0, t):
    if (a[i] > b[i]):
        for count in range(1, a[i]+1):
            if (a[i] % count == 0 and b[i] % count == 0):
                quote[i] = count
    elif (a[i] < b[i]):
        for count in range(1, b[i]+1):
            if (a[i] % count == 0 and b[i] % count == 0):
                quote[i] = count
    print("%d] %d" %(i + 1, quote[i]))
