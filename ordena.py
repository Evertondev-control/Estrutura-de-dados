#fila ordenadada

fila =[]
filadec=[]
adc = 1

while adc != 0:
    adc = int(input("Adicione um valor para sua fila: "))
    fila.append(adc)
    filadec.append(adc)
    for ord in range(len(fila)-1,0,-1):
        for f in range(ord):
            if fila[f]>fila[f+1]:
                aux = fila[f]
                fila[f] = fila[f+1]
                fila[f+1] = aux
    for ord in range(len(filadec)-1,0,-1):
        for f in range(ord):
            if filadec[f]<filadec[f+1]:
                aux = filadec[f]
                filadec[f] = filadec[f+1]
                filadec[f+1] = aux            

print(f"Sua fila em ordem crescente{fila}")
print(f"Sua fila em ordem decrescente{filadec}")
