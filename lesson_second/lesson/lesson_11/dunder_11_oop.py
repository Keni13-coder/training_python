'__str__ - для пользователя при принте или str'
'__repr__ - строка для создание экземпляра при копировании её кода, например вывод:  User(*args,**kwargs)'
'если есть __str__ и __repr__ чтобы получить 2 надо repr(), f"{user= }", или списком классов [user]'
'__add__ - сложенИе self + value'
'__radd__ - сложение value + self'
"сложение классов __add__(self othen) - self.(*args) + othen(*args)"

print(help(int))
print(int())