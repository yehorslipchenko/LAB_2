import DataGen
from Network import Network

InputData = [0] * 20
OutputData = [0] * 20
epoch = 10

InputData, OutputData = DataGen.generateData(InputData, OutputData)
net = Network(InputData, OutputData, 0.001)
#net.Train(InputData, OutputData)

for i in range(epoch):
    print(f"Epoch:{i}")
    InputData, OutputData = DataGen.generateData(InputData, OutputData)
    net.Train(InputData, OutputData)

