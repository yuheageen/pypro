import math

L = input("얼마빌림?")
ia = input("이자율")
n = input("몇달빌림")
i = (int(ia)/100)
i1 = (i+1)
for i1 in range(int(n)):
    ir= i1*i1
a = i*int(ir)*int(L)
b = ir-1
M = a/b
print("답:",M,"이다")