a = []
    
for i in range(1, 101):
    if (i == 2 or i % 2 != 0):
        if (i == 3 or i % 3 != 0):
            if (i == 5 or i % 5 != 0):
                if (i == 7 or i % 7 != 0):
                    a.append(i)
                            
alen = len(a)
for i in range(1, alen):
    print("%d " %a[i], end = '')
