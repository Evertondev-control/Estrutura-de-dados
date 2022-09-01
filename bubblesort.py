#bubble sort

def bubbleSort(lista):
    for numb in range(len(lista)-1,0,-1):
        for n in range(numb):
            if lista[n]<lista[n+1]:
                aux = lista[n]
                lista[n] = lista[n+1]
                lista[n+1] = aux

lista=[10,7,16,23,2,34,1]
bubbleSort(lista)
print(lista)