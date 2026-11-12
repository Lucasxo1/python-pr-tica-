#14
tanques=[1500.0, 3200.0, 4500.0, 6000.0]
tanques[0]=tanques[0]*1.25
tanques.append(2500.0)
esgostado=tanques.pop(2)
valor=tanques.index(6000.0)
dif=tanques[-1]-tanques[1]
print(esgostado)
print(valor)
print(dif)
print(tanques)
print(len(tanques))
