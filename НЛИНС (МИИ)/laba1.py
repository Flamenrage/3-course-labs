import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


posts_per_week = np.random.normal(18, 4, 50) #посты, мед: 18, макс 30, мин 4.6
tabs_per_week = np.random.normal(20,2, 50) #закладки, мед: 20, макс 26, мин 12
comments_per_week = np.random.gamma(30,1,50) #комменты, мед: 30, макс 49.5, мин 14
carm_value = np.random.binomial(n=5, p=0.8, size=50) #карма, мед: 4, макс 5, мин 1
array = dict()
for i in range(50):
     rand = random.randint(0,100)
     r = random.randint(5,20)
     r_column = random.randint(0,4)
     if rand>80:
         if (r%2==0):
             if r_column == 0:
                 posts_per_week[i]+= posts_per_week[i] -  posts_per_week[i]/r
             if r_column == 1:
                 tabs_per_week[i] += tabs_per_week[i] - tabs_per_week[i]/r
             if r_column == 2:
                 comments_per_week[i] += comments_per_week[i] - comments_per_week[i]/r
         else:
                 if r_column==0:
                     posts_per_week[i]=np.nan
                 if r_column==1:
                     tabs_per_week[i]=np.nan
                 if r_column==2:
                     comments_per_week[i]=np.nan

array = {'posts_per_week':posts_per_week,'tabs_per_week':tabs_per_week,
         'comments_per_week':comments_per_week,'carm_value':carm_value}
df = pd.DataFrame(data=array)
data_frame = pd.read_csv("data.csv")
df.to_csv("data.csv",index=False)

print(f"Median\n{df.median()}")
print(f"Max\n{df.max()}")
print(f"Min\n{df.min()}")

#гистограмма
show_data = df["comments_per_week"]
show_data.plot(kind='bar')
plt.ylabel('comments per week')
plt.xlabel('users id')
plt.title('Comment statistics')
plt.show()
   
#линейная регрессия
X = df[["posts_per_week"]]
y = df[["comments_per_week"]]
regressor = LinearRegression()
regressor.fit(X, y)

plt.scatter(X, y, color='red')
plt.plot(X, regressor.predict(X), color='blue')
plt.title('Linear regression of posts/comments')
plt.xlabel('posts')
plt.ylabel('comments')
plt.show()