#23
pets=[
{"raca": "poodle", "peso": 8.0},
{"raca": "beagle", "peso": 12.0},
{"raca": "labrador", "peso": 30.0}
]
pets[0]["peso"]=pets[0]["peso"]*1.15
pets.append({"raca": "pug", "peso": 7.0})
adotado=pets.pop(1)
soma=pets[0]["peso"]+pets[-1]["peso"]
print(adotado)
print(soma)
print(pets)
print(len(pets))
