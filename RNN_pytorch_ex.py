import torch
from torch import nn


# x=torch.rand(1,17)
# print(x)
#
# print(x.view(1,1,-1))
#
# print(x.size())
# print(x.size(0))
# print(x.size(1))
# print(x.data)
# topv,topi=x.data.topk(1)#返回最大的两个数及对应的坐标
# print(topv,topi,topi.item())



# input=torch.randn(1,17)
# print(input)
# print(input.size())
# m=nn.LayerNorm(17)
# output=m(input)
# print(output)



#RNN
rnn=nn.RNN(10,20,2) #(each_input_size, hidden_state, num_layers)
input=torch.randn(5,3,10) # (seq_len, batch, input_size)
h0=torch.randn(2,3,20) #(num_layers * num_directions, batch, hidden_size)
output,hn=rnn(input,h0)
print(output.size(),hn.size())


#LSTM
rnn=nn.LSTM(10,20,2) #(each_input_size, hidden_state, num_layers)
input=torch.randn(5,3,10) # (seq_len, batch, input_size)
h0=torch.randn(2,3,20) #(num_layers * num_directions, batch, hidden_size)
c0=torch.randn(2,3,20) #(num_layers * num_directions, batch, hidden_size)
output,(hn,cn)=rnn(input,(h0,c0))
print(output.size(),hn.size(),cn.size())


#GRU
rnn=nn.GRU(10,20,2)
input=torch.randn(5,3,10)
h0=torch.randn(2,3,20)
output,hn=rnn(input,h0)
print(output.size(),hn.size())

























