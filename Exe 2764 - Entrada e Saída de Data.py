# -*- coding: utf-8 -*-

data = (input())

#saida 1
um = data[3:5] + "/" + data[0:2] + "/" + data[6:]
dois = data[6:] + "/" + data[3:5] + "/" + data[0:2]
tres = data[0:2] + "-" + data[3:5] + "-" + data[6:]
print(um)
print(dois)
print(tres)