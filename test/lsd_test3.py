import numpy as np
import pandas as pd
from scipy.stats import f_oneway
import statsmodels.api as sm
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# 假设有一个DataFrame对象，其中包含组别和对应的观测值
data = pd.DataFrame({
    'Group': ['A', 'B', 'C', 'D', 'E'],
    'Value': [
        [10, 12, 8],
        [9, 11, 13, 15],
        [14, 9, 12, 10, 11],
        [13, 16, 14],
        [8, 9, 12, 10, 11, 13, 16, 14]
    ]
})

# 执行方差分析（ANOVA）
f_stat, p_value = f_oneway(*data['Value'])
anova_table = pd.DataFrame({'F-Statistic': f_stat, 'p-value': p_value}, index=['ANOVA'])

# 将数据展开为一维数组
all_values = np.concatenate(data['Value'].values)

# 生成组别标签
group_labels = np.repeat(data['Group'], [len(values) for values in data['Value']])

# 执行LSD方法的多重比较
posthoc = pairwise_tukeyhsd(all_values, group_labels)

# 将结果保存到Excel表格
with pd.ExcelWriter('lsd_analysis_results.xlsx') as writer:
    anova_table.to_excel(writer, sheet_name='ANOVA', index=False)
    posthoc.summary().tables[1].to_excel(writer, sheet_name='LSD Method', index=False)