class Bank:
    LIST = ('50','100','150','500','1000','5000','Другое','Выход')
    TAX = 10
    
    def __init__(self) -> None:
        
        self.summa = 0
        self.percent = 1.5
        self.count = 0
        self._operation = {}
        
        
    def choice(self)->str:
        print('Доступные методы\n'
                '1: Пополнить: account_replenishment\n'
                '2: Снять : account_withdrawal\n')

        return 'Удачи'
    
            
    def account_replenishment(self)->None|str: # Пополнение счета
        print(f'Вашь баланс на данный момент состовляет {self.summa}')
        if self.summa > 5_000_000:
            self.percent = self.TAX 
        if self.count % 3 ==0:
            self.percent += 3
        print('Доступные варианты')
        [print(f'{v}',end='   ') if i != 2 and i != len(self.LIST)-1 else print(f'{v}')  for i,v in enumerate(self.LIST)]
        replenish = input('Введите число для пополнение: ').strip()
        while replenish not in self.LIST:
            print('Доступные варианты')
            [print(f'{v}',end='   ') if i != 2 and i != len(self.LIST)-1 else print(f'{v}')  for i,v in enumerate(self.LIST)]
            replenish = input('Введите число для пополнение: ').strip()
        if replenish.isdigit():
            if replenish in self.LIST:
                self.summa += int(replenish)
                print(f'Вашь баланс на данный момент состовляет {self.summa}')
                self.count += 1
                self._operation.setdefault('Пополнение',[]).append(replenish)
            else:
                print('Данное число не найдено')     
        elif replenish == 'Другое':
            try:
                replenish = int(input("Введите другое число для пополнение: ").strip())
                self.summa += int(replenish)
                self._operation.setdefault('Пополнение',[]).append(replenish)
                self.count += 1
                print(f'Вашь баланс на данный момент состовляет {self.summa}')
            except  ValueError:
                print('Был введён не коректый символ\nЗавершение программы...')
        elif replenish == 'Выход':
            return 'Завершение работы'
                    
                    
                    
    def account_withdrawal(self)->None|str: # Снятие денег
        print(f'Вашь баланс на данный момент состовляет {self.summa}')
        if self.summa > 5_000_000:
            self.percent = self.TAX 
        if self.count % 3 ==0:
            self.percent += 3
        print('Доступные варианты')
        [print(f'{v}',end='   ') if i != 2 and i != len(self.LIST)-1 else print(f'{v}')  for i,v in enumerate(self.LIST)]
        replenish = input('Введите число для снятие наличных: ').strip()
        while replenish not in self.LIST:
            print('Доступные варианты')
            [print(f'{v}',end='   ') if i != 2 and i != len(self.LIST)-1 else print(f'{v}')  for i,v in enumerate(self.LIST)]
            replenish = input('Введите число снятие наличных: ').strip()
        if replenish.isdigit():
            if replenish in self.LIST:
                if self.summa - int(replenish) < 0:
                    print("Не достаточно средств")
                else:
                    replenish = int(replenish)
                    self.summa -= replenish + (30 if (s := ((replenish / 100) * self.percent)) < 30 else 600 if s >600 else s)
                    self.summa = f'{self.summa:.2f}'
                    self.summa = float(self.summa)
                    self._operation.setdefault('Снятие',[]).append(replenish)
                    print(f'Вашь баланс на данный момент состовляет {self.summa}')
                    self.count += 1
            else:
                print('Данное число не найдено')     
        elif replenish == 'Другое':
            try:
                replenish = int(input("Введите другое число снятие наличных: ").strip())
                if self.summa - int(replenish) < 0:
                    print("Не достаточно средств")
                else:
                    replenish = int(replenish)
                    self.summa -= replenish + (30 if (s := ((replenish / 100) * self.percent)) < 30 else 600 if s >600 else s)
                    self.summa = f'{self.summa:.2f}'
                    self.summa = float(self.summa)
                    self._operation.setdefault('Снятие',[]).append(replenish)
                    self.count += 1
                    print(f'Вашь баланс на данный момент состовляет {self.summa}')
            except  ValueError:
                print('Был введён не коректый символ\nЗавершение программы...')
        elif replenish == 'Выход':
            return 'Завершение работы'
                            
        
    def get_operation(self):
        print(self._operation)
        return self._operation
    


if __name__ == '__main__':        
    test = Bank()
    test.choice()
    test.account_replenishment()
    test.account_replenishment()
    test.account_withdrawal()
    test.get_operation()