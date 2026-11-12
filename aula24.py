#8
vendas =["tv", "geladeira", "fogão", "notebook"]
posicao= vendas.index("fogão")
vendas.append("celular")
vendas.insert(0, "videogame")
vendas.remove("fogão")
vendas[-1]="tabelet"
print(posicao)
print(vendas)
print(len(vendas))
