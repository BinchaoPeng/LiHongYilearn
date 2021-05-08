[TOC]



# self-supervised learning



**监督和自监督：**

![image-20210424110336236](images/image-20210424110336236.png)

监督：带有label y_hat；

自监督：无监督的一种，将没有标注的样本X分为两部分，一部分用于model的输入，另一部分作为学习目标，使得y_pre与其接近



# BERT：transformer encoder

![image-20210424111602919](images/image-20210424111602919.png)

输出是所有的可能出现的字的对应分数



![image-20210424111534495](images/image-20210424111534495.png)

湾---》one hot ---》 minimize cross entropy



![image-20210424112152333](images/image-20210424112152333.png)

yes/no: 判断句子是否相接；但是似乎这个没什么用



![image-20210424112750879](images/image-20210424112750879.png)

做下游任务



![image-20210424113122368](images/image-20210424113122368.png)

任务集GLUE：包含9个任务，在这里微调，看看9个模型的平均正确率如何，代表得到model的性能



![image-20210424113321152](images/image-20210424113321152.png)

性能结果



![image-20210424113632693](images/image-20210424113632693.png)

![image-20210424113735115](images/image-20210424113735115.png)



![image-20210424200903647](images/image-20210424200903647.png)



![image-20210424201221894](images/image-20210424201221894.png)

![image-20210424201330077](images/image-20210424201330077.png)

取CLS 经过Linear对应的向量，进行分类



![image-20210424201536820](images/image-20210424201536820.png)

![image-20210424202146140](images/image-20210424202146140.png)

与黄色向量做内积，得到答案的起始位置是2

![image-20210424202241153](images/image-20210424202241153.png)

与蓝色向量做内积，得到答案的结束位置是3



![image-20210424210158044](images/image-20210424210158044.png)

![image-20210424210726654](images/image-20210424210726654.png)



![image-20210424210944995](images/image-20210424210944995.png)

# GPT series

> bert 做填空题
>
> gpt 做预测接下来的部分



![image-20210508104842358](images/image-20210508104842358.png)



![image-20210508104929793](images/image-20210508104929793.png)



![image-20210508105014803](images/image-20210508105014803.png)

类似transformer的decoder



**GPT做翻译的方式：**

![image-20210508105821729](images/image-20210508105821729.png)



## learn more

**GPT3：**

![image-20210508105955285](images/image-20210508105955285.png)

## self-supervise 资料

![image-20210508110829550](images/image-20210508110829550.png)



## Speech GLUE

nlp基准资料库，有九个下游任务，再去平均，代表bert的好坏



# 自编码器（Auto-encoder）



**自监督学习框架：（使用没有label的资料，也可以做下游任务）**

![image-20210508111121389](images/image-20210508111121389.png)



## 基本概念

![image-20210508111849172](images/image-20210508111849172.png)

（vector：embedding、represention、code）



![image-20210508112156344](images/image-20210508112156344.png)

（维度变化：高维经过decoder变为低维）



![image-20210508165549676](images/image-20210508165549676.png)

**输入加入noises，最后还原成原图**



![image-20210508165910253](images/image-20210508165910253.png)

reconstruction：重建；还原



## 领结变声器与更多应用

![image-20210508170145169](images/image-20210508170145169.png)



### feature disentangle

![image-20210508170232245](images/image-20210508170232245.png)

哪些维度代表哪些资讯，比如内容、说话的是谁



### 应用：voice conversion 声音转换

![image-20210508170508816](images/image-20210508170508816.png)



**具体实现步骤：**

![image-20210508170642787](images/image-20210508170642787.png)





### text  as representation

![image-20210508172419565](images/image-20210508172419565.png)

**使用了gan的思想，gan让它可读**



### generator

![image-20210508172728929](images/image-20210508172728929.png)

**把decoder单独拿来做generator**



### compression

![image-20210508172844195](images/image-20210508172844195.png)

Lossy：会失真



### anomaly detection异常检测

![image-20210508173009485](images/image-20210508173009485.png)

**看是否与训练资料相似**



![image-20210508173347990](images/image-20210508173347990.png)

==适用场景==：容易收集到正常资料，不容易收集到异常资料



![image-20210508173708375](images/image-20210508173708375.png)





## learn more

==维度减少：==

![image-20210508112230147](images/image-20210508112230147.png)

==异常检测：==

![image-20210508173759554](images/image-20210508173759554.png)



