# День 13 — функции (def)
# Запуск: python lessons/day_13.py
#
# Сначала прочитай theory/day_13_functions.md (~20 мин), потом пиши код сам.
# Задачи НЕ повторяют примеры из теории.
# Подсказки — только по запросу в чате.


# --- Задача A ---
# Напиши функцию rectangle_area(width, height).
# Она **возвращает** площадь прямоугольника (width * height), ничего не печатает.
# Ниже вызови её: спроси у пользователя ширину и высоту (int),
# передай в функцию, результат выведи одной строкой:
#   Площадь: 50
def rectangle_area(width, height):
    return width * height
x=int(input("Введите ширину: "))
y=int(input("Введите высоту: "))
result = rectangle_area(x, y)
print("Площадь:", result)

# --- Задача B ---
# Напиши функцию greeting(name) — печатает: Привет, ...!
# (имя подставляется из параметра)
# Вызови её три раза с разными именами (строками в коде, без input).
def greeting(name):
    print("Привет!", name)
greeting("Sergey")
greeting("Alexey")
greeting("Ivan")
# --- Задача C (опционально) ---
# Напиши функцию ticket_price(age):
#   если age < 12  → return 0
#   если age >= 65 → return 200
#   иначе          → return 400
# Спроси возраст у пользователя, вызови функцию, выведи:
#   Стоимость билета: ...
def ticket_price(age):
    if age < 12:
        return 0
    elif age >= 65:
        return 200
    else:
        return 400
x = int(input("Введите возраст: "))
f = ticket_price(x)
print ("Стоимость билета =", f)

# --- Задача D ---
# Сборка — в отдельном файле: problem_D/day_13D.py
