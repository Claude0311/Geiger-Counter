import csv

ocounts = []
othetas = []
otimes = []
icounts = []
ithetas = []
itimes = []


with open('distance.csv','r') as f:
    csvreader = csv.reader(f,delimiter=',')
    skip = True
    for row in csvreader:
        if skip:
            skip=False
            continue
        othetas.append(int(row[0]))
        ocounts.append(int(row[1]))
        otimes.append(int(row[2]))
        print(len(row))
        if len(row)>3 and row[5]!='':
            ithetas.append(int(row[3]))
            icounts.append(int(row[4]))
            itimes.append(int(row[5]))
print(len(othetas),len(ithetas))

import matplotlib.pyplot as plt
import numpy as np
plt.grid(ls='--')

ox = np.array(othetas)
oy = np.array(ocounts)/np.array(otimes)
oey = np.sqrt(np.array(ocounts))/np.array(otimes)
plt.errorbar(ox, oy, yerr=oey, label ="outdoor", fmt='o',)

oy_fit = np.poly1d(np.polyfit(np.log10(ox),np.log10(oy),1))

otxt = 'log(y) = {:.3f} log(x) + {:.3f}'
plt.plot(ox,10**oy_fit(np.log10(ox)),'--',color='blue',label=otxt.format(float(oy_fit.c[0]),float(oy_fit.c[1])))

ix = np.array(ithetas)
iy = np.array(icounts)/np.array(itimes)
iey = np.sqrt(np.array(icounts))/np.array(itimes)
plt.errorbar(ix, iy, yerr=iey, label ="indoor", fmt='o',)


iy_fit = np.poly1d(np.polyfit(np.log10(ix),np.log10(iy),1))
print(iy_fit.c)
plt.plot(ix,10**iy_fit(np.log10(ix)),'--',color='orange',label=otxt.format(float(iy_fit.c[0]),float(iy_fit.c[1])))
print(iy_fit)
# thet = np.array([0,10,20,30,40,50,60,70,80,90])/180*np.pi
# print('y\'=')
# print(4*np.sin(thet))
# print(10**iy_fit(np.log10(4*np.sin(thet))))
plt.xlabel('distance (cm)')
plt.ylabel('Muon rate (counts/min)')
plt.title('Muon rate v.s. distance')

# x_th = np.linspace(-90,90,100)
# y_th = y[0]*np.cos(x_th/180*np.pi)**2
# plt.plot(x_th,y_th,label=r"$cos^2(\theta)$")
plt.xscale("log")
plt.yscale("log")
plt.legend()
plt.show()