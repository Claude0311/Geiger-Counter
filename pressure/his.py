from cProfile import label
import csv

counts = []
pressure = []

with open('data.csv','r') as f:
    csvreader = csv.reader(f,delimiter='\t')
    skip = True
    for row in csvreader:
        if skip:
            skip=False
            continue
        counts.append(int(row[0]))
        pressure.append(float(row[1]))

print(len(counts),len(pressure))
print(sum(counts))
import matplotlib.pyplot as plt
import numpy as np

ct = np.array(counts)/10
c_bin = np.linspace(min(ct),max(ct),30)
p_bin = np.linspace(min(pressure),max(pressure),30)

# plt.hist2d(pressure,ct,bins =[p_bin,c_bin])
# plt.title("Muon rate v.s. Pressure")
# plt.xlabel('Pressure (hPa)')
# plt.ylabel('Muon rate (counts/min)')

def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w
w = 10
ctn = moving_average(ct,w)
prn = moving_average(pressure,w)
c_bin = np.linspace(min(ctn),max(ctn),20)
p_bin = np.linspace(min(prn),max(prn),20)
# plt.title("Muon rate v.s. Pressure")

# plt.hist2d(prn,ctn)

# fig,ax1=plt.subplots()
# ax1.plot(ctn)
# ax1.set_ylabel('Muon rate (counts/min)')
# ax2 = ax1.twinx()
# ax2.plot(prn,color='orange')
# ax2.set_ylabel('Pressure (hPa)')
# plt.show()

from scipy.fftpack import fft
# from scipy.fftpack import *
pf = fft(pressure)
cf = fft(ct)
pfp = np.abs(pf[1:50]) #len(pf)//2
cfp = np.abs(cf[1:50])
c_bin = np.linspace(min(cfp),max(cfp),20)
p_bin = np.linspace(min(pfp),700,20)
# plt.hist2d(pfp,cfp)#,bins=[p_bin,c_bin])
freq = np.arange(1,80)/2003*6
# plt.plot(freq,np.abs(pf[1:80]))
# plt.xlabel(r'frequency ($hour^{-1}$)')
# plt.title('FFT of pressure data')

f_chose =  40
pf[f_chose:len(pf)-f_chose] = 0
p_fil = np.fft.ifft(pf)
cf[f_chose:len(cf)-f_chose] = 0
c_fil = np.fft.ifft(cf)
# print(np.abs(pf[1:len(pf)//2]))

time = np.arange(0,len(c_fil))/6/24
fig,ax1=plt.subplots()

c_fit = np.poly1d(np.polyfit(time,c_fil,1))
# ax1.plot(time,c_fit(time),'b--')
lns1 = ax1.plot(time,c_fil,label='Muon rate',color='blue')
ax1.set_ylabel('Muon rate (counts/min)')
ax2 = ax1.twinx()
p_fit = np.poly1d(np.polyfit(time,p_fil,1))
# ax2.plot(time,p_fit(time),'--',color='orange')
lns2 = ax2.plot(time,p_fil,color='orange',label='pressure')
ax2.set_ylabel('Pressure (hPa)')
ax1.set_xlabel('time (day)')
plt.title('Muon rate v.s Pressure')
lns = lns1+lns2
labs = [l.get_label() for l in lns]
plt.legend(lns, labs, loc=0)
plt.show()
# # show plot
dc = (c_fil[1:]-c_fil[:len(c_fil)-1])/10
dp = (p_fil[1:]-p_fil[:len(p_fil)-1])/10
c_bin = np.linspace(min(dc),max(dc),18)
p_bin = np.linspace(min(dp),max(dp),18)
cp_fit = np.poly1d(np.polyfit(dp,dc,1))
txt = 'dM = {:.3f} dP + {:.3f}'
plt.plot(p_bin,cp_fit(p_bin),'--',label=txt.format(float(cp_fit.c[0]),float(cp_fit.c[1])),color='orange')
plt.hist2d(dp,dc,bins=[p_bin,c_bin])
# plt.hist2d(c_fil,p_fil)
print(np.corrcoef(dc,dp))
print(np.corrcoef(c_fil,p_fil))
plt.ylabel(r'$dM/dt (min^{-1})$')
plt.xlabel(r'$dP/dt (hPa\bullet min^{-1})$')
plt.legend()
plt.title('Muon rate v.s Pressure')
plt.show()

