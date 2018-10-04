import numpy
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

opint = [18,95]
flops = [100e9,3e12]
txt = ["MOFF","FX"]

f,ax = plt.subplots(1)
ax.scatter(opint,flops)
plt.title("Roofline Model of EPIC vs FX")
plt.xlabel("Operational Intensity (Flops/Byte)")
plt.ylabel("Flops (Gflops/S)")

#Roof of roofline

line = Line2D([0,20],[0.1,4.6e12],c='r')
ax.add_line(line)
line2 = Line2D([20,100],[4.6e12,4.6e12],c='r')
ax.add_line(line2)
line3 = Line2D([20,20],[0,4.6e12],c='g',ls='--')
ax.add_line(line3)

for i,txt in enumerate(txt):
    ax.annotate(txt,(opint[i],flops[i]))
#a2.set_xlim([0,128]

plt.yscale('log',basey=10)
#plt.xscale('log',basex=10)
plt.xlim([0,100])
plt.ylim([0,1e13])
#plt.autoscale(True)
plt.show()
