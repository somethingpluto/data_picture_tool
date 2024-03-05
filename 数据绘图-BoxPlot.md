# Box Plot是什么？
BoxPlot 又称为箱线图/盒须图/盒式图，是一组用于显示一组数据分散情况资料的统计图，因为形状和箱子很像而得名。**通过四分位数以图形的方式展现数值数据的局部性，分布和偏度组的方法**。
箱形图的最大优点就是不受异常值的影响，能够准确稳定的描绘出数据的离散分布情况，同时也有利于数据的清洗。
**箱形图不受异常值的影响**
# 四分位数
四分位数(Quartile)，即把所有数值由小到大排列并分成四等份，处于三个分割点位置的值就是四分位数。
例如：有10，9，8，7，6，5，4，3，2，1,0，-1十二个数字
首选按照从下到大排列
-1 0 1 2 3 4 5 6 7 8 9 10
分成四等份，即每一份有3个数字。
-1 0 1 🟢  2 3 4🟢  5 6 7 🟢  8 9 10 
四等份，3个切割点，这三个切割点就是四分位数，称为Q1 Q2 Q3
下四分位：第一四分位Q1：25%
中位数：第二四分位Q2: 50%
上四分位：第三四分位Q3：75%
# BoxPlot图阅读
![image.png](https://cdn.nlark.com/yuque/0/2024/png/23003149/1709296454217-d191a321-1881-4fe4-9efb-1fc7a920e80b.png#averageHue=%23f5f3f0&clientId=u9e4dc9a9-cbc3-4&from=paste&height=514&id=u0d197e4e&originHeight=643&originWidth=1374&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=175442&status=done&style=none&taskId=ufe082acc-12e6-42d8-a24e-f6cc7032f0f&title=&width=1099.2)
图组成因素：

- 最小值：所有数据中最小值
- 第一四分位(25%)
- 中位数：所有数据中的中位数 median
- 第三四分位(75%)
- 最大值：所有数据中的最大值
- 差异值：
- IQR - 四分位距 Q3 - Q1 也就是中间50%数据落到的地方
## 常见版本
### 只有箱：横竖版
![image.png](https://cdn.nlark.com/yuque/0/2024/png/23003149/1709297244404-147900c5-50ca-405f-86e8-6cd1e23c6a3c.png#averageHue=%23eeeeee&clientId=u9e4dc9a9-cbc3-4&from=paste&height=290&id=uccec192a&originHeight=363&originWidth=542&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=22207&status=done&style=none&taskId=u48233b6b-40d0-4f40-b895-4fbbf9a117a&title=&width=433.6)
![image.png](https://cdn.nlark.com/yuque/0/2024/png/23003149/1709297254499-d6adedcb-994e-416d-85eb-b13ee7bb2a8c.png#averageHue=%23eeeeee&clientId=u9e4dc9a9-cbc3-4&from=paste&height=275&id=u98d81ca5&originHeight=344&originWidth=537&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=21832&status=done&style=none&taskId=u09e99400-0448-4374-8a5a-557f1ebc2d7&title=&width=429.6)
### 箱+点
在箱的基础上，把数据点都标记上去
![image.png](https://cdn.nlark.com/yuque/0/2024/png/23003149/1709297286006-26185415-2469-4b2e-8311-225661555cdb.png#averageHue=%23efefef&clientId=u9e4dc9a9-cbc3-4&from=paste&height=506&id=u6929abbc&originHeight=632&originWidth=586&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=68401&status=done&style=none&taskId=uc715be0f-a46e-4c09-b604-539f7befe58&title=&width=468.8)
![image.png](https://cdn.nlark.com/yuque/0/2024/png/23003149/1709297308700-04e4ab15-1284-4f8b-9a01-bff9ffd07b86.png#averageHue=%23f4f4f4&clientId=u9e4dc9a9-cbc3-4&from=paste&height=478&id=u2b8b853b&originHeight=598&originWidth=581&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=104868&status=done&style=none&taskId=ua8cb29d1-c71a-4222-b38d-620d157ac96&title=&width=464.8)
## 长度-看分布
![image.png](https://cdn.nlark.com/yuque/0/2024/png/23003149/1709297381631-bc4eb267-3fc0-4364-87cf-3bef3cd9594e.png#averageHue=%23ecebeb&clientId=u9e4dc9a9-cbc3-4&from=paste&height=570&id=uc515e29f&originHeight=712&originWidth=766&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=40050&status=done&style=none&taskId=u3959f81d-6ddb-457d-8956-884e48690c8&title=&width=612.8)
**整体越长，数据分布越广**
**整体越短，数据分布越密集**
> 例如，在上图A中，A比C数据跨度更大，从1-100，C集中在40-90之间


## 箱子长短-看集中
![image.png](https://cdn.nlark.com/yuque/0/2024/png/23003149/1709297570467-183ce105-ff89-40c3-b9f4-9bc86b483147.png#averageHue=%23f8f8f8&clientId=u9e4dc9a9-cbc3-4&from=paste&height=448&id=u3626c24a&originHeight=560&originWidth=997&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=113514&status=done&style=none&taskId=u158a643b-097c-4d7c-a43a-f8872c02c56&title=&width=797.6)
箱子的长度表示了50%的数据的分布情况。
**箱子越长，数据越分散，箱子越短，数据越集中**
## 箱子偏向-看数据偏向
![image.png](https://cdn.nlark.com/yuque/0/2024/png/23003149/1709297728226-facfbc89-e85a-4214-b720-baf4d30daa53.png#averageHue=%23ededed&clientId=u9e4dc9a9-cbc3-4&from=paste&height=610&id=u71fd98c0&originHeight=763&originWidth=816&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=95613&status=done&style=none&taskId=u5a76d7d3-7f23-45bb-a19f-b5480a9a13f&title=&width=652.8)
看箱子底部，是里最小值近，还是离箱子最大值近。
**箱子矮，靠近最小值，正态分布的峰值越靠左（50%的数据靠近最小值）**
**箱子高，靠近最大值，正态分布的峰值越靠右（50%的数据靠近最大值）**
上图中，A数据的柱状图分布情况如下：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/23003149/1709297854825-65a433e6-8ccd-446e-bcc4-bf78673ce534.png#averageHue=%23fefefc&clientId=u9e4dc9a9-cbc3-4&from=paste&height=270&id=uc674d168&originHeight=337&originWidth=698&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=9243&status=done&style=none&taskId=u795f57af-f455-45ea-93ca-cfaf589b15d&title=&width=558.4)
C数据的柱状图分布情况如下：

![image.png](https://cdn.nlark.com/yuque/0/2024/png/23003149/1709297870474-4884409b-737c-46b1-9e1f-e52eecbb26ec.png#averageHue=%23fefefd&clientId=u9e4dc9a9-cbc3-4&from=paste&height=205&id=u93c21582&originHeight=256&originWidth=681&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=6005&status=done&style=none&taskId=u960af4fd-04c9-4db9-a166-0f8488a9408&title=&width=544.8)
## 箱子中的线-看中位数字
![image.png](https://cdn.nlark.com/yuque/0/2024/png/23003149/1709297978983-72c52b09-08d2-4f0c-8fb0-9ef410e332c0.png#averageHue=%23efeaea&clientId=u9e4dc9a9-cbc3-4&from=paste&height=582&id=ua39890f7&originHeight=728&originWidth=760&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=71832&status=done&style=none&taskId=u18fb61b2-e53b-4895-b383-512ed063a4d&title=&width=608)
**黑线表示中位数的水平，不受极大值和极小值的影响的平均水平。**
例如上图中：
C组的中间分数高于A组，如果y轴表示薪水，C公司的普遍薪水应该高于A组
## 箱子中的线位置-看
![image.png](https://cdn.nlark.com/yuque/0/2024/png/23003149/1709298165122-735577b9-c3c8-4348-b20c-810025caf824.png#averageHue=%23f0f0f0&clientId=u9e4dc9a9-cbc3-4&from=paste&height=602&id=uc1d33912&originHeight=752&originWidth=792&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=57368&status=done&style=none&taskId=ue71b6ee6-082a-4563-9302-72d13cdf7cc&title=&width=633.6)
黑线在箱子的位置：中间，偏上，偏下
中间：中位数=均值 正常分布
偏上：中位数 > 均值 负偏分布 (左偏态)
偏下：中位数 < 均值 正偏分布 (右偏态)
# BoxPlot功能
## 检测异常值
![image.png](https://cdn.nlark.com/yuque/0/2024/png/23003149/1709298423286-46b590d5-55da-448f-8b72-1e165b81d2a7.png#averageHue=%23f4f3f3&clientId=u9e4dc9a9-cbc3-4&from=paste&height=444&id=ubaabee7b&originHeight=555&originWidth=1019&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=182095&status=done&style=none&taskId=uc27a3799-32bc-4bea-a0f8-ec405f1f4e3&title=&width=815.2)
上图中，4和30被判定位异常值，规则有上面boxplot图中的lower和upper根据算法定义
## 

