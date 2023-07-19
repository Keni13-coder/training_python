'''
Задание 8
'''

def test(N):
    return [print('_' * (N-i) + '*' * (i+i+1)+ '_' * (N-i)) if i % 2 != 0 else print('_' * (N-i) + 'o' * (i+i+1)+ '_' * (N-i))  for i in range(N)]

# test(10)
'Задача 5'
def t_2(n,e):
    return sum(x for x in range(0,n,2) if x % e != 0)


# print(t_2(100,4))

'Задача 7'
# def t_3(n=input("Введите число от 1 до 999: ")):
    # A = 10
    # B = 100
    # while not n.isdigit() or int(n) > 999:
    #     n = input("Введите число от 1 до 999: ")      
    # n = int(n)
    # match n:
    #     case z if z < A:
    #         return (z**2)
    #     case z if z >= B:
    #         def dd(i):
    #             return i if i < A else str('' if (d := i % A) == 0 else d) + str(dd(i // A))
    #         return dd(z)
    #     case z if z > A <B:
    #         return (z+(z % A))

    
# print(t_3())

'задача 6'
def t_4(n):
    x = 4
    z = 100
    return 'Обычный' if n % x != 0 or n % z == 0 and n % (z*x) != 0 else 'Високосный'


# print(t_4(2100))

'задача 9'
def t_5():
    x = 10
    lis = [[f'{i} * {j} = {i*j}' for j in range(2,x+1)] for i in range(2,x)]
    [print(x) for x in zip(lis[0],lis[1],lis[2],lis[3])]
    print()
    [print(x) for x in zip(lis[4],lis[5],lis[6],lis[7])]

# t_5()