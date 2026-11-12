#19
livros=[
{"titulo": "dom casmurro", "preco": 30.0},
{"titulo": "1984", "preco": 45.0},
{"titulo": "o hobbit", "preco": 50.0}
]
livros[0]["preco"]=livros[0]["preco"]*1.10
livros.append({"titulo": "duna", "preco": 60.0})
esgotado=livros.pop(1)
dif=livros[-1]["preco"]-livros[1]["preco"]
print(esgotado)
print(dif)
print(livros)
print(len(livros))
