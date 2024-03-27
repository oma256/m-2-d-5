"""
3.Создать множества с вопросами и ответами. Например: страна - столица. 
В зависимости от длины ответа пользователю предоставляется попытки ввода 
алфавитных символов. На каждые 4 символа в ответе дается одна попытка.
То есть для названия Бишкек должно быть 2 попытки.

Например:
Страна - Кыргызстан
Столица - **
У вас 2 попытки отгадать букву:
1. и
2. ш

Страна - Кыргызстан
Столица - *иш***

Ваш ответ: Бишкек
"""
# def start_game():
#     attempts = 4
#     text = 'азбука'
#     text_len = len(text)
#     text_stars = '*' * text_len
#     temp = ''
#     answer = ''
    
#     print('Что учат в первую очерь при изучении любого языка ?')
#     print(f'Слово состоит из {text_len} букв: {text_stars}\n')

#     while True:
#         char = input('Буква: ')

#         if char not in text:
#             attempts -= 1
#             print(f'Буквы {char} нет в слове')
#             if attempts == 0:
#                 print('Попытки исчерпаны, вы провалили')
#                 break
#             print(f'У вас осталось {attempts} попыт.')
#             continue
        
#         if char in answer:
#             attempts -= 1
#             print('Буква ранее уже была угада вами, но мы все равно вас \
#                    оштрафуем. Минус попытка.')
#             print(f'У вас осталось {attempts} попыт.')
#             continue

#         for i, t in enumerate(text_stars):
#             if text[i] == char:
#                 temp += char
#             else:
#                 if text_stars[i] != '*':
#                     temp += text_stars[i]
#                 else:
#                     temp += '*'
        
#         text_stars = temp
#         temp = ''
#         answer = text_stars
        
#         if '*' not in answer:
#             print(f'Поздравляем, вы угадали слово! {answer.upper()}')
#             break
#         else:
#             print(f'Вы угадали букву "{char}": {answer}')
#             print(f'Нужно угодать еще {answer.count("*")} буквы')


# start_game()


"""
Задача
"""


# class TriangleChecker:

#     def __init__(self, a, b, c) -> None:
#         self.__a = a
#         self.__b = b
#         self.__c = c

#     def is_triangle(self):
#         if isinstance(self.__a, str) or \
#             isinstance(self.__b, str) or \
#              isinstance(self.__c, str):
#             print('Нужно вводить только числа!')
#         elif self.__a < 0 or self.__b < 0 or self.__c < 0:
#             print('С отрицательными числами ничего не выйдет!')
#         elif (self.__a + self.__b) > self.__c and \
#             (self.__a + self.__c) > self.__b and \
#               (self.__b + self.__c) > self.__a:
#                 print('Ура, можно построить треугольник!')
#         else:
#             print('Жаль но из этого треугольника не сделать!')

#     def set_a(self, value):
#         if isinstance(value, str):
#             print('Метод принимает только числовые значения!')
#         else:
#             self.__a = value

#     def get_a(self):
#         return self.__a

#     def set_b(self, value):
#         if isinstance(value, str):
#             print('Метод принимает только числовые значения')
#         else:
#             self.__b = value

#     def get_b(self):
#         return self.__b
    
#     def set_c(self, value):
#         if isinstance(value, str):
#             print('Метод принимает только числовые значения')
#         else:
#             self.__c = value

#     def get_c(self):
#         return self.__c

# triangle = TriangleChecker(1, 2, 15)

# triangle.is_triangle()


"""
Задача
"""

# from math import pi

# class Shape:

#     def __init__(self, name) -> None:
#         self.name = name

#     def get_area(self):
#         pass



# class Triangle(Shape):

#     def __init__(self, name, height, a, b, c) -> None:
#         super().__init__(name)
#         self.__a = a
#         self.__b = b
#         self.__c = c
#         self.__height = height

#     def get_area(self):
#         return (1/2) * self.__a * self.__height


# class Circle(Shape):
#     def __init__(self, name, radius) -> None:
#         super().__init__(name)
#         self.__radius = radius

#     def get_area(self):
#         return pi * (pow(self.__radius, 2))
