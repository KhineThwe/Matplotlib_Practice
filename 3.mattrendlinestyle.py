import matplotlib.pyplot as plt
#black for k
month = [1,2,3,4,5,6,7,8,9,10,11,12]
#plt.style.use('ggplot')#သုံးချင်တဲ့style ကို Use nae write
#plt.style.use('dark_background')
plt.style.use('fivethirtyeight')
income_job1 = [150000,2000000,1000000,3000000,4000000,5000000,1000000,1500000,3500000,5000000,10000000,2000000]
plt.plot(month,income_job1,color='red',linestyle='--',label="Job1")#X,Y
income_job2 = [100000,2000000,2500000,2000000,5000000,5000000,2000000,1000000,2000000,3000000,5000000,40000000]
plt.plot(month,income_job2,color='c',linestyle='-.',label="Job2")#X,Y
plt.xlabel("Monthly in 2022")
plt.ylabel("Income from job")
plt.title("Income from all jobs in 2022")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
print(plt.style.available)#ရရှိနိုင်သော design များ
