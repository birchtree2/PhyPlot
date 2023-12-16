import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
from typing import Dict, List

class MyPlot:
    def __init__(self, data: Dict[str, List[float]],x_label: str):
        self.data = data
        self.x_label = x_label

    def plot_table(self) -> None:
        # 设置图表大小
        fig, ax = plt.subplots(figsize=(len(self.data)*1.8, len(self.data[self.x_label])*0.4))
        
        # 创建表格数据
        table_data = {'序号': np.arange(len(self.data[self.x_label]))+1}
        table_data.update(self.data)

        plt.rc("font", family="SimSun", size=13, weight="bold")
        ax.axis('off')  # 关闭坐标轴
        
        rowLabels=['序号']
        for key, values in self.data.items():
            rowLabels.append(key)
        
        cellText=list(map(list, zip(*table_data.values())))
        cellText = [list(row) for row in zip(*cellText)] #按行
        
        table = ax.table(cellText=cellText
                     ,loc='center', cellLoc='center',rowLabels=rowLabels)
        table.auto_set_font_size(False)
        table.set_fontsize(14)
        table.scale(1, 1)  # 等比例缩放

        # 保存表格
        plt.savefig('table.png')

    def plot_scatter_with_regression(self, fit_deg: int = 1, show_coordinate:bool=False) -> None:
        # 创建figure和子图
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.grid()
        plt.rc("font", family="SimSun", size=13, weight="bold")

        for key, values in self.data.items():
            if key != self.x_label:
                ax.scatter(self.data[self.x_label], values, label='')
                if show_coordinate:
                    for i in range(len(self.data[self.x_label])):
                        ax.annotate(f"({self.data[self.x_label][i]}, {values[i]})", (self.data[self.x_label][i], values[i]), textcoords="offset points", xytext=(0,10), ha='center')

        if fit_deg == 1:
            for label, values in self.data.items():
                if label != self.x_label:
                    # 计算线性回归的多项式系数
                    coefficients = np.polyfit(self.data[self.x_label],values,fit_deg) 
                    poly = np.poly1d(coefficients)
                    equation= f"{label}={coefficients[0]:.2f}*x+{coefficients[1]:.2f}"
                    lx=np.arange(min(self.data[self.x_label]),max(self.data[self.x_label])+0.2,step=0.1) #画曲线的点要更多
                    ax.plot(lx, poly(lx), color='orange', label=equation)
        else: #画平滑曲线
            for label, values in self.data.items():
                if label != self.x_label:
                    m = make_interp_spline(self.data[self.x_label], values)
                    xs = np.linspace(min(self.data[self.x_label]),max(self.data[self.x_label]), 500)
                    ys = m(xs)
                    plt.plot(xs, ys)

        ax.set_title(f"Graph")
        ax.set_xlabel(self.x_label)
        ax.legend()
        # 保存图表
        plt.savefig('figure.png')

    def plot(self, fit_deg: int = 1) -> None:
        self.plot_table()
        self.plot_scatter_with_regression(fit_deg)

x=[4,8,12,16,20]
y=[1.2,1.35,1.45,1.56,1.6]
m=MyPlot({'x/mm':x,'U/V':y},x_label='x/mm')
m.plot()