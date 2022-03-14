a=int(input('Введите количество минут:'))
day=1440
if a>day:
    print ('ОШИБКА. Максимальное количество минут в сутках - 1440. Введите корректные данные')
else:
    hours=a//60
    minutes=a%60
if hours==24:
    hours=0
print (hours, minutes)
