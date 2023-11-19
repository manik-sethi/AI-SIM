import torch
import torch.nn as nn 
import torch.nn.functional as F

#Creating a model class that inherits nn.module



class Model(nn.Module):
    # input layer (5 features of the car) -> hidden layer 
    def __init__(self, in_features=5, h1=4, h2=3, out_features=2):
        super().__init__() # Instantiate nn.module
        ##fc stands for "fully connected", We are connecting the layers maximally to the next ones
        self.fc1=nn.Linear(in_features,h1)
        self.fc2=nn.Linear(h1,h2)
        self.out=nn.Linear(h2,out_features)
    #This function is responsible for sending fata forward
    def forward(self, x):
        #Relu is the activation function we will use
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.out(x))

        return x
    
# Pick a seed for future randomization
torch.manual_seed(69)
#Create instance of model
model = Model()