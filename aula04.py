num = 67
tentantivas = 1
palp = int(input("dê seu palpite: "))
while palp != num:
    palp = int(input("Dê outro palpite: "))
    tentantivas +=1
    if palp == num:
        print("parabéns, você acertou!! ")
    elif palp >num:
        print("MENOS!!!")
    else:
        print("MAIS!!!")

print(f"suas tentativas até acertar: {tentantivas}")
