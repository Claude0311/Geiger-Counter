from math import sqrt
from matplotlib import pyplot as plt
import numpy as np
n = 7
x = []
y = []
ex = []
ey = []
count_raw  = [124, 23,  8,  8,  9,  8, 12]
t_duration = [ 20, 10, 10, 10, 15, 15, 10]
distance   = [  0,  5, 15, 25, 35, 40, 45]
# altitude  = [ 23, 26, 30, 31, 33, 37, 41]
altitude =   [ 31, 32, 35, 42, 48, 52, 55]

rho_standard = 2.67
base_altitude = 21

for i in range(n):
    y.append(count_raw[i] / t_duration[i])
    ey.append(sqrt(count_raw[i]) / t_duration[i])
    if(i == 0): x.append(0)
    else: x.append((altitude[i] - base_altitude) * rho_standard * 100.)
    print("%g %g"%( x[i], y[i]))

plt.xlabel("Rock Depth (g/cm^2)")
plt.ylabel("Muon Rate (counts/min)")
plt.grid(ls='--')
plt.errorbar(x, y, yerr=ey, fmt='o', label ="Observed")

N = 100
x2 = np.linspace(30,25000,N)
y2 = np.zeros(N)
range_ = 553.4
scale = y[0]
for i in range(N):
    if range_>x2[i]: y2[i] = scale
    else: y2[i] = scale * range_ / x2[i] #prob_surv
plt.plot(x2,y2,label="Muon Survival Prob. in Rock (Scaled)")
plt.title("Muon Rate vs. Rock Depth")
handles, labels = plt.gca().get_legend_handles_labels()
order = [1,0]
plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order])
plt.show()
