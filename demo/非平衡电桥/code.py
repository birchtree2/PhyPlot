import numpy as np
from phyplot import plot,calc
N = 10
t = [22.5] #温度,每5°C一个数据
U = [31.1,38.8,44.7,50.4,56.1,61.9,67.5,73.4,78.5,83.9] #电压
alphas = []
E = 1.3 #电源电动势
alpha_expect = 0.004280
for i in range(1, N):
    t.append(t[i-1] + 5)
for t_, U_ in zip(t, U):
    U_ = U_ / 1000
    alphas.append(4 * U_ / (t_ * (E - 2 * U_)))
alpha = sum(alphas) / len(alphas)
print("直接计算法:")
calc.relative_error(alpha_expect,alpha)

print("U-t曲线法:")
plt1=plot.MyPlot({'t/°C':t,'U/mV':U},
        filename="Cu50 电阻 U-t 特性曲线")
plt1.plot_table()
plt1=plot.MyPlot({'t/°C':t,'U/mV':U},filename="Cu50 电阻 U-t 特性曲线")
k,b=plt1.plot_fig()
calc.relative_error(alpha_expect,(4*(k[0]*0.001)/E))
#k是斜率,b是截距 但是返回的是一个list,所以是k[0]

print("1/t-1/U曲线法:")
invU=[]
invt=[]
for (x,y) in zip (t,U):
    invt.append(1/x)
    invU.append(1/y)
plt2=plot.MyPlot({'U^-1/mV^-1':invU,'t^-1/℃^-1':invt},filename="Cu50 电阻t^-1 - U^-1特性曲线")
k,b=plt2.plot_fig()
calc.relative_error(alpha_expect,(4*(k[0]*0.001)/E))

print("R-t曲线法:")
t = [22.5,30.9,33.9,38.1,43.0,47.5,52.3,58.1,62.0,67.3]
R = [55.20,56.99,57.65,58.55,59.60,60.56,61.62,62.84,63.68,64.83]
plt3=plot.MyPlot({'t/°C':t,'R/Ω':R},filename="Cu50 电阻 R-t 特性曲线")
k,b=plt3.plot_fig()
calc.relative_error(alpha_expect,k[0]/b[0])
# R=R0(1+at)
"""
直接计算法:
真实值=0.00428 测量值=0.004461695997333259 误差: 4.25%
U-t曲线法:
回归结果: U=1.16*x+6.61 (mV)
真实值=0.00428 测量值=0.0035569230769230773 误差: 16.89%
1/t-1/U曲线法:
回归结果: t^-1=1.49*x+-0.00 (℃^-1)
真实值=0.00428 测量值=0.004596517870894131 误差: 7.40%
R-t曲线法:
回归结果: R=0.21*x+50.36 (Ω)
真实值=0.00428 测量值=0.00426866346118975 误差: 0.26%
"""
