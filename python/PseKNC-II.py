import numpy as np
import math


class PseKNC:
    """
    对于不确定碱基N，直接将其物化性质置0
    :return
    PseKNC1: du先normalization，再计算W*tao，最后整体normalization
    PseKNC2： du先normalization，再计算tao并normalization，最后依据W设置du、tao之间的比例
    """

    def __init__(self, seq="ATGCACGCAT", K=4, lam=5, W=0.1,
                 pcf_array=["旋转扭曲", "左右倾斜", "前后卷动", "左右移动", "前后移动", "上下移动"],
                 n=2):
        # physicochemical feature value
        self.PC_dic_2 = {
            '旋转扭曲': {'AA': 0.063, 'AC': 1.502, 'AG': 0.783, 'AT': 1.071, 'CA': -1.376, 'CC': 0.063, 'CG': -1.664,
                     'CT': 0.783, 'GA': -0.081, 'GC': -0.081, 'GG': 0.063, 'GT': 1.502, 'TA': -1.233, 'TC': -0.081,
                     'TG': -1.376, 'TT': 0.063},
            '左右倾斜': {'AA': 0.502, 'AC': 0.502, 'AG': 0.359, 'AT': 0.215, 'CA': -1.364, 'CC': 1.077, 'CG': -1.22,
                     'CT': 0.359, 'GA': 0.502, 'GC': 0.215, 'GG': 1.077, 'GT': 0.502, 'TA': -2.368, 'TC': 0.502,
                     'TG': -1.364, 'TT': 0.502, },
            '前后卷动': {'AA': 0.092, 'AC': 1.195, 'AG': -0.276, 'AT': 0.827, 'CA': -1.011, 'CC': -0.276, 'CG': -1.359,
                     'CT': -0.276, 'GA': 0.092, 'GC': 2.98, 'GG': -0.276, 'GT': 1.195, 'TA': -1.379, 'TC': 0.092,
                     'TG': -1.011, 'TT': 0.092, },
            '左右移动': {'AA': 1.587, 'AC': 0.126, 'AG': 0.679, 'AT': -1.019, 'CA': -0.861, 'CC': 0.56, 'CG': -0.822,
                     'CT': 0.679, 'GA': 0.126, 'GC': -0.348, 'GG': 0.56, 'GT': 0.126, 'TA': -2.243, 'TC': 0.126,
                     'TG': -0.861, 'TT': 1.587, },
            '前后移动': {'AA': 0.111, 'AC': 1.289, 'AG': -0.241, 'AT': 2.513, 'CA': -0.623, 'CC': -0.822, 'CG': -0.287,
                     'CT': -0.241, 'GA': -0.394, 'GC': 0.646, 'GG': -0.822, 'GT': 1.289, 'TA': -1.511, 'TC': -0.394,
                     'TG': -0.623, 'TT': 0.111, },
            '上下移动': {'AA': 1.289, 'AC': -0.241, 'AG': 2.513, 'AT': -0.623, 'CA': -0.822, 'CC': -0.287, 'CG': -0.241,
                     'CT': -0.394, 'GA': 0.646, 'GC': -0.822, 'GG': 1.289, 'GT': -1.511, 'TA': -0.394, 'TC': -0.623,
                     'TG': 0.111, },
        }
        self.PC_dic_3 = {
            'a': {'AAA': 1, 'AAT': 1, 'AAG': 1, 'AAC': 1, 'ATA': 1, 'ATT': 1, 'ATG': 1, 'ATC': 1, 'AGA': 1, 'AGT': 1,
                  'AGG': 1,
                  'AGC': 1, 'ACA': 1, 'ACT': 1, 'ACG': 1, 'ACC': 1, 'TAA': 1, 'TAT': 1, 'TAG': 1, 'TAC': 1, 'TAA': 1,
                  'TAT': 1,
                  'TAG': 1, 'TAC': 1, 'TAA': 1, 'TAT': 1, 'TAG': 1, 'TAC': 1, 'TAA': 1, 'TAT': 1, 'TAG': 1, 'TAC': 1,
                  'GAA': 1,
                  'GAT': 1, 'GAG': 1, 'GAC': 1, 'GTA': 1, 'GTT': 1, 'GTG': 1, 'GTC': 1, 'GTA': 1, 'GTT': 1, 'GTG': 1,
                  'GTC': 1,
                  'GTA': 1, 'GTT': 1, 'GTG': 1, 'GTC': 1, 'CTA': 1, 'CTT': 1, 'CTG': 1, 'CTC': 1, 'CTA': 1, 'CTT': 1,
                  'CTG': 1,
                  'CTC': 1, 'CGA': 1, 'CGT': 1, 'CGG': 1, 'CGC': 1, 'CGA': 1, 'CGT': 1, 'CGG': 1, 'CGC': 1,
                  },
            'b': {'AAA': 1, 'AAT': 1, 'AAG': 1, 'AAC': 1, 'ATA': 1, 'ATT': 1, 'ATG': 1, 'ATC': 1, 'AGA': 1, 'AGT': 1,
                  'AGG': 1,
                  'AGC': 1, 'ACA': 1, 'ACT': 1, 'ACG': 1, 'ACC': 1, 'TAA': 1, 'TAT': 1, 'TAG': 1, 'TAC': 1, 'TAA': 1,
                  'TAT': 1,
                  'TAG': 1, 'TAC': 1, 'TAA': 1, 'TAT': 1, 'TAG': 1, 'TAC': 1, 'TAA': 1, 'TAT': 1, 'TAG': 1, 'TAC': 1,
                  'GAA': 1,
                  'GAT': 1, 'GAG': 1, 'GAC': 1, 'GTA': 1, 'GTT': 1, 'GTG': 1, 'GTC': 1, 'GTA': 1, 'GTT': 1, 'GTG': 1,
                  'GTC': 1,
                  'GTA': 1, 'GTT': 1, 'GTG': 1, 'GTC': 1, 'CTA': 1, 'CTT': 1, 'CTG': 1, 'CTC': 1, 'CTA': 1, 'CTT': 1,
                  'CTG': 1,
                  'CTC': 1, 'CGA': 1, 'CGT': 1, 'CGG': 1, 'CGC': 1, 'CGA': 1, 'CGT': 1, 'CGG': 1, 'CGC': 1,
                  },
            'c': {'AAA': 1, 'AAT': 1, 'AAG': 1, 'AAC': 1, 'ATA': 1, 'ATT': 1, 'ATG': 1, 'ATC': 1, 'AGA': 1, 'AGT': 1,
                  'AGG': 1,
                  'AGC': 1, 'ACA': 1, 'ACT': 1, 'ACG': 1, 'ACC': 1, 'TAA': 1, 'TAT': 1, 'TAG': 1, 'TAC': 1, 'TAA': 1,
                  'TAT': 1,
                  'TAG': 1, 'TAC': 1, 'TAA': 1, 'TAT': 1, 'TAG': 1, 'TAC': 1, 'TAA': 1, 'TAT': 1, 'TAG': 1, 'TAC': 1,
                  'GAA': 1,
                  'GAT': 1, 'GAG': 1, 'GAC': 1, 'GTA': 1, 'GTT': 1, 'GTG': 1, 'GTC': 1, 'GTA': 1, 'GTT': 1, 'GTG': 1,
                  'GTC': 1,
                  'GTA': 1, 'GTT': 1, 'GTG': 1, 'GTC': 1, 'CTA': 1, 'CTT': 1, 'CTG': 1, 'CTC': 1, 'CTA': 1, 'CTT': 1,
                  'CTG': 1,
                  'CTC': 1, 'CGA': 1, 'CGT': 1, 'CGG': 1, 'CGC': 1, 'CGA': 1, 'CGT': 1, 'CGG': 1, 'CGC': 1,
                  },
            'd': {'AAA': 1, 'AAT': 1, 'AAG': 1, 'AAC': 1, 'ATA': 1, 'ATT': 1, 'ATG': 1, 'ATC': 1, 'AGA': 1, 'AGT': 1,
                  'AGG': 1,
                  'AGC': 1, 'ACA': 1, 'ACT': 1, 'ACG': 1, 'ACC': 1, 'TAA': 1, 'TAT': 1, 'TAG': 1, 'TAC': 1, 'TAA': 1,
                  'TAT': 1,
                  'TAG': 1, 'TAC': 1, 'TAA': 1, 'TAT': 1, 'TAG': 1, 'TAC': 1, 'TAA': 1, 'TAT': 1, 'TAG': 1, 'TAC': 1,
                  'GAA': 1,
                  'GAT': 1, 'GAG': 1, 'GAC': 1, 'GTA': 1, 'GTT': 1, 'GTG': 1, 'GTC': 1, 'GTA': 1, 'GTT': 1, 'GTG': 1,
                  'GTC': 1,
                  'GTA': 1, 'GTT': 1, 'GTG': 1, 'GTC': 1, 'CTA': 1, 'CTT': 1, 'CTG': 1, 'CTC': 1, 'CTA': 1, 'CTT': 1,
                  'CTG': 1,
                  'CTC': 1, 'CGA': 1, 'CGT': 1, 'CGG': 1, 'CGC': 1, 'CGA': 1, 'CGT': 1, 'CGG': 1, 'CGC': 1,
                  },
        }

        # define param
        """
        K: k-tuple
        w: the weight between local sequence and global sequence
        lam: λ, 层级关系，即相隔λ长度之间的k-tuple核苷酸的关系
        pcf_array: 具体的特征名词数组
        pcf：∧, number of physicochemical feature
        n: 选择几元性质
        """
        self.K = K
        self.W = W
        self.lam = lam
        self.pcf_array = pcf_array
        self.pcf = len(self.pcf_array)
        self.n = n

        # other param
        """
        du_len: the length of k-tuple occurrence frequency
        tao_len: 长程序列效应的长度（每种层级关系遍历一次所有的物化性质）
        PseKNC: the final output
        L: the length of DNA sequence
        L_hat <= L - K
        """
        self.du_len = int(math.pow(4, self.K))
        self.tao_len = self.lam * self.pcf
        self.PseKNC = np.zeros(((self.du_len + self.tao_len)))
        # print(self.PseKNC.shape)
        self.seq = seq
        self.L = len(self.seq)

    def __call__(self, *args, **kwargs):
        # print("coming....")
        PseKNC2 = self.getPseKNC_1().copy()
        # print(self.PseKNC.__str__())
        # print(self.PseKNC.sum())
        # print("重置", "=" * 50)
        self.PseKNC.fill(0)
        # print(self.PseKNC.__str__())
        # print("=" * 100)
        PseKNC1 = self.getPseKNC_2()
        # print(self.PseKNC.__str__())
        # print(self.PseKNC.sum())
        # print(PseKNC1.__str__())
        # print("=" * 100)
        # print(PseKNC2.__str__())
        return PseKNC1, PseKNC2

    # 第一步：计算pow(4,K)个k-tuple元组
    def __getK_TupleIndex(self, tip: str):
        """
        4进制转换成10进制，得到该k-tuple所在的下标
        :param tip:
        :return:
        """
        index = 0
        tip_len = len(tip)
        for item in tip:
            index += int(item) * math.pow(4, tip_len - 1)
            tip_len -= 1
        return index

    def __getK_tupleCount(self):
        """
        用于对k-tuple计数，A:0, T:1, G:2, C:3,
        按照AAA，AAT，AAG，...，TTT排序,真实坐标即是4进制表示
        如果含N，则抛弃
        :return:
        """

        K_tuple_array = np.zeros(self.du_len)
        # print(K_tuple_array.shape)
        count = 0
        for j in range(self.L - self.K + 1):
            tip = self.seq[j: j + self.K]
            # print("tip:", tip)
            if tip.find('N') != -1:
                # print("遇到N")
                continue
            tip = tip.replace('A', '0')
            tip = tip.replace('T', '1')
            tip = tip.replace('G', '2')
            tip = tip.replace('C', '3')
            # print("tip_value_4:", tip)
            index = self.__getK_TupleIndex(tip)
            # print("index:", index)
            K_tuple_array[int(index)] += 1
            count += 1
        return K_tuple_array

    def __getDu_part1(self, K_tuple_array):
        """
        得到k-tuple核苷酸出现频率
        :param K_tuple_array:
        :param PseKNC:
        :return:
        """
        for index, item in enumerate(K_tuple_array, 0):
            value = item / K_tuple_array.sum()
            self.PseKNC[index] = value

    # 第二步：计算λΛ部分
    def __getPCValue(self, R_tip_left, R_tip_right, feature_name):
        """
        计算两相隔m层级远的n元核苷酸的某一物理性质的值
        :param feature_name:
        :param R_tip_left:
        :param R_tip_right:
        :return:
        """
        if self.n == 2:
            try:
                PCValue = self.PC_dic_2[feature_name][R_tip_left] * self.PC_dic_2[feature_name][R_tip_right]
            except KeyError:
                PCValue = 0
        elif self.n == 3:
            try:
                PCValue = self.PC_dic_2[feature_name][R_tip_left] * self.PC_dic_2[feature_name][R_tip_right]
            except KeyError:
                PCValue = 0
        return PCValue

    def __getSumOfJ(self, J_len, tier, feature_name):
        """
        求J_len个J的值
        :param J_len:J的个数
        :param tier:层级，从0计数
        :param feature_name:特征名称
        :return:
        """
        value = 0
        m = tier + 1
        for i in range(J_len):
            R_tip_left = self.seq[i]
            R_tip_right = self.seq[i + m]
            for r in range(1, self.n):
                R_tip_left += self.seq[i + r]
                R_tip_right += self.seq[i + m + r]
            value += self.__getPCValue(R_tip_left, R_tip_right, feature_name)
        return value

    def __getTaoArrayBeforeNormalization(self):
        """
        得到τ的np数组的原始数据，即未经过标准化
        :return:
        """
        taoArray = np.zeros(self.tao_len)
        for tier in range(self.lam):
            for pcf_index in range(self.pcf):
                # print(tier * self.pcf + pcf_index)
                taoArray[tier * self.pcf + pcf_index] = 1 / (self.L - self.K - tier - 1) * self.__getSumOfJ(
                    self.L - self.K - tier - 1, tier,
                    self.pcf_array[pcf_index])
        return taoArray

    def __getTao_part2_1(self, taoArray):
        """
        tao单独normalization
        :param taoArray:
        :return:
        """
        for index, tao_item in enumerate(taoArray):
            self.PseKNC[self.du_len + index] = tao_item / taoArray.sum()

    def __getTao_part2_2(self, taoArray):
        """
        :param taoArray:
        :return:
        """
        for index, tao_item in enumerate(taoArray):
            self.PseKNC[self.du_len + index] = self.W * tao_item

    # 第三步：得到最后的PseKNC
    def getPseKNC_1(self):
        """
        du和tao[分开独自]normalization，再依据W统一normalization
        即PseKNC数组的所有值的和是2
        这里W表示du和tao两类占的比例
        :return:
        """
        K_tuple_array = self.__getK_tupleCount()
        self.__getDu_part1(K_tuple_array=K_tuple_array)
        self.__getTao_part2_1(taoArray=self.__getTaoArrayBeforeNormalization())
        # 统一归一化
        # Sum = PseKNC.sum() / 2  # W*1 + （1-W）*1；两边都归一化了；sum一定是一
        for index, value in enumerate(self.PseKNC, 0):
            # PseKNC[index] = value / Sum
            if index < self.du_len:
                self.PseKNC[index] = value * (1 - self.W)
            else:
                self.PseKNC[index] = value * self.W
        return self.PseKNC

    # 论文中的是这种的
    def getPseKNC_2(self):
        """
        2014_Analytical Biochemistry_PseKNC - A flexible web server for generating pseudo K-tuple nucleotide composition
        2018_iTerm-PseKNC - a sequence-based tool for predicting bacterial transcriptional terminators
        du先normalization得到k-tuple核苷酸出现频率，这一部分的值的和为1；
        得到tao原始值后，再整体normalization
        即PseKNC数组的所有值的和是1
        :return:
        """
        K_tuple_array = self.__getK_tupleCount()
        self.__getDu_part1(K_tuple_array=K_tuple_array)
        self.__getTao_part2_2(taoArray=self.__getTaoArrayBeforeNormalization())
        # 统一归一化
        Sum = self.PseKNC.sum()
        for index, value in enumerate(self.PseKNC, 0):
            self.PseKNC[index] = value / Sum
        return self.PseKNC


if __name__ == '__main__':
    pseknc = PseKNC()
    PseKNC1, PseKNC2 = pseknc()
    print("=" * 100)
    print(PseKNC1)
    print("=" * 100)
    print(PseKNC2)
    # PseKNC.getPseKNC_1()
    # print(PseKNC.PseKNC.__str__())
    # print(PseKNC.PseKNC.sum())
    # print("重置", "=" * 50)
    # PseKNC.PseKNC.fill(0)
    # print(PseKNC.PseKNC.__str__())
    # print("=" * 50)
    # PseKNC.getPseKNC_2()
    # print(PseKNC.PseKNC.__str__())
    # print(PseKNC.PseKNC.sum())
