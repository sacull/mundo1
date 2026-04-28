import random
import time

adivinha = random.randint(0, 5)

def processamento():
    print("\nPROCESSANDO", end="", flush=True)
    for _ in range (3):
        time.sleep(0.5)
        print(".", end="", flush=True)

print("-=-" * 12)
print("Vou pensar em um numero entre 0 e 5")
print("-=-" * 12)

num = int(input("\nEm que numero eu pensei? "))
processamento()

if num > 5 or num < 0:
    num = int(input("\nnúmero inválido, digite um número entre 0 e 5: "))


print("Pensei em {}".format(adivinha))
if num == adivinha:
    print("\nParabéns você acertou!")
else:
    print("\nVocê errou!!!")