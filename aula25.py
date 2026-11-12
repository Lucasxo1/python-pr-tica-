#9
salarios =[2500, 3000, 4200, 5000]
soma =salarios[0]+salarios[1]
posicao = salarios.index(4200)
salarios.append(2000)
salarios.pop(1)
salarios[-1]=2200
print(salarios)
print(soma)
print(len(salarios))
