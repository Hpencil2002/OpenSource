inFp = None
inStr = ''

inFp = open('C:/Temp/data1.txt', 'r', encoding = 'UTF8')
num = 1

while True:
    inStr = inFp.readline()
    if inStr == '':
        break;
    print('%d: %s' %(num, inStr), end='')
    num += 1

inFp.close()
