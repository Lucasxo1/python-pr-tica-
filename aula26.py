#10
salario=[1800, 2500, 3500, 5000]
salario[0] = salario[0]*1.10
salario.append(4000)
demitido = salario.pop(2)
posicao=salario.index(5000)
md=(salario[-1]+salario[-2])/2
print("demitido: ",demitido)
print("media: ",md)
print(salario)
print(len(salario))
