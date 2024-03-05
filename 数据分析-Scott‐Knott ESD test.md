# 详细文档
[https://cran.r-project.org/web/packages/ScottKnottESD/ScottKnottESD.pdf](https://cran.r-project.org/web/packages/ScottKnottESD/ScottKnottESD.pdf)
# 介绍
斯科特-克诺特效应大小差异（Scott-Knott Effect Size Difference , ESD）检验是一种均值比较方法，它利用分层聚类将一组处理均值（treatment means）（如变量重要性评分均值、模型性能均值）划分为统计学上有显著差异的组，差异不可忽略。这是斯科特-克诺特检验的另一种方法，它考虑的是组内和组间处理均值的差异大小（即效应大小）
因此，Scott-Knott ESD 检验可以得出处理平均值的排序，同时确保：
(1) 每组中所有处理的差异幅度可以忽略不计；
(2) 每组间所有处理的差异幅度不可以忽略不计。
Scott-Knott ESD 检验的机制由两个步骤组成：

1. 找出一个分区（partition），使各组间的处理均值（treatment means）最大化。我们首先对处理均值（treatment means）进行排序。然后，按照最初的 Scott-Knott 检验方法，我们计算组间平方和（即数据点的离散度量），找出能使组间处理均值（treatment means）最大化的分区。
2. 分成两组或合并为一组。而不是使用似然比检验和卡方分布作为拆分和合并的标准（即对所有处理均值相等进行假设检验 我们不使用似然比检验和卡方分布作为拆分和合并标准（即假设检验所有处理均值相等），而是分析每对 的差异大小。如果有任何一对两组的处理均值是 不可忽略，我们就分成两组。否则，我们合并为一组。我们使用 Cohen effect size（科恩效应大小）–一种基于两组均值之差除以两组均值标准差的效应大小估计值（d = (mean(x_1) - mean(x_2))/s.d.）。

主要应用与下面几个方面：

1. 显著差异检测：Scott-Knott ESD测试可以帮助确定在某个指标上是否存在显著差异。通过比较不同组之间的差异大小，可以确定哪些组之间的差异是显著的，哪些组之间的差异不显著
2. 分组排序：该测试方法可以对多个组进行排序，以确定它们在某个指标上的相对表现。通过对组进行排名，可以清晰地了解哪些组在指标上表现最好，哪些组表现较差。
3. 组的分离：Scott-Knott ESD测试还可以将相似的组合并，以区分在某个指标上有显著差异的组。通过将相似的组结合起来，可以更好地理解数据中存在的不同群体，并识别出那些在指标上具有相似表现的组。
# sk_esd
## 使用说明
### 环境配置
跟着下方文档安装R语言环境。在pycharm or vscode中创建R语言文件，根据提示下载对应的插件即可。
[R及RStudio下载安装教程（超详细）-CSDN博客](https://blog.csdn.net/W_chuanqi/article/details/123626811)
### 代码目录
路径：data_picture_tool/sk_esd/sk_esd.r
![image.png](https://cdn.nlark.com/yuque/0/2024/png/23003149/1709617109811-1e547689-54ff-41f9-94a1-9319ac2cd072.png#averageHue=%23ece4ce&clientId=ue23f4451-aa8d-4&from=paste&height=85&id=u1313fb5b&originHeight=106&originWidth=304&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=4565&status=done&style=none&taskId=uf04ebd04-8896-4579-b01a-690b4c76318&title=&width=243.2)
output：计算结果保存文件夹
test_data：测试数据存放文件夹，可在代码中指定修改
sk_esd.R：源文件
### 输出文件
输出文件为txt文件。命名规则为，指标.txt
![image.png](https://cdn.nlark.com/yuque/0/2024/png/23003149/1709617229974-f3eb1d1d-d4eb-4856-b5f8-70e5f7227625.png#averageHue=%23ede7d3&clientId=ue23f4451-aa8d-4&from=paste&height=174&id=ufa975256&originHeight=217&originWidth=292&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=6687&status=done&style=none&taskId=u60721d2c-7325-46a6-9d8a-48bcb5c9802&title=&width=233.6)
文件内容：
```
"x"
"Bang.LOC" 1
"AP.LOC" 1
"Kmedoids.LOC" 2
"Dbscan.LOC" 2
"Optics.LOC" 2
"EMA.NPM" 3
"Cure.LOC" 3
"Rock.AMC" 3
"KmeansPlus.LOC" 3
"Bsas.LCOM3" 3
"Mbsas.LCOM3" 3
"Agglomerative.LOC" 3
"MiniBatchKmeans.LOC" 3
"Syncsom.CBO" 3
"Ttsas.NPM" 3
"Kmeans.LOC" 3
"Xmeans.CAM" 3
"Fcm.LCOM3" 3
"MeanShift.Avg_CC" 3
"Gmeans.DAM" 3
"Somsc.LOC" 3
"Birch.Ce" 3
```
输出的文件，即将所有方法进行分组，同一组别内的方法之间没有显著差异，不同组别之间具有显著差异。而且，这个排序是根据均值进行了数值的排序，1组是显著优于2和3组的方法，2组内的方法显著优于3组内的方法。
### 绘图
绘图可操作数据绘图文档  
数据绘图-BoxPlot
这里说明一下，根据上述sk_esd文件绘图需要关注的地方。
#### 1.sk_result 和 raw_data 文件路径
![image.png](https://cdn.nlark.com/yuque/0/2024/png/23003149/1709618806209-69f27b3d-603b-4077-a1b7-0b2fd6e1aa2c.png#averageHue=%23fcf4e0&clientId=ue23f4451-aa8d-4&from=paste&height=260&id=u56402070&originHeight=325&originWidth=833&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=41650&status=done&style=none&taskId=u39bd9d05-d3b0-4737-bf71-02486e8946a&title=&width=666.4)
sk_result_path: 即上述通过sk_esd 生成得到存放txt文件的文件夹路径
raw_data_path：即为sk_ead中是使用的csv文件夹路径。
#### 2.header修改
#### ![image.png](https://cdn.nlark.com/yuque/0/2024/png/23003149/1709618938292-f11751e6-f4dd-47be-a015-494a33d0edca.png#averageHue=%23fcf4e1&clientId=ue23f4451-aa8d-4&from=paste&height=558&id=u0332c2bb&originHeight=697&originWidth=702&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=57518&status=done&style=none&taskId=u6f5de481-c0cc-45c9-936b-98f94b26685&title=&width=561.6)
#### header以txt文件夹中的方法为准，这里一定要和txt文件夹中保持一致，可以多，但绝对不能少。
#### 3.绘图结果文件输出
默认保存在工作目录下的，pictures文件夹下。
![image.png](https://cdn.nlark.com/yuque/0/2024/png/23003149/1709619024164-f97b2045-3832-4bd9-b6a0-d9a7adf9ee66.png#averageHue=%23f7f7f6&clientId=ue23f4451-aa8d-4&from=paste&height=484&id=ueeae6720&originHeight=605&originWidth=2129&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=190516&status=done&style=none&taskId=u9f5455f1-0d92-4952-bc8c-87943d5b70f&title=&width=1703.2)
# sk_esd_ranking
## 使用说明
代码目录：data_piture_tool/sk_resd_ranking
![image.png](https://cdn.nlark.com/yuque/0/2024/png/23003149/1709620868294-a94cb74a-a861-467e-8714-2bf1029b7a9b.png#averageHue=%23ede6d3&clientId=uc3902975-287d-4&from=paste&height=134&id=u3e7e627b&originHeight=115&originWidth=302&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=5342&status=done&style=none&taskId=ucbf52fe9-971c-413a-9f5b-fa5dcc70211&title=&width=352.6000061035156)
picture：输出图片文件夹
test_data：测试数据
sk_esd_ranking.R：源文件
![image.png](https://cdn.nlark.com/yuque/0/2024/png/23003149/1709620921431-6adc4a78-c730-40a2-a0bb-453bca249338.png#averageHue=%23fcf4e1&clientId=uc3902975-287d-4&from=paste&height=117&id=ue35c8c65&originHeight=146&originWidth=1366&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=44717&status=done&style=none&taskId=uab87f62c-8aa9-4759-8a3d-a59447670be&title=&width=1092.8)
根据文件夹路径修改上述两个变量值即可。
![RQ1_Ranking_F1x.csv.jpg](https://cdn.nlark.com/yuque/0/2024/jpeg/23003149/1709622200427-7bdabbff-df40-4dbc-bb0a-4a2d16c4f69b.jpeg#averageHue=%23fefdfd&clientId=uc3902975-287d-4&from=paste&height=64000&id=ud9787405&originHeight=20000&originWidth=5000&originalType=binary&ratio=1.25&rotation=270&showTitle=false&size=2567140&status=done&style=none&taskId=uc4916936-d05c-498c-b707-07845535174&title=&width=16000)
# 论文写作
To rank all the different supervised methods and unsupervised methods, we use Scott-Knott test, which is recommended by Ghotra et al. [48]. Scott–Knott test is used to examine whether some methods outperform others and generates a global ranking of these methods. In particular, Scott-Knott test performs the grouping process in a recursive way. Firstly, Scott-Knott test uses a hierarchical cluster analysis to partition all the methods into two ranks based on the mean performance (FPA or Kendall). Then if the divided ranks are significantly different, Scott-Knott test is recursively executed again within each rank to further divide the ranks. When ranks can no longer be divided into statistically distinct ranks, the test will terminate. 

来源：Chen X, Zhang D, Zhao Y, et al. Software defect number prediction: Unsupervised vs supervised methods[J]. Information and Software Technology, 2019, 106: 161-181.

[48] Ghotra B, McIntosh S, Hassan A E. Revisiting the impact of classification techniques on the performance of defect prediction models[C]//2015 IEEE/ACM 37th IEEE International Conference on Software Engineering. IEEE, 2015, 1: 789-800.

原文2：

Scott‐Knott ESD [39] test is a multiple comparison method that utilises hierarchical clustering to divide EACPDP methods into different groups with significant differences at the significance level of 0.05 (α = 0.05). It ranks the EACPCP methods while ensuring the magnitude of differences is negligible for methods within the same group, and the difference is not negligible for methods between groups. In other words, there is no significant difference among the EACPDP methods in the same group, while the EACPDP methodsin different groups have significant difference. For example, the Scott‐Knott ESD test divides five methods into the two groups, that is, Group 1 (including methodsA, D and E) and Group 2 (including methods B and C). There is no significant difference between the methods within either Group 1 or Group 2. However, the methodsA, D and E in Group 1 significantly outperform the methods B and C in Group 2 according to the Scott‐Knott ESD test.
来源：Li F, Yang P, Keung J W, et al. Revisiting ‘revisiting supervised methods for effort‐aware cross‐project defect prediction’[J]. IET Software, 2023, 17(4): 472-495.

[39] Tantithamthavorn, C., et al.: An empirical comparison of model validation techniques for defect prediction models. IEEE Trans. Software Eng. 43, 1–18 (2016). https://doi.org/10.1109/tse.2016.2584050
> 本文档及程序代码 extends 杨佩鑫学张

