'''
2. Создайте скрипт который будет принимать от пользователя на ввод три целочисленных значения (a b c)
и выводить результат возведения первого числа в степень второго, а на следующей строке - остаток от целочисленного
деления результат на третье число.
Подразумевается что пользователь не введет число которое может привести к делению на 0
Ожидаются понятные для пользователя запросы на ввод.
Скрипт должен выводить два значения на двух разных строках, а не на одной строке подряд.
+4 балла за использование только одного print()

'''

a = int(input('Enter First Number: '))
b = int(input('Enter Second Number: '))
c = int(input('Enter Third Number: '))
power_of = a ** b
division_of = power_of % c
print(' Raising The First Number To the Power Of Second Number: ', power_of, '\n',
      'The Remained Of The Integer Division Of The Result By The Third Number: ', division_of)
