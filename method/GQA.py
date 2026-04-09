import torch
import torch.nn as nn

# dropout_layer = nn.Dropout(p=0.5)

# t1=torch.Tensor([1,2,3])
# t2=dropout_layer(t1)
# # 这里Dropout丢弃了1，为了保持期望不变，将1和3扩大两倍
# print(t2)


# layer = nn.Linear(in_features=3, out_features=5, bias=True)
# t1 = torch.Tensor([1, 2, 3])  # shape: (3,)

# t2 = torch.Tensor([[1, 2, 3]])  # shape: (1, 3)
# # 这里应用的w和b是随机的，真实训练里会在optimizer上更新
# output2 = layer(t2)             # shape: (1, 5)
# print(output2)

#改变张量
# t = torch.tensor([[ 1,  2,  3,  4,  5,  6],
#                   [ 7,  8,  9, 10, 11, 12]])
# t_view1 = t.view(3, 4)
# print(t_view1)
# t_view2 = t.view(4, 3)
# print(t_view2)

#交换维度
t1=torch.Tensor([[1,2,3],[4,5,6]])
t1=t1.transpose(0,1)
print(t1)
print(t1.shape)


#reshape 和 view的区别
#view不需要复制，但需要连续的内存，reshape有时候需要复制数据，不需要连续内存，


