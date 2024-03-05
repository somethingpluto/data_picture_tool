# 详细文档
[Attention Required! | Cloudflare](https://www.statisticshowto.com/probability-and-statistics/statistics-definitions/wilcoxon-signed-rank-test/)
# 介绍
Wilcoxon signed-rank test（Wilcoxon符号秩检验）是一种非参数统计检验方法，用于比较两个相关样本的中位数是否存在显著差异。它适用于非正态分布或有序分类数据。
Wilcoxon符号秩检验的基本原理是将两个相关样本的差异值（差异 = 第一个样本 - 第二个样本）按照绝对值大小进行排序，并计算排序后的差异值的秩次。然后，根据秩次的总和来判断两个样本的差异是否显著。
Wilcoxon符号秩检验有两种形式：

1. 单样本Wilcoxon符号秩检验：用于比较一个样本的中位数是否与一个已知的的值相等
2. 配对样本Wilcoxon符号秩检验：用于比较两个相关样本的中位数是否存在显著的差异

通过比较检验结果中的P值，可以判断两个样本的中位数是否存在显著差异。如果p值小于显著水平(通常为0.05)，则可以拒绝零假设，认为两个样本的中位数存在显著的差异。
# 作用
 Wilcoxon检验的部分作用如下：

1. 比较两个相关样本的中位数差异
2. 比较两个独立样本的中位数差异
3. 非参数假设检验：wilcoxon检验是一种分参数统计的校验方法，不依赖与数据的具体分布形式，适用于不满足正态分布假设的情况，或者对数据分布了解不充分的情况
4. 数据分析，wilcoxon可以帮助发现样本之间的差异，并提供关于这些信息的差异性统计信息。
> 简而言之，wilcoxon可以帮助我们在不清楚数据的分布情况下，比较不同样本之间的差异性，便于后续的进一步分析。

# 使用说明
## 代码目录
路径：data_picture_tool/wilcoxon/wilcoxon.py
![image.png](https://cdn.nlark.com/yuque/0/2024/png/23003149/1709562394390-8a1d97e6-eb5a-4f16-9a14-b9e578514998.png#averageHue=%23ede6d1&clientId=u457e0e36-72ce-4&from=paste&height=163&id=u5a67b14f&originHeight=125&originWidth=328&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=6615&status=done&style=none&taskId=u755e7232-3c9e-4a0c-b7d5-f1529e14652&title=&width=428.3999938964844)
output：wilcoxon计算结果
test_data: 测试数据，在配置文件中可修改为实验数据存放目录，该目录中，仅能存放metric数据，后面配置文件中会详细说明。
wilcoxon.py：源文件
wilcoxon_config.yaml：运行配置文件
## 数据格式准备
> 现假设场景如下：需要在比较多个不同数据集下，不同方法计算所得到的数据值，之间的差异性。
> precision.xlsx
> ![image.png](https://cdn.nlark.com/yuque/0/2024/png/23003149/1709562715173-e937ae6c-bd73-42a1-b615-33e86df4b870.png#averageHue=%23f9f9f9&clientId=u457e0e36-72ce-4&from=paste&height=182&id=gyIol&originHeight=228&originWidth=865&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=71056&status=done&style=none&taskId=u4bd88c8f-30fa-4c4b-a083-d7d3ea03eb1&title=&width=692)
> A为基础方法，也可以称之为baseline方法
> B-I 为需要对比的方法
> set1 - set11 为11个不同的数据集，
> 而中间的值，便是每个方法在该数据集上计算得出的precision

## 配置文件
```yaml
# 表头出现的所有方法
method_list:
  - Kmedoids.LOC
  - KmeansPlus.LOC
  - Cure.LOC
  - ManualUp
  - EALR
  - EATT
  - CBS+
# baseline 方法列表
base_line_list:
  - Kmedoids.LOC
  - KmeansPlus.LOC
  - Cure.LOC

# metric指标列表
metrics:
  - IFA
  - PofB
  - PMI
  - Recallx

# xlsx数据存放位置 xlsx文件命名规则为 为 metric.xlsx
data_path: ./test_data
```
### data_path
配置文件中的data_path字段，即为数据文件存放目录。如果wilcoxon_config.yaml文件和wilcoxon.py文件在同一目录下，则可以使用相对路径，如果不在请使用绝对路径。
### metrics
现在，假设需要比较IFA，PMI，PofB，Recallx 四个指标，数据文件夹下应该存放，一下四个xlsx文件，且命名规则为  IFA.xlsx,PMI.xlsx,PofB.xlsx,Recallx.xlsx。
![image.png](https://cdn.nlark.com/yuque/0/2024/png/23003149/1709563024825-819572a5-a203-4975-9a03-1d99bd494bde.png#averageHue=%23eae5ce&clientId=u457e0e36-72ce-4&from=paste&height=146&id=ufaac7980&originHeight=120&originWidth=311&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=4423&status=done&style=none&taskId=uc804bb8d-f812-423c-82ab-587e4b092c3&title=&width=377.8000030517578)
IFA，PMI，PofB，Recallx，对应着配置文件中的metrics数组
### method_list
IFA文件内容截图如下：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/23003149/1709563158613-6ff379cb-b1a0-449c-8203-72c97fab7421.png#averageHue=%23f5f2f0&clientId=u457e0e36-72ce-4&from=paste&height=203&id=uace0d355&originHeight=254&originWidth=812&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=24313&status=done&style=none&taskId=u523f51f6-4403-4347-8a7f-c0109efa3e1&title=&width=649.6)
从Kmedoids.LOC 到 CBS+，即为本次实验中的所有方法，对应着配置文件中的method_list数组。
### baseline
假设选择了了 Kmedoids.LOC，KmeansPlus.LOC，Cure.LOC三个基准方法作为比较方法，对应着配置文件中base_line_list数组。
## 结果输出
结果默认输出到，运行目录中的output文件夹。
![image.png](https://cdn.nlark.com/yuque/0/2024/png/23003149/1709563475956-378d382b-2793-4bae-b2c3-ad69150229dc.png#averageHue=%23ece6d0&clientId=u457e0e36-72ce-4&from=paste&height=338&id=uadb66c00&originHeight=423&originWidth=298&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=14289&status=done&style=none&taskId=ud73ad685-47d9-44dd-9278-50acc6aaee3&title=&width=238.4)
![image.png](https://cdn.nlark.com/yuque/0/2024/png/23003149/1709563519440-f1ac8597-ba9d-481c-8ec3-780283ff82d3.png#averageHue=%23f9f2de&clientId=u457e0e36-72ce-4&from=paste&height=55&id=u6d5f7b59&originHeight=69&originWidth=1335&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=9224&status=done&style=none&taskId=u071425f3-c05b-494f-b8ff-2f4f98d5335&title=&width=1068)
结果保存为各baseline的csv，即baseline方法与其他所有方法差异的p-value。
例如，p_IFA文件夹下的 Cure.LOC.csv 存储了，以Cure.LOC方法为base 方法计算得出的各个方法与其的 p-value值。
这样，我们就得到了bhp-value，如果p-value<0.05我们就认为两个方法之间的差异是显著的，否则不显著。
> 本文档及程序代码 extends 杨佩鑫学张

