#Barchart iot so po သင့်တော်
#first test -->without width
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('fivethirtyeight')
decDays = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
xData = np.arange(len(decDays))
#to define width
width = 0.5
Temp = [17,15,17,19,20,22,3,24,11,12,14,24,15,16,15]
# plt.bar(decDays,Temp,color='red',label='temp')
plt.bar(xData+0.0,Temp,width=width,color='red',label='temp')#0.0 နေရာမှာပြမယ်

Humidity = [27,25,27,29,20,22,23,24,21,22,24,24,25,26,25]
# plt.bar(decDays,Humidity,color='g',label='humidity')
plt.bar(xData+0.25,Humidity,width=width,color='g',label='humidity')#0.25 နေရာမှာပြမယ်

Fake = [27,25,27,29,20,22,23,24,21,22,24,24,25,26,25]
# plt.bar(decDays,Humidity,color='g',label='humidity')
plt.bar(xData+0.50,Fake,width=width,color='y',label='Fake')#0.50 နေရာမှာပြမယ်

plt.xlabel("Days in Dec")
plt.ylabel("Temp in Days")
plt.title("Temp")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
