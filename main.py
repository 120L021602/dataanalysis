# 这是一个为了外专业课程《地方政府治理与城市发展》小组项目所写的程序
# 程序的主要功能是处理从问卷星收集到的数据，并分析

import pandas as pd
import statistics

from matplotlib import pyplot as plt
from scipy import stats
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import f_oneway
from pylab import mpl

# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimSun"]
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False

# plt.rcParams['font.sans-serif']=['SimHei']

# 从excel表格中导入数据
df = pd.read_excel('../data(按序号).xlsx', sheet_name='Sheet1')

# 获取第一列性别数据
gender_list = df.iloc[:, 6]
# print(gender_list)

# 获取了解程度列表
understanding_level_list = df.iloc[:, 14]
# print(understanding_level_list)

# 获取院校列表
college_list = df.iloc[:, 8]
# print(college_list)

# 获取党员信息列表
political_status_list = df.iloc[:, 9]
# print(political_status_list)

# 获取户籍所在地信息列表
place_of_domicile_list = df.iloc[:, 10]
# print(place_of_domicile_list)

# 获取最希望就业的城市信息
best_location = df.iloc[:, 13]
# print(best_location)

# 获取专业列表
major_list = df.iloc[:, 7]
# print(major_list)

# 获取人才政策影响列表
talent_policy_list = df.iloc[:, 22]
print(talent_policy_list)


# print(df)


# 求平均数
def average(lst):
    return sum(lst) / len(lst)


# 人才政策是否会影响就业城市的选择
def talent_policy_affects_employment_city():
    positive_num = 0
    negative_num = 0

    for judgement in talent_policy_list:
        if judgement == 1:
            positive_num += 1
        if judgement == 2:
            negative_num += 1

    # 绘制饼形图
    labels = ['会', '不会']
    sizes = [positive_num, negative_num]
    title = '人才政策是否会影响就业城市的选择'
    draw_pie_chart(labels, sizes, title)


# 样本基本描述
def sample_basic_description():
    category = ['男', '女', '哲学', '经济学', '法学', '教育学', '文学', '历史学', '理学', '工学', '农学',
                '医学', '管理学', '军事学', '艺术学', '一般院校', '重点院校', '外国院校', '中共党员（含预备党员）',
                '非中共党员', '城镇', '农村']
    num_list = []
    ratio_list = []

    # 性别
    num_of_male = 0
    num_of_female = 0

    for gender in gender_list:
        if gender == 1:
            num_of_male += 1
        else:
            num_of_female += 1

    num_list.append(num_of_male)
    num_list.append(num_of_female)

    ratio_of_male = "{:.1%}".format(num_of_male / len(gender_list))
    ratio_of_female = "{:.1%}".format(num_of_female / len(gender_list))
    ratio_list.append(ratio_of_male)
    ratio_list.append(ratio_of_female)

    # 专业
    num_of_philosophy = 0
    num_of_economics = 0
    num_of_law = 0
    num_of_education = 0
    num_of_literature = 0
    num_of_history = 0
    num_of_science = 0
    num_of_engineering = 0
    num_of_agronomy = 0
    num_of_medicine = 0
    num_of_management = 0
    num_of_military = 0
    num_of_art = 0

    for major in major_list:
        if major == 1:
            num_of_philosophy += 1
        if major == 2:
            num_of_economics += 1
        if major == 3:
            num_of_law += 1
        if major == 4:
            num_of_education += 1
        if major == 5:
            num_of_literature += 1
        if major == 6:
            num_of_history += 1
        if major == 7:
            num_of_science += 1
        if major == 8:
            num_of_engineering += 1
        if major == 9:
            num_of_agronomy += 1
        if major == 10:
            num_of_medicine += 1
        if major == 11:
            num_of_management += 1
        if major == 12:
            num_of_military += 1
        if major == 13:
            num_of_art += 1

    num_list.append(num_of_philosophy)
    num_list.append(num_of_economics)
    num_list.append(num_of_law)
    num_list.append(num_of_education)
    num_list.append(num_of_literature)
    num_list.append(num_of_history)
    num_list.append(num_of_science)
    num_list.append(num_of_engineering)
    num_list.append(num_of_agronomy)
    num_list.append(num_of_medicine)
    num_list.append(num_of_management)
    num_list.append(num_of_military)
    num_list.append(num_of_art)

    ratio_of_philosophy = "{:.1%}".format(num_of_philosophy / len(gender_list))
    ratio_of_economics = "{:.1%}".format(num_of_economics / len(gender_list))
    ratio_of_law = "{:.1%}".format(num_of_law / len(gender_list))
    ratio_of_education = "{:.1%}".format(num_of_education / len(gender_list))
    ratio_of_literature = "{:.1%}".format(num_of_literature / len(gender_list))
    ratio_of_history = "{:.1%}".format(num_of_history / len(gender_list))
    ratio_of_science = "{:.1%}".format(num_of_science / len(gender_list))
    ratio_of_engineering = "{:.1%}".format(num_of_engineering / len(gender_list))
    ratio_of_agronomy = "{:.1%}".format(num_of_agronomy / len(gender_list))
    ratio_of_medicine = "{:.1%}".format(num_of_medicine / len(gender_list))
    ratio_of_management = "{:.1%}".format(num_of_management / len(gender_list))
    ratio_of_military = "{:.1%}".format(num_of_military / len(gender_list))
    ratio_of_art = "{:.1%}".format(num_of_art / len(gender_list))
    ratio_list.append(ratio_of_philosophy)
    ratio_list.append(ratio_of_economics)
    ratio_list.append(ratio_of_law)
    ratio_list.append(ratio_of_education)
    ratio_list.append(ratio_of_literature)
    ratio_list.append(ratio_of_history)
    ratio_list.append(ratio_of_science)
    ratio_list.append(ratio_of_engineering)
    ratio_list.append(ratio_of_agronomy)
    ratio_list.append(ratio_of_medicine)
    ratio_list.append(ratio_of_management)
    ratio_list.append(ratio_of_military)
    ratio_list.append(ratio_of_art)

    # 院校
    num_of_normal_college = 0
    num_of_key_college = 0
    num_of_foreign_college = 0

    for college in college_list:
        if college == 1 or college == 2:
            num_of_normal_college += 1
        if college == 3 or college == 4:
            num_of_key_college += 1
        else:
            num_of_foreign_college += 1

    num_list.append(num_of_normal_college)
    num_list.append(num_of_key_college)
    num_list.append(num_of_foreign_college)

    ratio_of_normal_college = "{:.1%}".format(num_of_normal_college / len(gender_list))
    ratio_of_key_college = "{:.1%}".format(num_of_key_college / len(gender_list))
    ratio_of_foreign_college = "{:.1%}".format(num_of_foreign_college / len(gender_list))
    ratio_list.append(ratio_of_normal_college)
    ratio_list.append(ratio_of_key_college)
    ratio_list.append(ratio_of_foreign_college)

    # 政治面貌
    num_of_communist = 0
    num_of_non_communist = 0

    for political_status in political_status_list:
        if political_status == 1:
            num_of_communist += 1
        else:
            num_of_non_communist += 1

    num_list.append(num_of_communist)
    num_list.append(num_of_non_communist)

    ratio_of_communist = "{:.1%}".format(num_of_communist / len(gender_list))
    ratio_of_non_communist = "{:.1%}".format(num_of_non_communist / len(gender_list))
    ratio_list.append(ratio_of_communist)
    ratio_list.append(ratio_of_non_communist)

    # 户籍所在地
    num_of_city_and_town = 0
    num_of_country = 0

    for place in place_of_domicile_list:
        if place == 1 or place == 2:
            num_of_city_and_town += 1
        else:
            num_of_country += 1

    num_list.append(num_of_city_and_town)
    num_list.append(num_of_country)

    ratio_of_city_and_town = "{:.1%}".format(num_of_city_and_town / len(gender_list))
    ratio_of_country = "{:.1%}".format(num_of_country / len(gender_list))
    ratio_list.append(ratio_of_city_and_town)
    ratio_list.append(ratio_of_country)

    # 输出表格
    data = {'类别': category, '人数': num_list, '百分比': ratio_list}
    df_data = pd.DataFrame(data)
    df_data.to_excel('../output/sample_basic_description_output.xlsx', index=False)


# 高校毕业生对地方人才政策了解情况的基本描述
def understanding_level_general():
    min_value = min(understanding_level_list)
    max_value = max(understanding_level_list)
    mean_value = average(understanding_level_list)
    std_dev = statistics.stdev(understanding_level_list)
    total_number = len(understanding_level_list)

    # 打印结果
    print("最小值为:", min_value)
    print("最大值为:", max_value)
    print("平均数为:", mean_value)
    print("标准差为:", std_dev)
    print("样本数为:", total_number)
    min_list = [min_value]
    max_list = [max_value]
    mean_value_list = [mean_value]
    std_dev_list = [std_dev]
    total_number_list = [total_number]

    # 创建DataFrame对象
    data = {'最小值': min_list, '最大值': max_list, '平均数': mean_value_list,
            '标准差': std_dev_list, '样本数': total_number_list}
    df_data = pd.DataFrame(data)

    # 导出DataFrame到excel文件
    df_data.to_excel('../output/understanding_level_output.xlsx', index=False)

    # 了解情况
    know_nothing_num = 0
    not_know_enough_num = 0
    general_num = 0
    know_well_num = 0
    know_very_well_num = 0

    for understanding_level in understanding_level_list:
        if understanding_level == 1:
            know_nothing_num += 1
        if understanding_level == 2:
            not_know_enough_num += 1
        if understanding_level == 3:
            general_num += 1
        if understanding_level == 4:
            know_well_num += 1
        else:
            know_very_well_num += 1

        know_nothing_ratio = '{:.1%}'.format(know_nothing_num / len(gender_list))
        not_know_enough_ratio = '{:.1%}'.format(not_know_enough_num / len(gender_list))
        general_ratio = '{:.1%}'.format(general_num / len(gender_list))
        know_well_ratio = '{:.1%}'.format(know_well_num / len(gender_list))
        know_very_well_ratio = '{:.1%}'.format(know_very_well_num / len(gender_list))

        # 创建DataFrame对象
        data = {'完全不了解': [know_nothing_num, know_nothing_ratio],
                '不太了解': [not_know_enough_num, not_know_enough_ratio],
                '一般': [general_num, general_ratio], '比较了解': [know_well_num, know_well_ratio],
                '非常了解': [know_very_well_num, know_very_well_ratio]}
        df_data = pd.DataFrame(data)

        # 导出DataFrame到excel文件
        df_data.to_excel('../output/understanding_level_output2.xlsx', index=False)


# 高校毕业生就业城市选择情况的基本描述
def choice_of_employment_city_general():
    category = ['直辖市城市', '省会城市', '非省会的地级市', '县城或乡镇', '合计']

    # 频数
    num_of_direct_controlled_municipality = 0
    num_of_provincial_capital = 0
    num_of_prefecture_city = 0
    num_of_county_or_village_and_town = 0

    for location in best_location:
        if location == 1:
            num_of_direct_controlled_municipality += 1
        if location == 2:
            num_of_provincial_capital += 1
        if location == 3:
            num_of_prefecture_city += 1
        if location == 4:
            num_of_county_or_village_and_town += 1

    sum = num_of_direct_controlled_municipality + num_of_provincial_capital + num_of_prefecture_city + num_of_county_or_village_and_town

    ratio_of_direct_controlled_municipality = "{:.1%}".format(num_of_direct_controlled_municipality / sum)
    ratio_of_provincial_capital = "{:.1%}".format(num_of_provincial_capital / sum)
    ratio_of_prefecture_city = "{:.1%}".format(num_of_prefecture_city / sum)
    ratio_of_county_or_village_and_town = "{:.1%}".format(num_of_county_or_village_and_town / sum)

    data = {'就业城市类型': category, '频数': [num_of_direct_controlled_municipality,
                                               num_of_provincial_capital, num_of_prefecture_city,
                                               num_of_county_or_village_and_town, sum],
            '百分比': [ratio_of_direct_controlled_municipality, ratio_of_provincial_capital,
                       ratio_of_prefecture_city, ratio_of_county_or_village_and_town, '100%'],
            '累积百分比': [ratio_of_direct_controlled_municipality,
                           "{:.1%}".format(
                               (num_of_direct_controlled_municipality / sum) + (num_of_provincial_capital / sum)),
                           "{:.1%}".format(
                               (num_of_direct_controlled_municipality / sum) + (num_of_provincial_capital / sum) + (
                                       num_of_prefecture_city / sum)),
                           "{:.1%}".format(
                               (num_of_direct_controlled_municipality / sum) + (num_of_provincial_capital / sum) + (
                                       num_of_prefecture_city / sum) +
                               (num_of_county_or_village_and_town / sum)), '']}
    df_data = pd.DataFrame(data)
    df_data.to_excel('../output/choice_of_employment_city_output.xlsx', index=False)

    # 绘制饼形图
    labels = ['直辖市城市', '省会城市', '非省会的地级市', '县城或乡镇']
    sizes = [num_of_direct_controlled_municipality, num_of_provincial_capital, num_of_prefecture_city,
             num_of_county_or_village_and_town]
    draw_pie_chart(labels, sizes, '高校毕业生的就业城市选择饼形图')


# 性别差异分析
def gender_analysis(data_list, module):
    category = ["男", "女"]
    male_list = []
    female_list = []
    for i in range(len(gender_list)):
        if gender_list[i] == 1:
            male_list.append(float(data_list[i]))
        if gender_list[i] == 2:
            female_list.append(float(data_list[i]))

    male_avg = average(male_list)
    female_avg = average(female_list)
    male_stddev_value = np.std(male_list)
    female_stddev_value = np.std(female_list)

    # 计算t和p值
    t_statistics, p_value = stats.ttest_ind(male_list, female_list)

    # 打印结果
    print("男平均数:", male_avg)
    print("女平均数:", female_avg)
    print("男标准差:", male_stddev_value)
    print("女标准差:", female_stddev_value)
    print("t值:", t_statistics, "p值:", p_value)

    # 输出表格
    data = {'分组': category, '平均数': [male_avg, female_avg], '标准差': [male_stddev_value, female_stddev_value],
            't': t_statistics, 'p': p_value}
    df_data = pd.DataFrame(data)
    df_data.to_excel('../output/' + module + '_gender_output.xlsx', index=False)


# 专业类别分析
# def major_analysis():


# 学校类别分析
def college_analysis_using_lsd(data_list, module):
    category = ['一般院校', '重点院校', '国外院校']
    normal_college_list = []
    key_college_list = []
    foreign_college_list = []
    for i in range(len(gender_list)):
        if college_list[i] == 1 or college_list[i] == 2:
            normal_college_list.append(data_list[i])
        if college_list[i] == 3 or college_list[i] == 4:
            key_college_list.append(data_list[i])
        else:
            foreign_college_list.append(data_list[i])

    normal_college_avg = average(normal_college_list)
    key_college_avg = average(key_college_list)
    foreign_college_avg = average(foreign_college_list)
    normal_college_stddev = np.std(normal_college_list)
    key_college_stddev = np.std(key_college_list)
    foreign_college_stddev = np.std(foreign_college_list)

    # 打印结果
    print("一般院校平均值:", normal_college_avg)
    print("重点院校平均值:", key_college_avg)
    print("外国院校平均值:", foreign_college_avg)
    print("一般院校标准差:", normal_college_stddev)
    print("重点院校标准差:", key_college_stddev)
    print("外国院校标准差:", foreign_college_stddev)

    data = pd.DataFrame({
        'Group': ['一般院校', '重点院校', '国外院校'],
        'Value': [
            normal_college_list,
            key_college_list,
            foreign_college_list
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

    # 打印方差分析结果
    print("ANOVA结果：")
    print(anova_table)

    # 打印LSD方法多重比较结果
    print("LSD方法多重比较结果：")
    print(posthoc)

    # 输出表格
    data = {'F': [f_stat], 'P': [p_value]}
    df_data = pd.DataFrame(data)
    df_data.to_excel('../output/' + module + '_college_output.xlsx', index=False)


# 政治面貌分析
def political_status_analysis(data_list, module):
    category = ['中共党员(含预备党员)', '非中共党员']
    communist_list = []
    non_communist_list = []
    for i in range(len(gender_list)):
        if political_status_list[i] == 1:
            communist_list.append(data_list[i])
        else:
            non_communist_list.append(data_list[i])

    communist_avg = average(communist_list)
    non_communist_avg = average(non_communist_list)
    communist_stddev = np.std(communist_list)
    non_communist_stddev = np.std(non_communist_list)
    t_statistics, p_value = stats.ttest_ind(communist_list, non_communist_list)

    # 打印结果
    print("中共党员(含预备党员)平均数:", communist_avg)
    print("非中共党员平均数:", non_communist_avg)
    print("中共党员(含预备党员)标准差:", communist_stddev)
    print("非中共党员标准差:", np.std(non_communist_list))
    print("t值:", t_statistics)
    print("p值:", p_value)

    # 输出表格
    data = {'分组': category, '平均数': [communist_avg, non_communist_avg],
            '标准差': [communist_stddev, non_communist_stddev],
            't': t_statistics, 'p': p_value}
    df_data = pd.DataFrame(data)
    df_data.to_excel('../output/' + module + '_political_status_output.xlsx', index=False)


# 户籍所在地分析
def place_of_domicile_analysis(data_list, module):
    category = ['城镇', '农村']
    city_and_town_list = []
    country_list = []
    for i in range(len(gender_list)):
        if place_of_domicile_list[i] == 1 or place_of_domicile_list[i] == 2:
            city_and_town_list.append(data_list[i])
        else:
            country_list.append(data_list[i])

    city_and_town_avg = average(city_and_town_list)
    country_avg = average(country_list)
    city_and_town_stddev = np.std(city_and_town_list)
    country_stddev = np.std(country_list)
    t_statistics, p_value = stats.ttest_ind(city_and_town_list, country_list)

    print("城镇平均数:", city_and_town_avg)
    print("农村平均数:", country_avg)
    print("城市标准差:", city_and_town_stddev)
    print("农村标准差:", country_stddev)
    print("t值:", t_statistics)
    print("p值:", p_value)

    data = {'分组': category, '平均数': [city_and_town_avg, country_avg],
            '标准差': [city_and_town_stddev, country_stddev],
            't': t_statistics, 'p': p_value}
    df_data = pd.DataFrame(data)
    df_data.to_excel('../output/' + module + '_place_of_domicile_output.xlsx', index=False)


# 专业类别差异的分析
def major_analysis_using_lsd(data_list, module):
    major_of_philosophy = []
    major_of_economics = []
    major_of_law = []
    major_of_education = []
    major_of_literature = []
    major_of_history = []
    major_of_science = []
    major_of_engineering = []
    major_of_agronomy = []
    major_of_medicine = []
    major_of_management = []
    major_of_military = []
    major_of_art = []

    for i in range(len(gender_list)):
        if major_list[i] == 1:
            major_of_philosophy.append(data_list[i])
        if major_list[i] == 2:
            major_of_economics.append(data_list[i])
        if major_list[i] == 3:
            major_of_law.append(data_list[i])
        if major_list[i] == 4:
            major_of_education.append(data_list[i])
        if major_list[i] == 5:
            major_of_literature.append(data_list[i])
        if major_list[i] == 6:
            major_of_history.append(data_list[i])
        if major_list[i] == 7:
            major_of_science.append(data_list[i])
        if major_list[i] == 8:
            major_of_engineering.append(data_list[i])
        if major_list[i] == 9:
            major_of_agronomy.append(data_list[i])
        if major_list[i] == 10:
            major_of_medicine.append(data_list[i])
        if major_list[i] == 11:
            major_of_management.append(data_list[i])
        if major_list[i] == 12:
            major_of_military.append(data_list[i])
        if major_list[i] == 13:
            major_of_art.append(data_list[i])

    # 假设有一个DataFrame对象，其中包含组别和对应的观测值
    data = pd.DataFrame({
        'Group': ['philosophy', 'economics', 'law', 'education', 'literature', 'history', 'science',
                  'engineering', 'agronomy', 'medicine', 'management', 'military', 'art'],
        'Value': [major_of_philosophy, major_of_economics, major_of_law, major_of_education,
                  major_of_literature, major_of_history, major_of_science, major_of_engineering,
                  major_of_agronomy, major_of_medicine, major_of_management, major_of_military, major_of_art]
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

    # 打印方差分析结果
    print("ANOVA结果：")
    print(anova_table)

    # 打印LSD方法多重比较结果
    print("LSD方法多重比较结果：")
    print(posthoc)

    data = {'F': [f_stat], 'P': [p_value]}
    df_data = pd.DataFrame(data)
    df_data.to_excel('../output/' + module + '_major_analysis_using_lsd_output.xlsx', index=False)


# 画饼形图
def draw_pie_chart(labels, sizes, title):
    # 绘制饼形图
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')

    # 添加标题
    plt.title(title)

    # plt.rcParams['font.sans-serif'] = ['SimHei']

    # 显示图形
    plt.show()

    # 导出图像为png文件
    # plt.savefig('../output/' + 'pie_chart' + '.png')


if __name__ == "__main__":
    # 人才政策是否会影响就业城市的选择
    # talent_policy_affects_employment_city()

    # 样本基本描述
    # sample_basic_description()

    # 高校毕业生对人才政策了解的描述及差异分析
    # understanding_level_general()
    # gender_analysis(understanding_level_list, "understanding_level")
    college_analysis_using_lsd(understanding_level_list, "understanding_level")
    # political_status_analysis(understanding_level_list, "understanding_level")

    # 高校毕业生就业城市选择的描述及差异分析
    # choice_of_employment_city_general()
    college_analysis_using_lsd(best_location, "employment_city")
    # political_status_analysis(best_location, "employment_city")
    # place_of_domicile_analysis(best_location, "employment_city")
    major_analysis_using_lsd(best_location, "employment_city")
