from ast import Index
from multiprocessing.managers import Value

from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem):
        if self.head:
            # inserção quando a lista ja possui elementos
            pointer = self.head
            while (pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            # primeira inserção
            self.head = Node(elem)
        self._size += 1

    def __len__(self):
        """retorna o tamanho da lista"""
        return self._size

    def __getitem__(self, index):
         pointer = self.head
         for i in range(index):
             if pointer:
                 pointer = pointer.next
             else:
                 raise IndexError("List index out of range")
         if pointer:
             return pointer.data
         else:
             raise IndexError("List index out of range")

    def __setitem__(self, index, elem):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("List index out of range")
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("List index out of range")

    def index(self, elem):
        """Retorna o indice do elemento na lista"""
        pointer = self.head
        i = 0
        while pointer:
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i += 1
        raise ValueError(f"{elem} not found in list")

lista = LinkedList()
lista.append(10)
lista.append(20)
lista.append(30)
lista.append(40)
print(lista[3])
lista.index(30)
print(lista.index(30))
