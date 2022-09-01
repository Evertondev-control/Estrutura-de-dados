class NodoLista: #nó da lista 
    def __init__(self,dado = 0,proximo_nodo=None): #definição(criando uma definição)
#o self é usado em classes no Python para indicar que você está referenciando alguma coisa do próprio objeto
#(sejam eles atributos ou métodos) - na verdade, (o self é o próprio objeto em si)    
        self.dado = dado
        self.proximo = proximo_nodo

class ListaEncadeada:#Esta classe representa uma lista encadeada.
    def __init__(self):
        self.cabeca = None

    def __repr__(self):
        return "[" + str(self.cabeca) + "]"