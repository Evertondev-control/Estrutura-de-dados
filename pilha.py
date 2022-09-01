#pilha 
#.append(elemento): adiciona elemento ao final da lista;
#.insert(índice, elemento): insere elemento após a posição índice;
#.pop(índice): remove e retorna o elemento contido na posição índice.
#ultima a entrar = primeiro a sair

pilha = [1,2,3,4,5]
print(pilha)
adc = int(input("Adicione um valor a Pilha: "))
pilha.append(adc)
print(pilha)
pilha.pop()
print(pilha)