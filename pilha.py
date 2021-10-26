class Nodo:
    """Esta classe representa um nodo de uma estrutura encadeada."""
    def __init__(self, dado=0, nodo_anterior=None):
        self.dado = dado
        self.anterior = nodo_anterior
    def __repr__(self):
        return '%s -> %s' % (self.dado, self.anterior)
class Pilha:
    """Esta classe representa uma pilha usando uma estrutura encadeada."""
    def __init__(self):
        self.topo = None
    def __repr__(self):
        return "[" + str(self.topo) + "]"

    def insere(self, novo_dado):
        """Insere um elemento no final da pilha."""
        # Cria um novo nodo com o dado a ser armazenado.
        novo_nodo = Nodo(novo_dado)
        # Faz com que o novo nodo seja o topo da pilha.
        novo_nodo.anterior = self.topo
        # Faz com que a cabeça da lista referencie o novo nodo.
        self.topo = novo_nodo

    def remove(self):
        """Remove o elemento que está no topo da pilha."""
        self.topo = self.topo.anterior

# Cria uma pilha vazia.
pilha = Pilha()
print("Pilha vazia: ", pilha)

while Pilha != True:
    menu = int(input("Escolha um dos elementos a seguir:\n[1] Adicionar elemento\n[2] Remover elemnto\n[3] Imprimir pilha\n[0] Sair\nDigite aqui de acordo com o numero correspondente:"))
    if menu == 1:
# Insere elementos na pilha.
        var = int(input("digite um valor: "))
        pilha.insere(var)
        print("Insere o valor {0} no topo da pilha: {1}".format(var, pilha), "\n")

# Remove elementos na pilha.
    elif menu == 2:
        if pilha.topo == None:
            pilha = Pilha()
            print("Pilha vazia: ", pilha, "\n")
        else:
            pilha.remove()
            print("Removendo elemento que está no topo da pilha: ", pilha, "\n")

    elif menu == 3:
        print("A Pilha: ", (pilha), "\n")

    elif menu == 0:
        print("cabou")
        exit()

