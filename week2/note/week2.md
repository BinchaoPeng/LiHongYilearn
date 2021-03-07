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

