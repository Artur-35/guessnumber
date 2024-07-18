# Импорт функции получения случайных чисел
# из модуля random.
from random import randint

# Получаем случайное число в диапазоне от 1 до 100.
    number = randint(1, 100)
print("Угадайте число от 1 до 100")

while True:
    # Получаем число от пользователя и сохраняем его в переменную.
    guess2 = int(input("Введите число: "))
    
    # Если число меньше загаданного...
    if guess2 < number:
        # ...выводим сообщение.
        print("Ваше число меньше того, что загадано.")
    
    # Если число больше загаданного...
    elifif guess2 > number:
        # ...выводим сообщение.
        print("Ваше число больше того, что загадано.")
    
    # Если число угадано...
    elifif guess2 == number:
        # ...прерываем выполнение программы и...
        break
# ...выводим сообщение.
print("Отличная интуиция! Вы угадали число :)")
редакция от Артура в браузере
