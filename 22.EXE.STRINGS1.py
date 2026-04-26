from itertools import count

nome = str(input("Digite seu nome completo: ")).strip()
print(f"Seu nome em maiúsculas é {nome.upper()} ")
print(f"Seu nome em minúsculas é {nome.lower()} ")
print(f"Seu nome tem {len(nome)} letras")
print("Seu primeiro nome é {} e seu nome todo tem {} letras ".format(nome.split()[0],len(nome) - nome.count(' ') ))
