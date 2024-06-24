import torch
import torch.nn as nn

class Softmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, data):
        exp_data = torch.exp(data)
        exp_sum = torch.sum(exp_data)
        return exp_data / exp_sum

class StableSoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, data):
        max_value = torch.max(data)
        stable_exp = torch.exp(data - max_value)
        exp_sum = torch.sum(stable_exp, dim=-1, keepdim=True)
        return stable_exp / exp_sum

data = torch.Tensor([1, 2, 3])
softmax = Softmax()
output = softmax(data)
print("Softmax output:", output)

stable_softmax = StableSoftmax()
output = stable_softmax(data)
print("Stable Softmax output:", output)
