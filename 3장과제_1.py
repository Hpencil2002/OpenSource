## 2021041035 조민규
import sys

intVar = 0
floatVar = 0.0
boolVar = True
strVar = ''
listVar = []
tupleVar = ()
dicVar = {}
setVar = set()

print('int형 기본 크기 --> ', sys.getsizeof(intVar))
print('float형 기본 크기 --> ', sys.getsizeof(floatVar))
print('bool형 기본 크기 --> ', sys.getsizeof(boolVar))
print('str형 기본 크기 --> ', sys.getsizeof(strVar))
print('list형 기본 크기 --> ', sys.getsizeof(listVar))
print('tuple형 기본 크기 --> ', sys.getsizeof(tupleVar))
print('dictionary형 기본 크기 --> ', sys.getsizeof(dicVar))
print('set형 기본 크기 --> ', sys.getsizeof(setVar))
