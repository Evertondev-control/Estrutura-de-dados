#Triangulos Exercicio

a = float(input("Indique a medida do lado A: "))
b = float(input("Indique a medida do lado B: "))
c = float(input("Indique a medida do lado C: "))

print(f"Medida A: {a} , Medida B: {b} , Medida c: {c}.")

if a == b and b == c and c == a:
  print(f"Este é um triângulo é Equilátero")
elif a == b or b == c or c == a:
  print(f"Este é um triângulo isóceles ")
elif a != b != c:
  print(f"Este é um triângulo Escaleno")