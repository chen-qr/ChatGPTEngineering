import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

# Datasets
# 从云端下载训练数据和测试数据
training_data = datasets.FashionMNIST(
    root="data", # 指定数据存储的目录
    train=True,  # 指定说明是训练数据还是测试数据
    download=True, # 下载
    transform=ToTensor()
)
test_data = datasets.FashionMNIST(root="data", train=False, download=True, transform=ToTensor())

# DataLoader
batch_size = 64
train_dataloader = DataLoader(training_data, batch_size=batch_size)
test_dataloader = DataLoader(test_data, batch_size=batch_size)

for X, y in test_dataloader:
    print("Shape of X [N, C, H, W]: ", X.shape)
    print("Shape of y: ", y.shape)