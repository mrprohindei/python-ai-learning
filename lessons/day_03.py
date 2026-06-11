# День 3 — числа и арифметика


# --- Задача A ---
# Спроси два числа у пользователя. Выведи их сумму.
number_1 = int(input("Введите 1-ое число"))
number_2 = int(input("Введите 2-ое число"))
summ = number_1 + number_2
print("Сумма ваших чисел:", number_1, "+", number_2, "=", summ)
# --- Задача B ---
# Спроси два числа. Выведи результат всех четырёх операций:
# сложение, вычитание, умножение, деление.
number_3 = int(input("Введите 1-ое число"))
number_4 = int(input("Введите 2-ое число"))
summ2 = number_3 + number_4
sub = number_3 - number_4
mult = number_3 * number_4
div = number_3 / number_4
print("Сумма ваших чисел:", number_3, "+", number_4, "=", summ2)
print("Разница ваших чисел:", number_3, "-", number_4, "=", sub)
print("Произведение ваших чисел:", number_3, "*", number_4, "=", mult)
print("Частное ваших чисел:", number_3, "/", number_4, "=", div)