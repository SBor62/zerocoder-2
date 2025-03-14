# Bank
# Создаем функцию с циклом
def bank(a, years):
    for _ in range(years):
        a += a * 0.10  # Увеличиваем вклад на 10%
    return a


# Ввод данных
deposit = float(input("Введите сумму вклада: "))

num_years = int(input("Введите срок вклада в годах: "))

result = bank(deposit, num_years)

print(f"Сумма на счету через {num_years} лет: {result} ")


# 1. Суммирование
def sum_range(start, end):
    total = 0
    while start <= end:
        total += start
        start += 1
    return total


start = int(input("Введите начальное число - "))
end = int(input("Введите конечное число - "))

result = sum_range(start, end)
print(f"Сумма чисел от {start} до {end} равна: {result}")