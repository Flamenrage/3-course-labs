import random

# На языке Python разработайте скрипт, который с помощью генетического алгоритма
# и полного перебора решает следующую задачу. Дано N наименований продуктов,
# для каждого из которых известно m характеристик.
# Необходимо получить самый дешевый рацион из k наименований,
# удовлетворяющий заданным медицинским нормам для каждой из m характеристик.

names = ['Яблоко', 'Бекон', 'Йогурт', 'Хлеб', 'Банан', 'Апельсин']
# норма для каждой характеристики (граммов на 100 грамм)
rate = [34, 25, 60, 500]
# цены продуктов (за 100 грамм)
prices = [30, 150, 40, 15, 45, 50]
# матрица значений характеристик для каждого из продуктов (граммов на 100 грамм)
# белки, жиры, углеводы, Ккал
A = [
    [1, 1, 10, 47],  
    [16, 40, 0, 420], 
    [4, 3, 7, 75], 
    [9, 4, 49, 259], 
    [2, 1, 21, 89],
    [1, 0, 8, 45]
]


def random_chromosome_value(size, max_digit):
    '''
    Генерируем случайную хромосому, возвращая строку
    max_digit: максимальное значение хромосомы (в данном случае число продуктов)
    '''
    chromosome_value = ''
    for i in range(size):
        chromosome_value += str(random.randint(0, max_digit))
    return chromosome_value
