#python ကို install လုပ်ထားတယ် ပြီးတော့ စက်ထဲမှာ Install လုပ်တယ်ဆိုတာစက်တစ်ခုလုံးထဲမှာ install လုပ်ထားတာဖြစ်တယ်
#virtual env ကျတော့ စက်ထဲမှာ folder တစ်ခုရှိမယ် အဲ့ထဲမှာ virtual env အသစ်တစ်ခုဖန်တီးလိုက်တာ နေရာလွတ်လေးဘာမှမရှိဘူး
#virtual env ထဲမှာထပ် install လုပ်ပေးမှရမယ် ဘာကောင်းလဲဆိုတော့တခြားနေရာမှာသွားပြန် run mal ဆိုရင် သူ့ရဲံ ver တိုင်းလိုက် down pi tok work လို့ရ
#venv ---> right click ---> open in terminal
#pip install matplotlib in env or pip install matplotlib==ver no or pip install --upgrade matplotlib
#pip list in env
#pip show matplotlib
#pip uninstall matplotlib
#can save in pnh
import matplotlib.pyplot as plt
xData = [1,2,3,4,5,6,7,8,9,10]
yData = [10,20,30,40,50,60,70,80,90,100]
plt.plot(xData,yData)
plt.show()
