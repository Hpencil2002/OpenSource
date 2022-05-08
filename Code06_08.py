## 전역 변수 선언 ##
i, k, guguLine = 0, 0, ""

## 메인 코드 ##
for i in range(2, 10):
    guguLine += (" #  %d단  #" %i)

print(guguLine)

for i in range(1, 10):
    guguLine = ""
    for k in range(2, 10):
        guguLine += str("%2dX %2d= %2d" %(k, i, k*i))
    print(guguLine)
