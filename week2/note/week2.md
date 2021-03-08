[TOC]



# week2-类神经网络训练不起来



## lecture2-1  

通常步骤：

![image-20210307164927390](images/image-20210307164927390.png)





overfitting解决办法：

- 增加训练资料
- 数据增广（data augmentation）



数据集划分：

mse：mean squared error



- cross validation

![image-20210307172004356](images/image-20210307172004356.png)



- k-flod cross validation

![image-20210307171940652](images/image-20210307171940652.png)

 

## optimization fails

![image-20210307172655076](images/image-20210307172655076.png)

gradient=0时，loss就不再下降了

有以下情况：

- critical point：gradient=0【一个统称】

- local minima
- local maxima
- saddle point（鞍点）：gradient=0，不是local minima，也不是local maxima

![image-20210307175433245](images/image-20210307175433245.png)



![image-20210307175603861](images/image-20210307175603861.png)

elgen value:特征值



H： Hessian

![image-20210307180244350](images/image-20210307180244350.png)



## lecture2-2 batch and momentum（动量）



### batch

![image-20210308084332272](images/image-20210308084332272.png)

shuffle：打乱数据集，每epoch分的batch中的数据不一样

batch_size=n：每看n个数据，参数就update一次；

==更小的batch_size性能更好；因为大的batch_size会optimization fails==



![image-20210308085820435](images/image-20210308085820435.png)



Full Batch：gradient=0，就卡住了

small batch：gradient=0，换下一个epoch，此时不一定卡住，会继续计算



最终对比：

![image-20210308090610851](images/image-20210308090610851.png)



### momentum

![image-20210308090835275](images/image-20210308090835275.png)

动量一定大的时候，球不一定会停在鞍点或者局部最低点



计算方式：

![image-20210308091427402](images/image-20210308091427402.png)

朝gradient的反方向运动



![image-20210308091602683](images/image-20210308091602683.png)



![image-20210308091757515](images/image-20210308091757515.png)



