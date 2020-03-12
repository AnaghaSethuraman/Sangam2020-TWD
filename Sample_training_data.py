import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.integrate import quad
import csv

a = 2.5

def integrand(t):
    return (math.exp(-t))*t**(a-1)
ans, err = quad(integrand, 0, np.inf)
print (ans)

temp = 0
x = 0
y= 1

xaxis=[]
yaxis=[]

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    while y >= (0.05*temp):
        y = ((x**(a-1))*(2.71**(-x)))
        writer.writerow([x, y])
        if y > temp:
            temp = y
        x = x + 0.01

if (a <= 3):
    label = 'Yes'
else:
    label = 'No'

print (label)

data = np.loadtxt('data.csv', delimiter =',')
frequency = data[:,0]
intensity = data[:,1]

plt.plot(frequency, intensity)

plt.plot(x,y, label='Frequency Spectrum')
plt.xlabel('Frequency')
plt.ylabel('Intensity')
plt.title('Frequency Spectrum')
plt.legend()
plt.show()
