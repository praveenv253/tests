#!/usr/bin/env python3

"""
A pytorch-based test for classifying MNIST digits by following the tutorial of
Michael Nielsen ()
"""

from __future__ import print_function, division

import numpy as np
import matplotlib.pyplot as plt

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torchvision
import torchvision.transforms as transforms


class SimpleNet(nn.Module):
    """
    A simple neural network with no convolutional elements. It uses a
    fully-connected architecture with a fixed number of layers and neurons
    in each layer.
    """

    def __init__(self, num_hidden):
        """Initializes a neural network with one hidden layer."""
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(28**2, num_hidden)  # MNIST image dim is 28x28
        self.fc2 = nn.Linear(num_hidden, 10)     # 10 outputs for each digit

    def forward(self, x):
        x = x.view(-1, 28**2)
        x = F.sigmoid(self.fc1(x))
        x = F.sigmoid(self.fc2(x))
        return x


if __name__ == '__main__':
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    net = SimpleNet(30).to(device=device)

    num_epochs = 2

    transform = transforms.Compose([transforms.ToTensor(),
                                    transforms.Normalize((0.5,), (0.5,))])

    trainset = torchvision.datasets.MNIST(root='./data', train=True,
                                          download=False, transform=transform)
    trainloader = torch.utils.data.DataLoader(trainset, batch_size=10,
                                              shuffle=True, num_workers=1)
    testset = torchvision.datasets.MNIST(root='./data', train=False,
                                         download=False, transform=transform)
    testloader = torch.utils.data.DataLoader(testset, batch_size=10,
                                             shuffle=False, num_workers=1)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=0.1, momentum=0.9)

    for epoch in range(num_epochs):  # loop over the dataset multiple times

        running_loss = 0.0
        for i, data in enumerate(trainloader):
            # get the inputs; data is a list of [inputs, labels]
            inputs, labels = data

            # zero the parameter gradients
            optimizer.zero_grad()

            # forward + backward + optimize
            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            # print statistics
            running_loss += loss.item()
            if i % 1000 == 0:    # print every 2000 mini-batches
                print('[%d, %5d] loss: %.3f' %
                      (epoch + 1, i, running_loss / 1000))
                running_loss = 0.0

    print('Finished Training')

    PATH = './mnist_net.pth'
    torch.save(net.state_dict(), PATH)

    #net = SimpleNet(30)
    #net.load_state_dict(torch.load(PATH))

    correct = 0
    total = 0
    with torch.no_grad():
        for data in testloader:
            images, labels = data
            outputs = net(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    print('Accuracy of the network on the 10000 test images: %d %%'
          % (100 * correct / total))
