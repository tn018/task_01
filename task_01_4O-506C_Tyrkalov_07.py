import numpy as np
import os
import matplotlib.pyplot as plt

try: os.mkdir('results')
except OSError: pass

w = open('results/task_01_4O-506C_Tyrkalov_07.txt', 'w')
print('x{0:4}y(x)\n'.format(' '), file = w)
A = 512
x = np.linspace(-512,512,1025)
y = -(A+47) * np.sin(np.sqrt(abs((x/2) + (A+47)))) - x * np.sin(np.sqrt(abs((x - (A+47)))))
for i in range(0,1025):
    print('{0}{1:4}{2}'.format(x[i],' ',y[i]), file = w)
w.close()

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.grid()
plt.show()
