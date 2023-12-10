import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# 假设有一个DataFrame对象，其中包含组别和对应的观测值
data = pd.DataFrame({
    'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [10, 12, 8, 9, 15, 13]
})

# 执行方差分析（ANOVA）
model = sm.formula.ols('Value ~ Group', data=data).fit()
anova_table = sm.stats.anova_lm(model)

# 提取组别之间的显著差异
posthoc = pairwise_tukeyhsd(data['Value'], data['Group'])

# 打印方差分析结果
print("ANOVA结果：")
print(anova_table)

# 打印LSD法多重比较结果
print("LSD法多重比较结果：")
print(posthoc)