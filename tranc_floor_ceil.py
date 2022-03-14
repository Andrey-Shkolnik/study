import math #   import лучше делать вверху кода, так понятнее о чём будет идти речь

a=min(max(int(input('Укажите количество учащихся в первом классе:')),0),50)
b=min(max(int(input('Укажите количество учащихся во втором классе')),0),50)
c=min(max(int(input('Укажите количество учащихся в третьем классе:')),0),50)
child_per_table=2
tables=(a+b+c)/child_per_table

print (math.ceil(tables))
