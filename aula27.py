#11
precos=[100.0, 250.0, 400.0, 800.0]
precos[1]=precos[1]*1.20
precos.append(1500.0)
esgotado =precos.pop(2)
posicao= precos.index(800.0)
md = (precos[0]+precos[-1])/2
print(esgotado)
print(posicao)
print(md)
print(precos)
print(len(precos))
