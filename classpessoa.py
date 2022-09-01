fila=[]
inicio=1
class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade=idade
    def setNome(self,nome):
        self.nome = nome
    def setIdade(self,idade):
        self.idade
    def getNome(self):
        return self.nome
    def getIdade(self):
        return self.idade

while inicio >0:
    tempessoa=str(input("Tem pessoas para adicionar na fila? "))
    if tempessoa == "s" or tempessoa == "sim":
        nome = str(input("Insira o nome: "))
        idade=int(input("Insira a idade: "))
        pessoa=Pessoa(nome,idade)  
        fila.append(pessoa)
        for ord in range(len(fila)-1,0,-1):
            for f in range(ord):
                if fila[f].idade<fila[f+1].idade:
                    aux = fila[f]
                    fila[f] = fila[f+1]
                    fila[f+1] = aux        
    elif tempessoa != "s" or tempessoa != "sim":
        inicio=0
              
Pessoa(nome,idade)
print(pessoa)   