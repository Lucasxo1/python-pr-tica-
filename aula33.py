#17
func=[
    {"nome": "ana", "salario": 3000.0},
    {"nome": "bruno", "salario": 4500.0},
    {"nome": "carla", "salario": 6000.0}
]
func[0]["salario"]=func[0]["salario"]*1.15
func.append({"nome": "daniel", "salario": 5000.0})
desligado=func.pop(1)
dif=func[-1]["salario"]-func[1]["salario"]

print(desligado)
print(dif)
print(func)
