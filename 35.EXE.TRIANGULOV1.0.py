


a = float(input("digite o primeiro lado "))
b = float(input("digite o segundo lado "))
c = float(input("digite o terceiro lado "))
if a < b + c and b < a + c and c < a + b:
    print("Os segmentos acima podem formar triângulo")
else:
    print("Impossivel formar um triãngulo")