a = int(input(" Digite o primeiro número "))
b = int(input(" Digite o segundo "))
c = int(input(" Digite o terceiro "))
menor = a
maior = b

if b < c and b < a:
    menor = b
if c < b and c < a:
    menor = c

if a > b and a > c:
    maior = a
if c > a and c > b:
    maior = c

print("O maior número digitado foi {}".format(maior))
print("O menor número digitado foi {}".format(menor))
