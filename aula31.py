#15
faturamento=[80.0, 150.0, 220.0, 310.0]
faturamento[0]=faturamento[0]*1.10
faturamento.append(190.0)
pago=faturamento.pop(2)
pos=faturamento.index(310.0)
total=faturamento[0]+faturamento[1]+faturamento[2]+faturamento[3]
print(pago)
print(pos)
print(total)
print(faturamento)
print(len(faturamento))
