[https://real-statistics.com/non-parametric-tests/mann-whitney-test/cliffs-delta/](https://real-statistics.com/non-parametric-tests/mann-whitney-test/cliffs-delta/)
# 介绍
Cliff's Delta是一种非参数的效应大小度量方法，用于量化两个组或条件之间的差异。它通常在数据为顺序或非正态分布，并且假设组间方差不相等时使用。
# 论文中使用
![image.png](https://cdn.nlark.com/yuque/0/2024/png/23003149/1709614172956-2305123e-a3e0-4647-b53f-c4fa1336cbb4.png#averageHue=%23f4f1ea&clientId=u2a76f730-d9c9-4&from=paste&height=177&id=u5d6fde61&originHeight=221&originWidth=865&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=131467&status=done&style=none&taskId=ue34483ec-b4c9-4b63-bc2f-677d0f6e0a0&title=&width=692)
小于 0.147认为差异可忽略，大于0.147就认为差异不可忽略了，各个等级描述如上。
和wilcoxon和cliff delta相结合，描述如下：

- p-value < 0.05 && d > 0.147 认为两者之间具有显著性差异
- p-value > 0.05 或者 p<0.05 并且 d < 0.147 认为两个方法之间没有显著差异
## 写作
> 以下内容最好取舍使用，变换下说法，尤其是Wilcoxon signed-rank test说的比较多，可以取舍下，表达方式最好也稍微改下，有的是论文原话，我融合了好几篇论文。
> 参考文献[4-7]都是有这种表达的论文，即同时使用了Wilcoxon signed-rank test和cliff‘s delta的论文。表格也可以换成文字描述（这种使用的也比较多）
> Wilcoxon signed-rank test [1] is a non-parametric sample test, which is based on the ranking of the methods rather than the mean. 
> This statistical test method does not require the analyzed data should follow any distribution. Moreover, it can be used to compare pairs of results and is able to compare the difference against zero.
> The basic principle of hypothesis testing is the small probability principle, which states that a small probability event cannot actually occur in a single test.
> However, when multiple hypothesis tests are performed under the same research problem, it no longer fits the single test as stated by the small probability principle.
> So we use the Benjamini-Hochberg (BH) [2] procedure to adjust p-values if we perform multiple comparisons. 
> 
> Then if the test shows a significant difference, we compute Cliffs 𝛿 [3], which is a non-parametric effect size measure, to examine whether the magnitude of the difference is substantial or not. 
> The meaning of different Cliffs 𝛿 value and their corresponding interpretation are shown in Table 1. 
> In summary, a method performs significantly better or worse than another method, if BH corrected p-value is less than 0.05 and the effectiveness level is not negligible based on Cliff’s 𝛿. While the difference between two methods is not significant, if p-value is not less than 0.05 or p-value is less than 0.05 and the effectiveness level is negligible (less than 0.147) [4,5,6,7].
> ![image.png](https://cdn.nlark.com/yuque/0/2024/png/23003149/1709614459200-0e4559f0-4f97-43f0-a9cc-58ed4d52bb0d.png#averageHue=%23f6f4f3&clientId=u2a76f730-d9c9-4&from=paste&height=342&id=u415bd47b&originHeight=428&originWidth=756&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=116595&status=done&style=none&taskId=u29030925-152d-4eff-830d-aa28969ef19&title=&width=604.8)
> ![image.png](https://cdn.nlark.com/yuque/0/2024/png/23003149/1709614455212-4b6ff736-b3c6-4bb1-b8b8-2c9d53b5720a.png#averageHue=%23f4f0e9&clientId=u2a76f730-d9c9-4&from=paste&height=173&id=ucfd2feb6&originHeight=216&originWidth=865&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=138172&status=done&style=none&taskId=u70e385d3-2122-46ec-9d10-130e27f483c&title=&width=692)
> [1] Benjamini Y, Yekutieli D. The control of the false discovery rate in multiple testing under dependency[J]. Annals of statistics, 2001: 1165-1188.
> [2] Ferreira J A, Zwinderman A H. On the benjamini–hochberg method[J]. 2006.
> [3] Benjamini Y, Hochberg Y. Controlling the false discovery rate: a practical and powerful approach to multiple testing[J]. Journal of the Royal statistical society: series B (Methodological), 1995, 57(1): 289-300.
> [4] Chen X, Zhang D, Zhao Y, et al. Software defect number prediction: Unsupervised vs supervised methods[J]. Information and Software Technology, 2019, 106: 161-181.
> [5] Chen D, Chen X, Li H, et al. Deepcpdp: Deep learning based cross-project defect prediction[J]. IEEE Access, 2019, 7: 184832-184848.
> [6] Li Y, Meng L, Chen L, et al. Training data debugging for the fairness of machine learning software[C]//Proceedings of the 44th International Conference on Software Engineering. 2022: 2215-2227.
> [7] Sae-Lim N, Hayashi S, Saeki M. Can automated impact analysis techniques help predict decaying modules?[C]//2019 IEEE International Conference on Software Maintenance and Evolution (ICSME). IEEE, 2019: 541-545.

# 使用说明
## 代码目录
路径：data_picture_tool/cliff_delta/clif_delta.py
![image.png](https://cdn.nlark.com/yuque/0/2024/png/23003149/1709614522132-06266d8b-943f-4fce-8d9d-34069271a0d6.png#averageHue=%23ede6d2&clientId=u42194ffe-6878-4&from=paste&height=212&id=uec431cba&originHeight=132&originWidth=298&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=5609&status=done&style=none&taskId=u5df08427-267d-486a-831b-34b5942a2b4&title=&width=478.3999938964844)
output：cliff_delta计算结果
test_data：测试数据存放文件夹
cliff_delta_config.yaml：配置文件
cliff_delta.py：源文件
## 数据格式准备
和 wilcoxon Singed Rank Test 数据格式要求一致
文件命名：性能指标.xlsx
xlsx文件要求：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/23003149/1709614844056-894e0664-78a2-4dad-bb6c-7ef0ce0a567c.png#averageHue=%23f4edda&clientId=u602b6a23-df62-4&from=paste&height=782&id=ued87932a&originHeight=977&originWidth=1043&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=65875&status=done&style=none&taskId=u871c5600-e993-4f9b-9df2-0f06d58232b&title=&width=834.4)
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
结果默认输出到，运行目录中的output文件夹。结果保存为csv文件。
![image.png](https://cdn.nlark.com/yuque/0/2024/png/23003149/1709615177573-d8ad0a81-071c-4f3f-8664-da3161140af1.png#averageHue=%23ebe5d0&clientId=u0a66c0f0-5562-4&from=paste&height=387&id=u000814e5&originHeight=484&originWidth=293&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=20149&status=done&style=none&taskId=ucab07457-cd0d-42f8-90a2-066cf444918&title=&width=234.4)
![image.png](https://cdn.nlark.com/yuque/0/2024/png/23003149/1709615209591-d7277380-77b9-47a6-a571-91409221eef8.png#averageHue=%23f9f2dd&clientId=u0a66c0f0-5562-4&from=paste&height=70&id=uaff82e42&originHeight=87&originWidth=1554&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=35834&status=done&style=none&taskId=u73168150-40bd-4d19-9a62-54555535224&title=&width=1243.2)
Cliff_IFA文件夹 中Cure.LOC.csv文件表明IFA指标中，以Cure.LOC.csv为baseline条件下计算的各个cliff_delta值。
> 本文档及程序代码 extends 杨佩鑫学张

