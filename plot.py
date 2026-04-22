import matplotlib.pyplot as plt
import numpy as np

height = [100,120,130,150,180]
weight = [30,40,50,60,70]

plt.plot(height, weight, marker='o', linestyle='-', color='b')
plt.bar(height, weight)
plt.xlabel('Height')
plt.ylabel('Weight')
plt.title('Bar Plot of Height vs Weight')
plt.show()