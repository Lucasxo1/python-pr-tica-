contpar = 0
contimp = 0
num = int(input("digite um número: "))
while num != -1:
    if num %2==0:
        contpar +=1
    else:
        contimp +=1
    num = int(input("quer outro número: (-1 pra sair) "))

print(f"A quantidade de par{contpar}")
print(f"A quantidade de impar{contimp}")
