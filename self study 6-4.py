## 전역 변수 선언 ##
i, k, guguLine = 0, 0, ""

## 메인 코드 ##
for i in range(9, 1, -1):
    guguLine += (" #  %d단  #" %i)

print(guguLine)

for i in range(9, 0, -1):
    guguLine = ""
    for k in range(9, 1, -1):
        guguLine += str("%2dX %2d= %2d" %(k, i, k*i))
    print(guguLine)
