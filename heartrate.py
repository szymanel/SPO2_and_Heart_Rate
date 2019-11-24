#-*-coding:utf-8-*-

import matplotlib.pyplot as plt
import numpy as np
import hrcalc

# load log data
red = []
with open("./red.log", "r") as f:
    for r in f:
        red.append(int(r))

ir = []
with open("./ir.log", "r") as f:
    for r in f:
        ir.append(int(r))

# x-axis values



heartrate = []
for i in range(37):
    #print(hrcalc.calc_hr_and_spo2(ir[25*i:25*i+100], red[25*i:25*i+100]))
    hr_count = hrcalc.calc_heart_and_spo2(ir[5*i:5*i+900], red[5*i:5*i+900])
    hr = hrcalc.calc_heart_and_spo2(ir[5*i:5*i+900], red[5*i:5*i+900])
    if hr > 40 and hr <250:
       heartrate.append (hr)
       print (hr)
    
x = np.arange(len(heartrate))

fig = plt.figure()
ax = fig.add_subplot(111)

# RED LED
ax.plot(x, heartrate, c="red", label="HEART_RATE")



# modify limits
ax.set_ylim(0, 350)
# ax.set_xlim(400,600)

# show legend
ax.legend(loc="best")

plt.show()