import numpy as np
import matplotlib.pyplot as plt
import os

try: os.mkdir('results')
except OSError: pass

A = 512
x = np.linspace(-512,512,1025)
y = (-(A+47) * np.sin(np.sqrt(abs((x/2) + (A+47))))
     - x * np.sin(np.sqrt(abs((x - (A+47))))))

STOLBIKI = np.column_stack((x, y))
PROBEL = ' '
np.savetxt('results/task_01_4O-506C_Tyrkalov_07.txt',
           STOLBIKI, delimiter=f'{4*PROBEL}')

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.grid()
plt.show()
