import numpy as np
import matplotlib.pyplot as plt
'''
x = [1, 6, 3]
y = [5, 2, 7]
manzanas = [20,10,25,30]
nombres = ["Ana","Juan","Diana","Catalina"]

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

fig, ax = plt.subplots()
ax.fill_between(x, y)
plt.show()

fig, ax = plt.subplots()
ax.bar(x,y)
plt.show()

fig, ax = plt.subplots()
ax.barh(x, y)
plt.show()

fig, ax = plt.subplots()
x = np.random.normal(5, 1.5,
size=1000)
ax.hist(x, np.arange(0, 11))
plt.show()

plt.pie(manzanas, labels=nombres, autopct="%0.1f%%")
plt.axis("equal")
plt.show() 
'''

fig, ax = plt.subplots()
dias = ['L', 'M', 'X', 'J', 'V', 'S', 'D']
temperaturas = {'Madrid':[28.5, 30.5, 31, 30, 28, 27.5, 30.5], 'Barcelona':[24.5,
25.5, 26.5, 25, 26.5, 24.5, 25]}
ax.plot(dias, temperaturas['Madrid'], color = 'tab:purple')
ax.plot(dias, temperaturas['Barcelona'], color = 'tab:green')
plt.show()
