from math import radians, sin, cos, tan
an = float(input("Digite o ângulo: "))
seno = sin(radians(an))
print("O ângulo {} tem o seno: {:.2f} " .format(an,seno))
cos = cos(radians(an))
print("O ângulo {} tem o cosseno de: {:.2f} " .format(an,cos))
tan = tan(radians(an))
print("O ângulo de {} tem a tangente de: {:.2f} " .format(an,tan))