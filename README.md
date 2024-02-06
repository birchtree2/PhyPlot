# phyplot

`phyplot` is a simple Python package for data visualization with matplotlib.

## 安装

Clone this repository and then run:

```bash
pip install .
```

## 使用说明

### `MyPlot`类

`MyPlot` 是 PhyPlot 库的核心类，用于创建绘图对象并进行数据可视化。

#### 初始化方法 `__init__`

```python
def __init__(self, data: Dict[str, List[float]], x_label: str = None, filename: str ='.png'):
```

- **功能**: 初始化绘图对象。
- 参数
    - `data`: 字典类型，键为字符串表示的变量名（带单位），值为浮点数列表，表示对应变量的数据序列。 变量名的格式为`符号/单位`，且最多只能包含一个`/`
    - `x_label`: 字符串类型，指定作为 x 轴的变量名。如果为 `None`，默认使用 `data` 字典中的第一个键。
    - `filename`: 字符串类型，指定保存图表和表格的文件名前缀。

例子`/demo/demo.py`:

```python
from phyplot import plot
x=[4,8,12,16,20]
y=[1.2,1.35,1.45,1.56,1.77]
z=[3,4,5,6,7]
fig=plot.MyPlot({'x/mm':x,'U1/V':y,'U2/V':z})
fig.plot_table()
fig.plot_fig()
#x作为横轴, y,z分别是两个画在纵轴的变量
```

执行`python demo.py`后，图片会保存在当前目录下:

效果如图所示

![](https://s2.loli.net/2024/02/06/X3b7WYukghDANVZ.png)



![](https://s2.loli.net/2024/02/06/aZ3co8ORMz6kEtf.png)

#### 方法 `plot_table`

```python
def plot_table(self) -> None:
```

- **功能**: 绘制并保存包含实验数据的表格。
- **无需参数**。

#### 方法 `plot_fig`

```python
def plot_fig(self, fit_deg: int = 1, show_coordinate: bool = False):
```

- **功能**: 绘制散点图和拟合曲线，并保存图像。同时可返回回归结果便于后续计算

- 参数

    - `fit_deg`: 整型，指定拟合曲线的多项式度数。默认为 1，即线性拟合。
    - `show_coordinate`: 布尔型，是否在每个数据点旁显示坐标。默认为 `False`。

- 返回值:

    - 当`fit_deg=1`时，会返回两个列表`slope`,`intercept`. 列表中分别是每个拟合变量对应拟合直线的斜率和截距

    例:

    ```python
    t = [22.5,30.9,33.9,38.1,43.0,47.5,52.3,58.1,62.0,67.3]
    R = [55.20,56.99,57.65,58.55,59.60,60.56,61.62,62.84,63.68,64.83]
    plt3=plot.MyPlot({'t/°C':t,'R/Ω':R},filename="Cu50 电阻 R-t 特性曲线")
    k,b=plt3.plot_fig() #k是斜率列表,b是截距列表。 
    #因为拟合变量只有一个R，所以列表中只有一个元素
    #所求变量可用斜率除以截距表示，即k[0]/b[0]
    print(f'alpha={k[0]/b[0]}')
    calc.relative_error(alpha_expect,k[0]/b[0])
    ```

    

#### 方法 `plot`

```python
def plot(self, fit_deg: int = 1, show_coordinate: bool = False):
```

- **功能**: 综合 `plot_table` 和 `plot_fig` 方法，绘制并保存数据表格和图像。
- 参数
    - `fit_deg`: 整型，指定拟合曲线的多项式度数。默认为 1，即线性拟合。
    - `show_coordinate`: 布尔型，是否在每个数据点旁显示坐标。默认为 `False`。

### 辅助函数

#### 函数 `relative_error`

```python
def relative_error(actual_value, measured_value, echo=True):
```

- **功能**: 计算并打印真实值与测量值之间的相对误差。
- 参数
    - `actual_value`: 真实值。
    - `measured_value`: 测量值。
    - `echo`: 是否打印误差信息。默认为 `True`。

#### 函数 `type_a_uncertainty`

```python
def type_a_uncertainty(values):
```

- **功能**: 计算 A 类不确定度（样本标准偏差的估计）。

- 参数

    :

    - `values`: 数据值列表。

#### 函数 `type_b_uncertainty`

```python
def type_b_uncertainty(limits):
```

- **功能**: 计算 B 类不确定度（基于测量仪器精度的估计）。
- 参数
    - `limits`: 测量限度。

#### 函数 `uncertainty`

```python
def uncertainty(values, limits):
```

- **功能**: 计算总不确定度，结合 A 类和 B 类不确定度。
- 参数
    - `values`: 数据值列表。
    - `limits`: 测量限度。
