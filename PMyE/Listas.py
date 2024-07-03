class Node:
    """
    Clase que representa un nodo en una lista enlazada.
    Cada nodo contiene un valor y un enlace al siguiente nodo.
    """
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None  # Agregado para listas doblemente enlazadas

class LinkedList:
    """
    Clase que representa una lista enlazada simple.
    Proporciona métodos para insertar, eliminar y recorrer la lista.
    """
    def __init__(self): 
        self.head = None
        self.tail = None

    def insert_at_beginning(self, value): 
        """
        Inserta un nuevo nodo al principio de la lista.
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def insert_at_end(self, value):
        """
        Inserta un nuevo nodo al final de la lista.
        """
        new_node = Node(value)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def delete_node(self, value):
        """
        Elimina el primer nodo que contiene el valor especificado.
        """
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return

        current = self.head
        while current.next:
            if current.next.value == value:
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                return
            current = current.next

    def traverse(self):
        """
        Recorre la lista y muestra los valores de los nodos.
        """
        current = self.head
        while current:
            print(current.value)
            current = current.next

class DoublyLinkedList:
    """
    Clase que representa una lista enlazada doble.
    Proporciona métodos para insertar, eliminar y recorrer la lista en ambas direcciones.
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, value):
        """
        Inserta un nuevo nodo al principio de la lista.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, value):
        """
        Inserta un nuevo nodo al final de la lista.
        """
        new_node = Node(value)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete_node(self, value):
        """
        Elimina el primer nodo que contiene el valor especificado.
        """
        if self.head is None:
            return

        if self.head.value == value:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return

        current = self.head
        while current.next:
            if current.next.value == value:
                if current.next == self.tail:
                    self.tail = current
                else:
                    current.next.next.prev = current
                current.next = current.next.next
                return
            current = current.next

    def traverse_forward(self):
        """
        Recorre la lista de principio a fin y muestra los valores de los nodos.
        """
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def traverse_backward(self):
        """
        Recorre la lista de fin a principio y muestra los valores de los nodos.
        """
        current = self.tail
        while current:
            print(current.value)
            current = current.prev

class CircularLinkedList:
    """
    Clase que representa una lista enlazada circular.
    Proporciona métodos para insertar, eliminar y recorrer la lista.
    """
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        """
        Inserta un nuevo nodo al principio de la lista.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, value):
        """
        Inserta un nuevo nodo al final de la lista.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def delete_node(self, value):
        """
        Elimina el primer nodo que contiene el valor especificado.
        """
        if self.head is None:
            return

        if self.head.value == value:
            if self.head.next == self.head:
                self.head = None
                return
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            return

        current = self.head
        while current.next != self.head:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    def traverse(self):
        """
        Recorre la lista y muestra los valores de los nodos.
        """
        if self.head is None:
            return

        current = self.head
        while True:
            print(current.value)
            current = current.next
            if current == self.head:
                break
# Prueba de lista enlazada simple
print("Lista Enlazada Simple:")
simple_list = LinkedList()
simple_list.insert_at_beginning(3)
simple_list.insert_at_beginning(2)
simple_list.insert_at_beginning(1)
simple_list.insert_at_end(4)
simple_list.traverse()
print("Eliminando nodo con valor 3...")
simple_list.delete_node(3)
simple_list.traverse()
print()

# Prueba de lista enlazada doble
print("Lista Enlazada Doble:")
double_list = DoublyLinkedList()
double_list.insert_at_beginning(3)
double_list.insert_at_beginning(2)
double_list.insert_at_beginning(1)
double_list.insert_at_end(4)
double_list.traverse_forward()
print("Recorriendo en orden inverso:")
double_list.traverse_backward()
print("Eliminando nodo con valor 2...")
double_list.delete_node(2)
double_list.traverse_forward()
print()

# Prueba de lista enlazada circular
print("Lista Enlazada Circular:")
circular_list = CircularLinkedList()
circular_list.insert_at_beginning(3)
circular_list.insert_at_beginning(2)
circular_list.insert_at_beginning(1)
circular_list.insert_at_end(4)
circular_list.traverse()
print("Eliminando nodo con valor 2...")
circular_list.delete_node(2)
circular_list.traverse()