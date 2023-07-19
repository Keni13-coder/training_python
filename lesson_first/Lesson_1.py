# from math import ceil
# x = int(input("Введите число 1: "))
# y = int(input("Введите число 2: ")) 

# print("Больше 1 чсило" if eval(f'{x}>{y}') else "Больше 2 число" if eval(f'{x}<{y}') else "2 Числа равны" )


# n = int(input())
# m = int(input())
# s = (m + n - 1) // n
# print(s)


# True = 1
# False = 0

# n = int(input("Введите число 1: "))
# m = int(input("Введите число 2: "))
# print(ceil(eval(f'{m}/{n}')))

# a,b,c = int(input('Введите количество учеников 1 класса: '))/2 ,int(input('Введите количество учеников 2 класса: '))/2,int(input('Введите количество учеников 3 класса: '))/2
# print(a+(a % 2 > 0),b+(b % 2 > 0),c+(c % 2 > 0))
# # print( (a1+1)//2 + (b2+1)//2 + (c3+1)//2) решение от преподователя


i = 3
j = 4

print("Недостаточно информации"  if i == j else i+j-1)

x = int(input("Введите год: "))
print("Yes" if x % 4 ==0 or x % 400 ==0 and x % 100 != 0 else 'No' )