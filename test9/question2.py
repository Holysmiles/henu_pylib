import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(-10, 10, 50)
y = x ** 2

plt.plot(x, y, 'ro--')
plt.xlabel('tick')
plt.ylabel('voltage')
plt.title('抛物线示意图')

plt.show()
