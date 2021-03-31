import numpy as np
import math

# define param
"""
K: k-tuple
w: the weight between local sequence and global sequence
lam: λ, 层级关系，即相隔λ长度之间的k-tuple核苷酸的关系
pcf：∧, number of physicochemical feature
"""
K = 4
w = 0.1
lam = 5
pcf = 6

# other param
"""
du_len: the length of k-tuple occurrence frequency
tao_len: 长程序列效应的长度（每种层级关系遍历一次所有的物化性质）
PseKNC: the final output
L: the length of DNA sequence
L_hat <= L - K
"""
du_len = int(math.pow(4, K))
tao_len = lam * pcf
PseKNC = np.zeros((du_len + tao_len), 1)
print(PseKNC.shape)
L = None


# 第一步：计算pow(4,K)个k-tuple元组
def getIndex(tip: str):
    """
    4进制转换成10进制，得到该k-tuple所在的下标
    :param tip:
    :return:
    """
    index = None

    return index


def getK_tupleCount(seq: str):
    # 用于对k-tuple计数，A:0, T:1, G:2, C:3,按照AAA，AAT，AAG，...，TTT排序,真实坐标即是4进制表示
    K_tuple_array = np.zeros(du_len)
    print(K_tuple_array.shape)
    L = len(seq)
    count = 0
    for j in range(L - K + 1):
        tip = seq[j: j + K]
        print("tip:", tip)
        if tip.find('N') != -1:
            print("遇到N")
            continue
        tip.replace('A', '0')
        tip.replace('T', '1')
        tip.replace('G', '2')
        tip.replace('C', '3')
        index = getIndex(tip)
        K_tuple_array[index] += 1
