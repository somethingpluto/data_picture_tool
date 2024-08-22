import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# 设置 Matplotlib 字体为 Times New Roman
mpl.rcParams['font.family'] = 'Times New Roman'

# 读取CSV文件
data = pd.read_csv('./llm_count.csv')  # 确保文件名和路径正确

# 生成包含值的标签
labels = ['{}, {}'.format(label, value) for label, value in zip(data['Word'], data['Count'])]

# 自定义百分比显示格式，设置百分比字体大小
def custom_autopct(pct):
    return ('{:.1f}%'.format(pct)) if pct >= 1 else ''

# 绘制饼图
plt.figure(figsize=(8, 8))  # 设置画布大小
plt.pie(data['Count'], labels=labels, autopct=custom_autopct, startangle=140,
        textprops={'fontsize': 19})  # 设置标签字体大小
plt.axis('equal')  # 保持饼图为圆形

# 保存图表
plt.savefig('./pie_chart.png', bbox_inches='tight')  # 自动裁剪边缘，并保存为PNG文件

# 关闭图表显示，避免内存泄漏
plt.close()
