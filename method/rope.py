# import torch

# x = torch.tensor([1,2,3,4,5])
# y = torch.tensor([10,20,30,40,50])

# condition = x > 3

# result = torch.where(condition, x, y)

# print(result)


# t = torch.arange(0,20,2)
# print(t)

# t2 = torch.arange(10,0,-2)
# print(t2)

# v1 = torch.tensor([1,2,3])
# v2 = torch.tensor([4,5,6])
# result = torch.outer(v1,v2)
# print(result)

# t1=torch.tensor([[[1,2,3],[4,5,6]],[[15,16,17],[18,19,20]]])
# t2=torch.tensor([[[7,8,9],[10,11,12]],[[21,22,23],[24,25,26]]])

# print(t1.shape)

# result=torch.cat((t1,t2),dim=0)
# print(result)  

# result2=torch.cat((t1,t2),dim=1)
# print(result2)  

#-1也是同理
# result2=torch.cat((t1,t2),dim=2)  
# print(result2)  

# import torch
# t1 = torch.Tensor([1, 2, 3])
# t2 = t1.unsqueeze(0)
# print(t2)
# print(t1.shape)
# print(t2.shape)


