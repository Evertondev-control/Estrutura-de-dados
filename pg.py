#progressão geométrica
n = int(input("Número de elementos"))
an = 0 #valor desconhecido
a1 = int(input("Primeiro valor da PG: "))#primeiro termo da sequência geométrica
q = int(input("Razão da PG: ")) #razão elevada ao número desconhecido menos 1


an = a1 * (q**(n-1))


print(an)
