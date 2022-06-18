import csv

counts = []
thetas = []
times = []

with open('EW.csv','r') as f:
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

plt.grid(ls='--')

plt.bar(x, y, yerr=ey, label ="Observed", width=10, capsize=5, color="orange")

plt.xlabel('WEST                        Zenith angle (degree)                        EAST')
plt.ylabel('Muon rate (counts/min)')
plt.title('East-West effect')

x_th = np.linspace(-90,90,100)
y_th = y[0]*np.cos(x_th/180*np.pi)**2
plt.plot(x_th,y_th,label=r"$cos^2(\theta)$")
plt.legend()

plt.show()