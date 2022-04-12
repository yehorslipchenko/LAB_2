import DataGen
from Network import Network

InputData = [0] * 20
OutputData = [0] * 20
epoch = 10

InputData, OutputData = DataGen.generateData(InputData, OutputData)
net = Network(InputData, OutputData, 0.0001)
net.Initialize()
net.Train(InputData, OutputData)

for i in range(epoch):
    print(f"Epoch:{i + 1}")
    DataGen.Shuffle(InputData, OutputData)
    net.Train(InputData, OutputData)

InputData, OutputData = DataGen.generateData(InputData, OutputData)
net.Test(InputData, OutputData)



