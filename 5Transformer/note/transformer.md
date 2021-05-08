[TOC]



# Transformer



## P27-Encoder

![image-20210329195220672](images/image-20210329195220672.png)



![image-20210329195347493](images/image-20210329195347493.png)



![image-20210329195908301](images/image-20210329195908301.png)



## P28-Decoder

> 两种decoder：
>
> 1. Autoregressive



### Autoregressive（AT）



![image-20210411133051805](images/image-20210411133051805.png)





vocab.txt  :存储常见字



![image-20210411133341359](images/image-20210411133341359.png)



#### decoder内部结构





![image-20210411133610604](images/image-20210411133610604.png)

![image-20210411133821049](images/image-20210411133821049.png)

**Masked Self-attention：**每个b~i~只考虑当前位置前面的a，比如b~2~只考虑a^1^，a^2^两部分，不考虑a^3^，a^4^



![image-20210411134055319](images/image-20210411134055319.png)

![image-20210411134118565](images/image-20210411134118565.png)

**Masked: **不考虑他右边的部分，只考虑左边的部分



**不知道输出的长度，可能一直输出，因此：**增加符号“END”表示停止

![image-20210411134551609](images/image-20210411134551609.png)

![image-20210411134656301](images/image-20210411134656301.png)

输入习，得到END的概率是max



### Non-autoregressive（NAT）

![image-20210411134846640](images/image-20210411134846640.png)



![image-20210411134944911](images/image-20210411134944911.png)

AT是串行；NAT是并行，可控的输出长度，但是通常效果不如AT好

**怎么知道输出长度：**2种方式

![image-20210411135616529](images/image-20210411135616529.png)

==NAT==

![image-20210411140113517](images/image-20210411140113517.png)





![image-20210411140343081](images/image-20210411140343081.png)

![image-20210411140422302](images/image-20210411140422302.png)
decoder的q和encoder的k、v



![image-20210411144904018](images/image-20210411144904018.png)



![image-20210411145338331](images/image-20210411145338331.png)

### Guided Attention

要求做attention的时候，有固定方式



![image-20210411151420570](images/image-20210411151420570.png)

下面的attention方式对语音合成不适用，不是和上面一样，从左到右



### Beam Search

有时有用、有时没用



### Metrics

![image-20210411152702537](images/image-20210411152702537.png)

使用BLEU score判断两个句子，越高越好



![image-20210411152855638](images/image-20210411152855638.png)

**使用RL硬做**



### exposure bias

![image-20210411153000227](images/image-20210411153000227.png)

训练的时候，它输入的永远是正确的，但是，测试的时候，预测的不一定是对的，就会一直错



#### Scheduled Sampling

![image-20210411153426492](images/image-20210411153426492.png)



