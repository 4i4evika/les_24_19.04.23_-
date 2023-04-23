### Зад.1. Создайте класс Circle (окружность). Для данного класса реализуйте ряд перегруженных операторов:
# ■ Проверка на равенство радиусов двух окружностей (операция = =);
# ■ Сравнения длин двух окружностей (операции >, <, <=,>=);
# ■ Пропорциональное изменение размеров окружности, путем изменения ее радиуса (операции + - += -=).

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#         self.circumference = self.radius*3.14*2
#
#     def __add__(self, other):
#         self.radius += other
#         self.circumference = self.radius * 3.14 * 2
#         return self.circumference
#
#     def __iadd__(self, other):
#         return self.__add__(other)
#
#     def __sub__(self, other):
#         return self.__add__(-other)
#
#     def __isub__(self, other):
#         return self.__add__(-other)
#
#     def __lt__(self, other):
#         return self.circumference < other.circumference
#
#     def __le__(self, other):
#         return self.circumference <= other.circumference
#
#     def __gt__(self, other):
#         return self.circumference > other.circumference
#
#     def __ge__(self, other):
#         return self.circumference >= other.circumference
#
#     def __eq__(self, other):
#         return self.radius == other.radius
#
#
# a = Circle(10)
# a += 20
# print(a)
# a = Circle(10)
# a -= 5
# print(a)
# a = Circle(10)
# print(a + 20)
# a = Circle(10)
# print(a - 5)
# b = Circle(2)
# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)



### Зад.2. Создайте класс Complex (комплексное число). Более подробно ознакомиться с комплексными числами можно
# по ссылке. Создайте перегруженные операторы для реализации арифметических операций для по работе с комплексными
# числами (операции +, -, *, /).

# class Complex:
#     def __init__(self, valid, imaginary):
#         self.valid = valid
#         self.imaginary = imaginary
#
#     def __add__(self, other):
#         return Complex(self.valid + other.valid, self.imaginary + other.imaginary)
#
#     def __sub__(self, other):
#         return Complex(self.valid - other.valid, self.imaginary - other.imaginary)
#
#     def __mul__(self, other):
#         return Complex((self.valid * other.valid) + (self.imaginary * other.imaginary * (-1)), \
#                        (self.valid * other.imaginary) + (self.imaginary * other.valid))
#
#     def __truediv__(self, other):
#         return Complex(((self.valid * other.valid) + (self.imaginary * other.imaginary)) / \
#                                             ((other.valid ** 2) + (other.imaginary ** 2)), \
#                        ((self.valid * other.imaginary * (-1)) + (self.imaginary * other.valid)) / \
#                                              ((other.valid ** 2) + ((other.imaginary ** 2))))
#
#
#     def __str__(self):
#         if self.imaginary == 0:
#             result = "%.2f+0.00i" % (self.valid)
#         elif self.valid == 0:
#             if self.imaginary >= 0:
#                 result = "0.00+%.2fi" % (self.imaginary)
#             else:
#                 result = "0.00-%.2fi" % (abs(self.imaginary))
#         elif self.imaginary > 0:
#             result = "%.2f+%.2fi" % (self.valid, self.imaginary)
#         else:
#             result = "%.2f-%.2fi" % (self.valid, abs(self.imaginary))
#         return result
#
# 
# a = Complex(13, 1)
# b = Complex(7, -6)
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)



### Зад.3. Вам необходимо создать класс Airplane (самолет). С помощью перегрузки операторов реализовать:
# ■ Проверка на равенство типов самолетов (операция = =);
# ■ Увеличение и уменьшение пассажиров в салоне самолета (операции + - += -=);
# ■ Сравнение двух самолетов по максимально возможному количеству пассажиров на борту (операции > < <= >=).

# class Airplane:
#     def __init__(self, type, passengers, capacity):
#         self.type = type
#         self.passengers = passengers
#         self.capacity = capacity
#
#     def __str__(self):
#         return f'Самолет: {self.type}\n' \
#                f'    Количество пассажиров: {self.passengers}'
#
#     def __add__(self, other):
#         self.passengers += other
#         return self
#
#     def __iadd__(self, other):
#         return self.__add__(other)
#
#     def __sub__(self, other):
#         return self.__add__(-other)
#
#     def __isub__(self, other):
#         return self.__add__(-other)
#
#     def __lt__(self, other):
#         return self.capacity < other.capacity
#
#     def __le__(self, other):
#         return self.capacity <= other.capacity
#
#     def __gt__(self, other):
#         return self.capacity > other.capacity
#
#     def __ge__(self, other):
#         return self.capacity >= other.capacity
#
#     def __eq__(self, other):
#         return self.type == other.type
#
#     def __ne__(self, other):
#         return self.type != other.type
#
#
# a = Airplane('пассажирский', 300, 500)
# a += 50
# print(a)
# a -= 100
# print(a)
# print(a + 10)
# print(a - 10)
# b = Airplane('военный', 10, 140)
# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)



### Зад.4. Создать класс Flat (квартира). Реализовать перегруженные операторы:
# ■ Проверка на равенство площадей квартир (операция ==);
# ■ Проверка на неравенство площадей квартир (операция !=);
# ■ Сравнение двух квартир по цене(операции> < <= >=).

# class Flat:
#     def __init__(self, square, price):
#         self.square = square
#         self.price = price
#
#     def __lt__(self, other):
#         return self.price < other.price
#
#     def __le__(self, other):
#         return self.price <= other.price
#
#     def __gt__(self, other):
#         return self.price > other.price
#
#     def __ge__(self, other):
#         return self.price >= other.price
#
#     def __eq__(self, other):
#         return self.square == other.square
#
#     def __ne__(self, other):
#         return self.square != other.square
#
#
# a = Flat(50, 5000000)
# b = Flat(65, 12000000)
# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)