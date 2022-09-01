#fibonacci 
ant = 0 
prox = 1 
soma= 0
limite = int(input("Limite: "))

for a in range(0,14):
  if soma < limite:
    print(ant) 
    soma = ant + prox 
    ant = prox 
    prox = soma


