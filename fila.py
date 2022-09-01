#.append(elemento): adiciona elemento ao final da lista;
#.insert(índice, elemento): insere elemento após a posição índice;
#.pop(índice): remove e retorna o elemento contido na posição índice.
adc = 1
fila = []

while adc != 0:
    adc = int(input("Adicione um valor da fila: "))
    fila.append(adc)
    print(f"{adc} Adiconado com sucesso: {fila}")



rmv = int(input("Remova um valor da fila: "))
fila.pop(rmv)
print(f"{rmv} Removido com sucesso: {fila}")



