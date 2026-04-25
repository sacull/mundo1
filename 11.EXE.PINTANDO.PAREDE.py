largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))
area = largura * altura
print("Sua parede tem a dimensão de {}x{} e sua àrea é de {}m².".format(largura, altura, area))
tinta = area / 2
print("Para pintar essa parede, você precisará de {} de tinta." .format(tinta))
