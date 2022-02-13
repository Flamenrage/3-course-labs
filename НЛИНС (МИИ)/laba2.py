import pandas as pd
import numpy as np

cities_data = pd.read_csv("data.csv")
#медиана, максимум и минимум до правки данных
print(f"Median\n{cities_data.median()}")
print(f"Max\n{cities_data.max()}")
print(f"Min\n{cities_data.min()}")

arr = cities_data.values #numpy формат

down = list(cities_data.quantile(q=0.25, numeric_only=True)) #нижний квантиль, возвращает список из 4х элементов с квантилями
                                                             #для каждого столбца
up = list(cities_data.quantile(q=0.75, numeric_only=True)) #верхний квантиль
band = list() # межквартильный диапазон данных
up_bound = list() #верхние и нижние границы для каждого столбца
down_bound = list()

for i in range(0,4):
    band.append(up[i] - down[i])
    up_bound.append(up[i] + 1.5 * band[i]) #Qup - 1.5*IQ = Верхний квантиль - 1,5*МДД
    down_bound.append(down[i] - 1.5 * band[i]) #Qdown + 1.5*IQ = Нижний квантиль + 1,5*МДД

# print(up_bound)
# print(down_bound)

for i in range(0,500):
    for j in range(0,4):
        if(arr[i][j] > up_bound[j] or arr[i][j] < down_bound[j]):
            arr[i][j]=None #обнуляем аномальные значения массива

average = list(cities_data.mean()) #среднее арифметическое значений элементов массива

for i in range(0,500):
    for j in range(0,4):
        if(np.isnan(arr[i][j])): #если пропуск
            arr[i][j] = average[j] #меняем значение элемента на средн арифм

print(f"Median\n{cities_data.median()}") #выводим измененные данные
print(f"Max\n{cities_data.max()}")
print(f"Min\n{cities_data.min()}")

laba2 = cities_data
laba2.to_csv("lab2.csv", index=False)

