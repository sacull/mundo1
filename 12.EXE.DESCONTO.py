produto = float(input("Digite o valor do produto: "))
deconto = float(produto - (produto * 0.05))
print("O preço do produto de R$ {:.2f} com o desconto de 5% ficará em R$ {:.2f}".format(produto, deconto))