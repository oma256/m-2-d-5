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

# text = 'азбука'
# answer_text = ''
# answer_text_final = ''
# failed_count = 0

# text_stars = '*' * len(text)
# answer = ''
# print(text_stars)

# while True:
#     char = input('Скажите букву: ')
#     if char in text:
#         for i, c in enumerate(text):
#             if char != c:
#                 text = text.replace(char, '*')
#             else:
#                 continue

#     print(text)


# while True:
#     char = input('Скажите букву: ')

#     if char in text:
#         if char in answer_text or char in answer_text_final:
#             print('Буква уже угадана')
#         else:
#             if answer_text != '':
#                 for i, a in enumerate(answer_text):
#                     if a != '*':
#                         answer_text_final += a
#                     else:
#                         char_index = text.index(char)
#                         if i == char_index:
#                             answer_text_final += text[i]
#                         else:
#                             answer_text_final += '*'

#                 print(f'Буква {char} есть в слове')
#                 print(answer_text_final)
#             else:
#                 for c in text:
#                     if c == char:
#                         answer_text += char
#                     else:
#                         answer_text += '*'

#                 print(f'Буква {char} есть в слове')
#                 print(answer_text)



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

from math import pi

class Shape:

    def __init__(self, name) -> None:
        self.name = name

    def get_area(self):
        pass



class Triangle(Shape):

    def __init__(self, name, height, a, b, c) -> None:
        super().__init__(name)
        self.__a = a
        self.__b = b
        self.__c = c
        self.__height = height

    def get_area(self):
        return (1/2) * self.__a * self.__height


class Circle(Shape):
    def __init__(self, name, radius) -> None:
        super().__init__(name)
        self.__radius = radius

    def get_area(self):
        return pi * (pow(self.__radius, 2))
