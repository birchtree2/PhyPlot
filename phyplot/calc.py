import numpy as np

def relative_error(actual_value, measured_value, echo=True):
    relative_error = np.abs((actual_value - measured_value) / actual_value)
    if(echo):
         print(f"真实值={actual_value} 测量值={measured_value} 误差: {relative_error:.2%}")
    return relative_error

def type_a_uncertainty(values): #A类不确定度
    mean = np.mean(values) #均值
    std = np.std(values, ddof=1) #标准差
    return std/np.sqrt(len(values))

def type_b_uncertainty(limits): #B类不确定度
    return limits/np.sqrt(3)

def uncertainty(values, limits):
    return np.sqrt(type_a_uncertainty(values)**2 + type_b_uncertainty(limits)**2)