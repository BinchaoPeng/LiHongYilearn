[TOC]



# GAN(生成式对抗网络)



## P30-基本概念

![image-20210411154152372](images/image-20210411154152372.png)

每次输入一个x，就要**加上**一个随机变量Z，z属于一个简单分布，比如高斯分布



![image-20210411155850614](images/image-20210411155850614.png)

![image-20210411160410272](images/image-20210411160410272.png)





**Generator:**



**Discriminator:**



两者反复迭代



**GAN-zoo**

![image-20210411155122743](images/image-20210411155122743.png)





## P31-理论介绍与WGAN



![image-20210411162541189](images/image-20210411162541189.png)

Divergence：评价指标，衡量两个分布之间的相似度，越小越相近

P~G~：预测的数据

P~data~：真实数据

![image-20210412085600521](images/image-20210412085600521.png)

distribution的Divergence很难算，算不出来，因此，使用他们的sample

normal distribution 



![image-20210411164320651](images/image-20210411164320651.png)

![image-20210411164416595](images/image-20210411164416595.png)

看到真的图（蓝色），给高分，看到生成的图（黄色），给低分



![image-20210412090454337](images/image-20210412090454337.png)

类似二分类来判断的思路



![image-20210412090929358](images/image-20210412090929358.png)

相似，很小的maxV；



![image-20210412091112182](images/image-20210412091112182.png)



![image-20210412091200729](images/image-20210412091200729.png)





### Gan 训练技巧



#### JS Divergence

![image-20210412091716316](images/image-20210412091716316.png)





![image-20210412092020015](images/image-20210412092020015.png)

![image-20210412092125894](images/image-20210412092125894.png)



#### Wasserstein distance

![image-20210412092337955](images/image-20210412092337955.png)

earth mover:推土机



![image-20210412092519449](images/image-20210412092519449.png)



把P变成Q；左边距离少，右边大

![image-20210412092612900](images/image-20210412092612900.png)





![image-20210412092744550](images/image-20210412092744550.png)



![image-20210412093155751](images/image-20210412093155751.png)

这里的X是指label，输出的图片



![image-20210412093403963](images/image-20210412093403963.png)



