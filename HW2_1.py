'''
1. Создайте простой скрипт который будет принимать на ввод от пользователя его любимый фильм и год его выхода,
и выводить строку с названием фильма и годом выхода фильма.
Пример вывода - "My favorite movie is Terminator. It was released in 1991."
+3 балла если вывод будет вида "My favorite movie is Terminator. It was released 29 years ago."
Вычислять только разницу в годах.
Строка не меняется от кол-ва лет.
Ожидаются понятные для пользователя запросы на ввод.
Подразумевается что пользователь не будет вводить некорректных данных.
'''
film = input('Enter Yo Favourite Film: ')
old = int(input('Year Of Release Is: '))
year = int(input('Whats Year Is It Now? : '))
how_old = (year - old)
print('Ma Favourite Film Is {}. It Was Released In {}. It Is {} Years Ago.'.format(film, old, how_old))