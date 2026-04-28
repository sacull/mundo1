sal = float(input("Digite o seu salario "))

if sal > 1250:
    aum = sal * 1.10
if sal < 1250:
    aum = sal * 1.15

print("Quem ganhava {:.2f} passa a ganhar {:.2f}".format(sal, aum))