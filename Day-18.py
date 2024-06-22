##Bitwise operators in python
#There are 6 bitwise ipwerators namely and,or,xor,not,leftshift,rightshift
#The operation of bitwise operators are not same as logical operators
#And
# a=22
# b=13
# res=a & b
# res1=a / b
# res2=a ^ b
# res3=a << b
# res4=a >> b
# res5=~a
# print(res)
# print(res1)
# print(res2)
# print(res3)
# print(res4)
# print(res5)



number = 12  
mask = 11

result = number & ~mask
print(bin(result))
