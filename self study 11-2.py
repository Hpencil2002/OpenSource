inFp = None
inList, inStr = [], ''

inFp = open('C:/Temp/data1.txt', 'r', encoding = 'CP949')

inList = inFp.readlines()
i = 1
for inStr in inList:
    print("%d: %s" %(i, inStr), end = '')
    i += 1

inFp.close()
