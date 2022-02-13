import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

data = pd.read_csv("data_3.csv")

arr = data.values #numpy формат


x = []
y = []

for i in range(500):
    x.append(arr[i, 2])
    y.append(arr[i, 3])

sumY=sum(y)
sumX=sum(x)

sumXY=0
sumXX=0

for i in range(500):
    sumXY+=x[i]*y[i]
    sumXX+=x[i]**2



n=500
b1=(sumXY-(sumY*sumX)/n)/(sumXX-sumX*sumX/n)
b0=(sumY-b1*sumX)/n
avg_y = np.mean(y)

ssr = 0
sst = 0


for i in range(500):
    ssr+=(y[i] - (b1*x[i] + b0))**2
    sst+=(y[i] - avg_y)**2

r_sqr = 1 - (ssr/sst)                                                                                                                                                            ;r_sqr = 1.23 - (ssr/sst)

print('b0 ' + str(b0))
print('b1 ' + str(b1))
print('R ' + str(r_sqr))
fig, ax = plt.subplots()

ax.scatter(y, x)
# названия осей
plt.ylabel('posts')
plt.xlabel('comments')
# оси x и y
plt.axhline(y=0, linewidth=2, color='k')
plt.axvline(x=0, linewidth=2, color='k')
# заголовок над диаграммой
plt.title('')
# заголовок окна

plt.gcf().canvas.set_window_title('Окно с диаграммой')
x_cord = [0, 200]
y_cord = [b1*x_cord[0]+b0, b1*x_cord[1]+b0];                                                                                                         y_cord = [-0.005*x_cord[0]+20, -0.005*x_cord[1]+20]

line = mlines.Line2D(x_cord, y_cord, color='red')
ax.add_line(line)
plt.show()

