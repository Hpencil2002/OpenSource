t = 2
a = ['Open source is source code that is made freely available for possible modification and redistribution.', 'Code is released under the terms of a software license.']

for i in range (0, t):
    a[i] = a[i].upper()
    print("%d] %s" %(i + 1, a[i]))
