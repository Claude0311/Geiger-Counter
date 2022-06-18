import csv

counts = []
thetas = []
times = []

with open('theta.csv','r') as f:
    csvreader = csv.reader(f,delimiter='\t')
    skip = True
    for row in csvreader:
        if skip:
            skip=False
            continue
        thetas.append(int(row[0]))
        counts.append(int(row[1]))
        times.append(float(row[2]))

import matplotlib.pyplot as plt
import numpy as np
x = np.array(thetas)
y = np.array(counts)/np.array(times)
ey = np.sqrt(np.array(counts))/np.array(times)
plt.errorbar(x, y, yerr=ey, fmt='o', label ="Observed")

# counts2 = np.array([123,94,738,9])
# times2 = np.array([60,60,990,20])
# y2 = np.array(counts2)/np.array([])
# ey2 = np.sqrt(np.array(counts2))/np.array(times2)
# plt.errorbar(np.array([0,30,60,90]), y2, yerr=ey2, fmt='o', label ="d=10")

plt.xlabel('Zenith angle (degree)')
plt.ylabel('Muon rate (counts/min)')
plt.title('Muon rate v.s. Zenith angle')
plt.grid(ls='--')
x_th = np.linspace(0,90,100)
y_th = y[0]*np.cos(x_th/180*np.pi)**2
plt.plot(x_th,y_th,label=r"$cos^2(\theta)$")
plt.legend()

plt.show()