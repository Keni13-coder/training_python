'''
Выведите в консоль таблицу умножения 
от 2х2 до 9х10 как на школьной тетрадке. 
✔ Таблицу создайте в виде однострочного 
генератора, где каждый элемент генератора — 
отдельный пример таблицы умножения. 
✔ Для вывода результата используйте «принт» 
без перехода на новую строку.

'''
def t_5():
    MAX_RANGE = 10
    gener=([f'{i:>2} * {j} = {i*j:>2}' for j in range(2,MAX_RANGE)] for i in range(2,MAX_RANGE) )
    return gener
            

t_5()

for j,z in enumerate(zip(*list(t_5())[:4]),1):
        for i,x in enumerate(z,1):
            if i % 4 != 0:
                    print(f'{x}\t',end='')
            else:
                print(x)
print()               
for j,z in enumerate(zip(*list(t_5())[4:]),1):
        for i,x in enumerate(z,1):
            if i % 4!= 0:
                    print(f'{x}\t',end='')
            else:
                print(x)                    