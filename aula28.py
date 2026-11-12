#12
carros =[45000.0, 60000.0, 85000.0, 120000.0]
carros[0]=carros[0]*0.95
carros.append(180000.0)
vendido = carros.pop(2)
pos = carros.index(120000.0)
dif=carros[-1]-carros[0]

print(vendido)
print(pos)
print(dif)
print(carros)
print(len(carros))
