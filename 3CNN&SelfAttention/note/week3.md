[TOC]



# week3

> p9_卷积神经网络（CNN）
>
> p10_自注意力机制（Self_attention）



## p9_卷积神经网络（CNN）



![image-20210314140855703](images/image-20210314140855703.png)



![image-20210314143400343](images/image-20210314143400343.png)

==transformer==





## P10_自注意力机制（Self_attention）上

### input

文本方式：

![image-20210314143834441](images/image-20210314143834441.png)

learn more: ==word Embedding==



语音方式：

![image-20210314144040665](images/image-20210314144040665.png)



图（graph）方式：

每个node作为一个节点，用向量表示信息



### output

- 每个向量都有一个输出（输入输出数目一样的）

  ![image-20210314144805797](images/image-20210314144805797.png)

- 整个序列只有一个输出（类似分类问题）

  ![image-20210314144948008](images/image-20210314144948008.png)

- 机器自己决定输出label的数量（seq2seq）

  ![image-20210314145036788](images/image-20210314145036788.png)





### self_attention

![image-20210314145614011](images/image-20210314145614011.png)

经过self_attention得到的输出，就考虑了整个seq的后得到的结果。



交替使用**self_attention**

![image-20210314145726250](images/image-20210314145726250.png)



paper：Attention is all you need  http://arxiv.org/abs/1706.03762



**内部结构：**

![image-20210314145945478](images/image-20210314145945478.png)



计算b^1^的过程：

- 根据a^1^这个向量，找出整个seq中哪个是最重要的，哪些跟判断a^1^是哪一个label是有关系的

  ![image-20210314150328120](images/image-20210314150328120.png)

  - ​	alfer（关联性）怎么计算？

    ![image-20210314153359367](images/image-20210314153359367.png)

    一般用左边，transformer里面也是用左边的

  - 具体计算过程：

    计算关联性：

  	![image-20210314153710766](images/image-20210314153710766.png)

  	​	

  	![image-20210314153733329](images/image-20210314153733329.png)

  	不一定使用Soft-max，也可以relu

  - 得到b^1^
  
    ![image-20210314155206865](images/image-20210314155206865.png)



## P11_Self-attention(下)



计算b~2~

![image-20210329094536042](images/image-20210329094536042.png)

这里，α^'^ 应该是经过了softmax的。



Q、K、V

![img](images/0019%7DQC1S%25NW%5BO%605RZPJ%25%25Q.png)



α的计算过程

![image-20210329101020194](images/image-20210329101020194.png)



O是attention矩阵

![image-20210329101541790](images/image-20210329101541790.png)

### Muti-head Self-attention





![image-20210329102139892](images/image-20210329102139892.png)

![image-20210329102215408](images/image-20210329102215408.png)

多头注意时：对应头做点积运算，最后拼接得到b^i^



### Positional Encoding

> 添加序列位置信息（可选）
>
> 为每一个位置设置一个vector e^i^  (i代表位置，类似独热，合起来就是矩阵)



![image-20210329103155197](images/image-20210329103155197.png)



### bert

![image-20210329103512006](images/image-20210329103512006.png)



### Truncated Self-attention

> 考虑一个小范围位置，加快计算速度

![image-20210329103717638](images/image-20210329103717638.png)



### 影像处理

![image-20210329103918792](images/image-20210329103918792.png)



![image-20210329103937222](images/image-20210329103937222.png)



### Self-attention && CNN

![image-20210329104418743](images/image-20210329104418743.png)



![image-20210329104612908](images/image-20210329104612908.png)



self-attention需要大量训练样本

从弹性上分析，self-attention的弹性更大，需要更多的数据，训练样本少的时候容易overfiting 。而CNN相反，弹性较小。



### Self-attention && RNN

![image-20210329105102943](images/image-20210329105102943.png)

RNN串行、self-attention并行

RNN双向时，相当于考虑了整个序列，而不是输入以前的序列

![image-20210329105404380](images/image-20210329105404380.png)



### RNN

![image-20210329105429564](images/image-20210329105429564.png)



### Graph处理

![image-20210329105544363](images/image-20210329105544363.png)

之间的关系：

![image-20210329105644861](images/image-20210329105644861.png)



### GNN（Graph ... ...）

![image-20210329105720972](images/image-20210329105720972.png)



### 变型

![image-20210329105809867](images/image-20210329105809867.png)