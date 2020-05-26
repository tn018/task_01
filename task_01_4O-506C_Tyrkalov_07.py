import numpy as np
import matplotlib.pyplot as plt
import os

if not os.path.exists('results'):
    os.mkdir('results')
    
A = 512

x = np.linspace(-512,512,1025)
y = -(A+47) * np.sin(np.sqrt(abs((x/2) + (A+47)))) - x * np.sin(np.sqrt(abs((x - (A+47)))))

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()

p = os.path.join(os.getcwd(),'results','task_02_4O-506C_Tyrkalov_07.txt')
    
with open(p, 'w') as file:
    file.write('x{0:4}y(x)\n'.format(' '))
    for i in range(0,1025):
        file.write('{0}{1:4}{2}\n'.format(str(x[i]),' ',str(y[i])))
        

