import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
from typing import Dict, List
from matplotlib.ticker import FormatStrFormatter
class MyPlot:

    def __init__(self, 
        data: Dict[str, List[float]], 
        x_label: str = None,
        filename: str ='.png'
    ):
        self.data = data
        if x_label is None:
            self.x_label = list(data.keys())[0] # 默认取第一个作为x轴
        else:
            self.x_label = x_label
        self.filename=filename
    
    def split_label(self, label: str) -> str:
        return label.split('/')
    
    def plot_table(self) -> None:
        # 设置图表大小
        fig, ax = plt.subplots(figsize=(len(self.data)*1.8, len(self.data[self.x_label])*0.4))
        
        # 创建表格数据
        table_data = {'序号': np.arange(len(self.data[self.x_label]))+1}
        table_data.update(self.data)

        plt.rc("font", family="SimSun", size=13, weight="bold")
        ax.axis('off')  # 关闭坐标轴
        #ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
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
        plt.savefig('table_'+self.filename)

    def     plot_fig(self, fit_deg: int = 1 ,show_coordinate:bool=False):
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
        slope=[]
        intercept=[]
        colors = ['blue','orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']  
        if fit_deg == 1:
            for i, (label, values) in enumerate(self.data.items()): #enumerate
                if label != self.x_label:
                    # print(label)
                    # 计算线性回归的多项式系数
                    coefficients = np.polyfit(self.data[self.x_label],values,fit_deg) 
                    poly = np.poly1d(coefficients)
                    var,unit=self.split_label(label) #分离变量名和单位
                    equation= f"{var}={coefficients[0]:.2f}*x+{coefficients[1]:.2f} ({unit})"
                    print(f"回归结果: {var}={coefficients[0]:.2f}*x+{coefficients[1]:.2f} ({unit})")
                    lx=np.arange(min(self.data[self.x_label]),max(self.data[self.x_label])+0.2,step=0.1) 
                    #画曲线的点要更多
                    ax.plot(lx, poly(lx), color=colors[i % len(colors)], label=equation)
                    #不同变量对应颜色
                    slope.append(coefficients[0])
                    intercept.append(coefficients[1])
        else: #画平滑曲线
            for label, values in self.data.items():
                if label != self.x_label:
                    m = make_interp_spline(self.data[self.x_label], values)
                    xs = np.linspace(min(self.data[self.x_label]),max(self.data[self.x_label]), 500)
                    ys = m(xs)
                    plt.plot(xs, ys)

        # 设置图表标题和坐标轴标签
        ax.set_xlabel(self.x_label)
        ax.legend()
        if len(self.data)>2 :
            var,unit=self.split_label(list(self.data.keys())[1])
            ax.set_ylabel(f'{var[0]}/{unit}')
        else:
            var,unit=self.split_label(list(self.data.keys())[1])
            ax.set_ylabel(f'{var}/{unit}')
        # 保存图表
        plt.savefig('figure_'+self.filename)
        return slope,intercept

    def plot(self, fit_deg: int = 1, show_coordinate:bool=False):
        self.plot_table()
        return self.plot_fig(fit_deg,show_coordinate)

