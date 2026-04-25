medida = float(input("Digite a medida em metros: "))
cm = float(medida * 100)
milimetro = float(medida * 1000)
print("Você digitou {:.2f} em metros, que é equivalente a {:.2f} cm, {:.2f} mm ".format(medida, cm, milimetro))