from node import Node

class LinkedList:
    def __init__(self):
        self.head = None # Cabeça da lista (primeiro nó)

    # Método para verificar se a lista está vazia
    def is_empty(self):
        return self.head is None

    # Método para adicionar um nó ao início da lista
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Método para adicionar um nó ao final da lista
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Método para buscar um nó na lista
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def remove(self, data):
        """Método para remover um nó específico da lista"""
        current = self.head
        previous = None
        while current:
            if current.data == data:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return
            previous = current
            current = current.next
        print(f"Nó com dado {data} não encontrado.")

    # Método para exibir a lista
    def display(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        print(" -> ".join(nodes))

    # Método para obter o tamanho da lista
    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def remove_first(self):
        """Método para remover o primeiro nó da lista"""
        if not self.is_empty():
            self.head = self.head.next
        else:
            print("A lista está vazia.")

    def remove_last(self):
        """Método para remover o ultimo nó da lista"""
        if self.is_empty():
            print("A lista está vazia.")
            return
        if self.head.next is None:
            self.head = None
            return
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

# Exemplo de uso
lista = LinkedList()
lista.insert_at_end(10)
lista.insert_at_end(20)
lista.insert_at_end(30)
lista.insert_at_start(5)
lista.display() # Output esperado: 5 -> 10 -> 20 -> 30
print("Tamanho da lista:", lista.size()) # Output esperado: 4

lista.remove(20)
lista.display() # Output esperado: 5 -> 10 -> 30
nodo = lista.search(10)
print(f"Nó encontrado: {nodo.data}") if nodo else print("Nó não encontrado.")
lista.remove_first()
lista.display() # Output esperado: 10 -> 30
lista.remove_last()
lista.display() # Output esperado: 10