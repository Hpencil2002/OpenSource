t = 5
a = ['22220228', '20150002', '01010101', '20140230', '11111111']
b = [' '] * 5

for i in  range(0, 5):
    if (int(a[i][4:6]) < 1 or int(a[i][4:6]) > 12):
        b[i] = '-1'
    else:
        if (int(a[i][4:6]) == 1 or int(a[i][4:6]) == 3 or int(a[i][4:6]) == 5 or int(a[i][4:6]) == 7 or int(a[i][4:6]) == 8 or int(a[i][4:6]) == 10 or int(a[i][4:6]) == 12):
            if (int(a[i][6:]) >= 1 and int(a[i][6:]) <= 31):
                b[i] = a[i][0:4] + '/' + a[i][4:6] + '/' + a[i][6:]
            else:
                b[i] = '-1'
                
        elif (int(a[i][4:6]) == 2):
            if (int(a[i][6:]) >= 1 and int(a[i][6:]) <= 28):
                b[i] = a[i][0:4] + '/' + a[i][4:6] + '/' + a[i][6:]
            else:
                b[i] = '-1'
                
        elif (int(a[i][4:6]) == 4 or int(a[i][4:6]) == 6 or int(a[i][4:6]) == 9 or int(a[i][4:6]) == 11):
            if (int(a[i][6:]) >= 1 and int(a[i][6:]) <= 30):
                b[i] = a[i][0:4] + '/' + a[i][4:6] + '/' + a[i][6:]
            else:
                b[i] = '-1'
                
    print("%d] %s" %(i + 1, b[i]))
