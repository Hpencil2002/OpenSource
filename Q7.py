t = 2
a = ['Open source is source code that is made freely available for possible modification and redistribution.', 'Code is released under the terms of a software license.']
aLen1 = len(a[0])
aLen2 = len(a[1])
b = [' '] * 2
Str = ''

for i in range(0, aLen1):
    Str = a[0][aLen1 - (i + 1)]
    b[0] += Str

for i in range(0, aLen2):
    Str = a[1][aLen2 - (i + 1)]
    b[1] += Str

for i in range(0 ,t):
    print("%d]%s" %(i + 1, b[i]))
