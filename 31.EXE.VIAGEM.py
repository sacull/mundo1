distancia=int(input("Digite a distancia da viagem: "))
if distancia<=200:
    distancia=distancia*0.50
    print("Sua passagem vai custar apenas {:.2f}".format(distancia))
else :
    distancia = distancia * 0.45
    print("Sua passagem está com preço promocional e vai custar apenas {:.2f}".format(distancia))
