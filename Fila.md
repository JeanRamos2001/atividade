class Nodo:
    """Esta classe representa um nodo de uma estrutura duplamente encadeada."""
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)
class Fila:
    """Esta classe representa uma fila usando uma estrutura encadeada."""
    def __init__(self):
        self.primeiro = None
        self.ultimo   = None
    def __repr__(self):
        return "[" + str(self.primeiro) + "]"
    def insere(self, novo_dado):
        """Insere um elemento no final da fila."""
        novo_nodo = Nodo(novo_dado)
        if self.primeiro == None:
            self.primeiro = novo_nodo
            self.ultimo = novo_nodo
        else:
            self.ultimo.proximo = novo_nodo
            self.ultimo = novo_nodo
    def remove(self):
        """Remove o último elemento da fila."""
        self.primeiro = self.primeiro.proximo

fila = Fila()
print("Fila vazia: ", fila)

while Fila != True:
    menu = int(input("Escolha um dos elementos a seguir:\n[1] Adicionar elemento\n[2] Remover elemnto\n[3] Imprimir fila\n[0] Sair\nDigite aqui de acordo com o numero correspondente:"))
    if menu == 1:
        var = int(input("digite um valor: "))
# Insere elementos na fila.
        fila.insere(var)
        print("Insere o valor {0} final da fila: {1}".format(var, fila), "\n")

    elif menu == 2:
        if fila.primeiro == None:
            fila = Fila()
            print("Fila vazia: ", fila, "\n")
        else:
# Remove elementos da fila.
            fila.remove()
            print("Removendo elemento que está no começo da fila: ", fila, "\n")
    elif menu == 3:
        print("A fila: ",(fila), "\n")

    elif menu == 0:
        print("Fim do programa")
        exit()
