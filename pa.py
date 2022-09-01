#progressão aritmética

n = int(input("Insira o número de elementos da PA "))
p = int(input("Insira o primeiro elemento da PA "))
r = int(input("Insira a razão da PA "))

ult = p + (n-1) * r
ult = ult + 1
 
for f in range(p,ult,r):
    print(f)