import matplotlib.pyplot as plt

# 定义饼图的标签和对应的数据
labels = ['A', 'B', 'C', 'D']
sizes = [30, 20, 15, 35]

# 绘制饼形图
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# 添加标题
plt.title('Pie Chart')

# 显示图形
plt.show()