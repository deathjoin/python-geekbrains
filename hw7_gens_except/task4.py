# Написать функцию которая принимает на вход число от 1 до 100. Если число равно 13,
# функция поднимает исключительную ситуации ValueError иначе возвращает введенное число, возведенное в квадрат.
# Далее написать основной код программы.
# Пользователь вводит число.
# Введенное число передаем параметром в написанную функцию и печатаем результат, который вернула функция.
# Обработать возможность возникновения исключительной ситуации, которая поднимается внутри функции.


def i_hate_13(number):
    if number == 13:
        raise ValueError("i hate 13")

    return number * number


try:
    number = int(input("Введите число: "))
    print(f'Квадрат числа: {i_hate_13(number)}')
except ValueError as error:
    print(error)

print('The end')
