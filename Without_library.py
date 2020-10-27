'''

Write a code in Python to compute and plot the Cross Correlation function
between the given signals.Both signals should have 100 samples. fc is 0.1 hz.
w(t) is a white Gaussian noise.
a. x(t) = 5sin(2*pi*fc*t) + w(t)
b. y(t) = 3cos(2*pi*fc*t) + w(t)


'''


import matplotlib.pyplot as plt
import numpy as np

mean = 0
std = 1 
step = 1
f = 0.1
samples = 100
white_noise = np.random.normal(mean, std, size=samples)
x = []                         # X coordinates for signal Plotting
ss1 = []                       # dummy list to store signal 1
ss2 = []                       # dummy list to store signal 2
corr = np.arange(0,2*samples)  # dummy numpy array for storing Correlation values
x1 = np.arange(-samples,samples)    # X coordinates for Correlation Plotting

for i in range(0,samples):
    # X coordinates for Signal Plotting
    x.append(i)
    # Signal + AWGN
    ss1.append(5*np.sin(2 * np.pi * f * x[i]/step) + white_noise[i])
    # Signal + AWGN
    ss2.append(3*np.cos(2 * np.pi * f * x[i]/step) + white_noise[i])

# Loop to generate cross correlation values for positive values of 'n'
for i in range(0,len(ss1)):
    temp = 0    # temporary variable to change the index
    summ = 0    # temporary variable to store sum for a perticular index
    for j in range(i,len(ss1)):
       summ = summ + ss2[j]*ss1[temp]
       temp = temp+1
    corr[i+len(ss1)] = summ      # storing correlation value in dummy array for plotting

# Loop to generate cross correlation values for negative values of 'n'
for i in range(0,len(ss1)):
    temp = 0    # temporary variable to change the index
    summ = 0    # temporary variable to store sum for a perticular index
    for j in range(i,len(ss1)):
       summ = summ + ss2[temp]*ss1[j]
       temp = temp+1
    corr[len(ss1)-i] = summ      # storing correlation value in dummy array for plotting


# Plotting using PyPlot
'''
# Plotting of Signal 1
plt.figure()
plt.subplot(711)
plt.plot(x,white_noise)
plt.grid(True)
plt.xlabel('Frequency')
plt.title('5sin(2(pi)(fc)t) + AWGN')
plt.ylabel('Amplitude')


# Plotting of Signal 1
plt.subplot(713)
plt.plot(x,ss1)
plt.grid(True)
plt.xlabel('Frequency')
plt.title('5sin(2(pi)(fc)t) + AWGN')
plt.ylabel('Amplitude')

# Plotting of Signal 2
plt.subplot(715)
plt.plot(x,ss2)
plt.grid(True)
plt.title('3cos(2(pi)(fc)t) + AWGN')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')

# Plotting of cross correlation of two signal
plt.subplot(717)
'''
plt.plot(x1, corr, 'g')
plt.grid(True)
plt.title('Cross Correlation')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.show()



