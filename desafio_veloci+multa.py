velocidade = float(input("Digite sua velocidade: "))
if velocidade > 80:
    print("Voce foi multado! exesso de velocidade! ")
    multa = (velocidade - 80)*7
print("voce pagara {} por excesso de velocidade".format(multa))

