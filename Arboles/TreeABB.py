class Node:
    def __init__(self, data):
        """
        Inicializa un nuevo nodo con el valor 'data' y establece
        los punteros 'left' y 'right' a None.
        """
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        """
        Inicializa un nuevo árbol de búsqueda binaria con la raíz establecida a None.
        """
        self.root = None

    def insert(self, data):
        """
        Inserta un nuevo nodo con el valor 'data' en el árbol.
        Si el árbol está vacío, crea un nuevo nodo y lo establece como la raíz.
        De lo contrario, llama al método '_insert' para insertar el nodo en la posición correcta.
        """
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        """
        Método auxiliar que realiza la inserción recursiva de un nodo en el árbol.
        Compara el valor 'data' con el valor del nodo actual y lo inserta en el
        subárbol izquierdo o derecho, según corresponda.
        """
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)

    def search(self, data):
        """
        Busca un valor 'data' en el árbol. Llama al método '_search'
        para realizar la búsqueda.
        """
        return self._search(data, self.root)

    def _search(self, data, node):
        """
        Método auxiliar que realiza la búsqueda recursiva de un valor 'data' en el árbol.
        Compara el valor 'data' con el valor del nodo actual y continúa la búsqueda en
        el subárbol izquierdo o derecho, según corresponda.
        """
        if node is None:
            return False
        elif data == node.data:
            return True
        elif data < node.data:
            return self._search(data, node.left)
        else:
            return self._search(data, node.right)

    def preorder_traversal(self):
        """
        Realiza un recorrido en preorden (Raíz-Izquierda-Derecha) del árbol.
        """
        return self._preorder_traversal(self.root)

    def _preorder_traversal(self, node):
        """
        Método auxiliar que realiza el recorrido en preorden de forma recursiva.
        """
        if node is None:
            return []
        result = [node.data]
        result.extend(self._preorder_traversal(node.left))
        result.extend(self._preorder_traversal(node.right))
        return result

    def inorder_traversal(self):
        """
        Realiza un recorrido en inorden (Izquierda-Raíz-Derecha) del árbol.
        """
        return self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        """
        Método auxiliar que realiza el recorrido en inorden de forma recursiva.
        """
        if node is None:
            return []
        result = self._inorder_traversal(node.left)
        result.append(node.data)
        result.extend(self._inorder_traversal(node.right))
        return result

    def postorder_traversal(self):
        """
        Realiza un recorrido en postorden (Izquierda-Derecha-Raíz) del árbol.
        """
        return self._postorder_traversal(self.root)

    def _postorder_traversal(self, node):
        """
        Método auxiliar que realiza el recorrido en postorden de forma recursiva.
        """
        if node is None:
            return []
        result = self._postorder_traversal(node.left)
        result.extend(self._postorder_traversal(node.right))
        result.append(node.data)
        return result

    def level_order_traversal(self):
        """
        Realiza un recorrido por niveles (anchura) del árbol.
        """
        if self.root is None:
            return []
        queue = [self.root]
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result
# Crear un árbol de búsqueda binaria
bst = BinarySearchTree()

# Insertar elementos en el árbol
bst.insert(21)
bst.insert(13)
bst.insert(33)
bst.insert(10)
bst.insert(18)
bst.insert(25)
bst.insert(40)

# Recorrido en preorden
print("Recorrido en preorden:")
print(bst.preorder_traversal())  # Salida: [5, 3, 1, 4, 7, 6, 8]

# Recorrido en inorden
print("\nRecorrido en inorden:")
print(bst.inorder_traversal())  # Salida: [1, 3, 4, 5, 6, 7, 8]

# Recorrido en postorden
print("\nRecorrido en postorden:")
print(bst.postorder_traversal())  # Salida: [1, 4, 3, 6, 8, 7, 5]

# Recorrido por niveles
print("\nRecorrido por niveles:")
print(bst.level_order_traversal())  # Salida: [5, 3, 7, 1, 4, 6, 8]

# Búsqueda de elementos
print("\nBúsqueda de elementos:")
print(bst.search(40))  # True
print(bst.search(9))  # False
#Otro ejemplo
bst1 = BinarySearchTree()
bst1.insert(68)
bst1.insert(35)
bst1.insert(90)
bst1.insert(30)
bst1.insert(60)
bst1.insert(70)
bst1.insert(98)
bst1.insert(10)
bst1.insert(54)
bst1.insert(65)
bst1.insert(92)
bst1.insert(99)

# Recorrido en preorden
print("Recorrido en preorden:")
print(bst1.preorder_traversal())  

# Recorrido en inorden
print("\nRecorrido en inorden:")
print(bst1.inorder_traversal())  

# Recorrido en postorden
print("\nRecorrido en postorden:")
print(bst1.postorder_traversal())  
# Recorrido por niveles
print("\nRecorrido por niveles:")
print(bst1.level_order_traversal()) 
