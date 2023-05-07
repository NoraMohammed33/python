#Q1

""""
 statment=input('enter statment')
vowels = ('a', 'e', 'i', 'o', 'u')
for x in statment:
    if x in vowels:
        statment=statment.replace(x,"")
print(statment);
"""
#Q2


num=int(input('enter num'))
for i in range(1, num + 1):
    print(" " * (num - i) + "*" * i);