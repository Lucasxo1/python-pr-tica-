#6
tarefas =["design", "banco de dados", "login", "teste"]
posicao = tarefas.index("login")
print(posicao)
tarefas.insert(1,"reunião")
tarefas.append("deploy")
tarefas.remove("banco de dados")
print(tarefas)
print(len(tarefas))
