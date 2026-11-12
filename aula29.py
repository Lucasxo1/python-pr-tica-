#13
devs=[3200.0, 4800.0, 6500.0, 9000.0]
devs[0]=devs[0]*1.15
devs.append(7200.0)
saida=devs.pop(2)
pos=devs.index(9000.0)
extremos=devs[0]+devs[-1]
print(saida)
print(pos)
print(extremos)
print(devs)
print(len(devs))
