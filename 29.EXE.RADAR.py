from traceback import print_tb

velocidade = int(input("Qual a velocidade do carro? "))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print("Você foi multado em R${:.2f}".format(multa))
else :
    print("Tenha uma boa viagem! ")