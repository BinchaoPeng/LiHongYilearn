[TOC]



# week3

> p9_卷积神经网络（CNN）
>
> p10_自注意力机制（Self_attention）



## p9_卷积神经网络（CNN）



![image-20210314140855703](images/image-20210314140855703.png)



![image-20210314143400343](images/image-20210314143400343.png)

==transformer==





## P10_自注意力机制（Self_attention）

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