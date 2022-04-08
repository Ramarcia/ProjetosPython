distancia =int(input("digite quantos km ate seu destino: "))

if distancia <=200:
    preço = distancia * 0.50
    print("sua viagem custara {}.".format(preço))
else  :
    preço = distancia * 0.45
    print("Com desconto sua viagem com mais de 200km custara {}.".format(preço))
print("boa viagem!")