# In[]
import torch

flag = torch.cuda.is_available()
print(flag)

ngpu = 1
# Decide which device we want to run on
device = torch.device("cuda:0" if (torch.cuda.is_available() and ngpu > 0) else "cpu")
print(device)
print(torch.cuda.get_device_name(0))
print(torch.rand(3, 3).cuda())

# In[]
# tf 1.x
# import tensorflow as tf
#
# tf.test.is_gpu_available()

# In[]
# tf 2.x
import tensorflow as tf
#查看tensorflow版本
print(tf.__version__)

print('GPU', tf.test.is_gpu_available())

a = tf.constant(2.0)
b = tf.constant(4.0)
print(a + b)
