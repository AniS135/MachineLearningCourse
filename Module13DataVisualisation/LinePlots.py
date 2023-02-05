import matplotlib.pyplot as plt
import numpy as np

# Line Plot
x = np.arange(10)
y1 = x ** 2
y2 = 2 * x + 3

print(x)
print(y1)
print(y2)

plt.style.use("seaborn")

plt.plot(x, y1, color = 'red', label = "Apple")
plt.plot(x, y2, color = 'green', label = "Kiwi")
plt.xlabel("Time")
plt.ylabel("Price")
plt.title("Prices of Fruit over Time")
plt.show()
