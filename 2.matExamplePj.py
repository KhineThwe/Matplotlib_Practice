import matplotlib.pyplot as plt
#default colr = blue
#monthly
month = [1,2,3,4,5,6,7,8,9,10,11,12]
income_job1 = [150000,2000000,1000000,3000000,4000000,5000000,1000000,1500000,3500000,5000000,10000000,2000000]
plt.plot(month,income_job1,color='red',linestyle='--',label="Job1")#X,Y
income_job2 = [100000,2000000,2500000,2000000,5000000,5000000,2000000,1000000,2000000,3000000,5000000,40000000]
plt.plot(month,income_job2,color='g',linestyle='-.',label="Job2")#X,Y
plt.xlabel("Monthly in 2022")
plt.ylabel("Income from job")
plt.title("Income from all jobs in 2022")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

"""
ver အလိုက်ပြောင်းနိုင်တယ်
'-' solid line style
'--' dashed line style
'-.' dash-dot line style
':' dotted line style
'.' point marker
',' pixel marker
'0' circle marker
'v' triangle down marker
'^' triangle up marker
'<' triangle left marker
'>' triangle right marker
'1' tri_down marker
'2' tri_up marker
'3' tri_left marker
'4' tri_right marker
's' square marker
'p' pentagon marker 
'*' star marker 
'h' hexagon1 marker 
'H' hexagon2 marker 
'+' plus marker 
'x' x marker 
'D' diamond marker 
'd' thin_diamond marker 
'|' vline marker 
'_' hline marker 
"""
