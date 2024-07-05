import matplotlib.pyplot as plt
import networkx as nx
class Nodo:
    def __init__(self, dato):
        """
        Inicializa un nuevo nodo con el valor 'dato' y establece
        los punteros 'izquierdo' y 'derecho' a None.
        """
        self.dato = dato
        self.izquierdo = None
        self.derecho = None

class ArbolBinarioBusqueda:
    def __init__(self):
        """
        Inicializa un nuevo árbol de búsqueda binaria con la raíz establecida a None.
        """
        self.raiz = None

    def insertar(self, dato):
        """
        Inserta un nuevo nodo con el valor 'dato' en el árbol.
        Si el árbol está vacío, crea un nuevo nodo y lo establece como la raíz.
        De lo contrario, llama al método '_insertar' para insertar el nodo en la posición correcta.
        """
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self._insertar(dato, self.raiz)

    def _insertar(self, dato, nodo):
        """
        Método auxiliar que realiza la inserción recursiva de un nodo en el árbol.
        Compara el valor 'dato' con el valor del nodo actual y lo inserta en el
        subárbol izquierdo o derecho, según corresponda.
        """
        if dato < nodo.dato:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(dato)
            else:
                self._insertar(dato, nodo.izquierdo)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(dato)
            else:
                self._insertar(dato, nodo.derecho)

    def buscar(self, dato):
        """
        Busca un valor 'dato' en el árbol. Llama al método '_buscar'
        para realizar la búsqueda.
        """
        return self._buscar(dato, self.raiz)

    def _buscar(self, dato, nodo):
        """
        Método auxiliar que realiza la búsqueda recursiva de un valor 'dato' en el árbol.
        Compara el valor 'dato' con el valor del nodo actual y continúa la búsqueda en
        el subárbol izquierdo o derecho, según corresponda.
        """
        if nodo is None:
            return False
        elif dato == nodo.dato:
            return True
        elif dato < nodo.dato:
            return self._buscar(dato, nodo.izquierdo)
        else:
            return self._buscar(dato, nodo.derecho)

    def recorrido_preorden(self):
        """
        Realiza un recorrido en preorden (Raíz-Izquierda-Derecha) del árbol.
        """
        return self._recorrido_preorden(self.raiz)

    def _recorrido_preorden(self, nodo):
        """
        Método auxiliar que realiza el recorrido en preorden de forma recursiva.
        """
        if nodo is None:
            return []
        resultado = [nodo.dato]
        resultado.extend(self._recorrido_preorden(nodo.izquierdo))
        resultado.extend(self._recorrido_preorden(nodo.derecho))
        return resultado

    def recorrido_inorden(self):
        """
        Realiza un recorrido en inorden (Izquierda-Raíz-Derecha) del árbol.
        """
        return self._recorrido_inorden(self.raiz)

    def _recorrido_inorden(self, nodo):
        """
        Método auxiliar que realiza el recorrido en inorden de forma recursiva.
        """
        if nodo is None:
            return []
        resultado = self._recorrido_inorden(nodo.izquierdo)
        resultado.append(nodo.dato)
        resultado.extend(self._recorrido_inorden(nodo.derecho))
        return resultado

    def recorrido_postorden(self):
        """
        Realiza un recorrido en postorden (Izquierda-Derecha-Raíz) del árbol.
        """
        return self._recorrido_postorden(self.raiz)

    def _recorrido_postorden(self, nodo):
        """
        Método auxiliar que realiza el recorrido en postorden de forma recursiva.
        """
        if nodo is None:
            return []
        resultado = self._recorrido_postorden(nodo.izquierdo)
        resultado.extend(self._recorrido_postorden(nodo.derecho))
        resultado.append(nodo.dato)
        return resultado

    def recorrido_por_niveles(self):
        """
        Realiza un recorrido por niveles (anchura) del árbol.
        """
        if self.raiz is None:
            return []
        cola = [self.raiz]
        resultado = []
        while cola:
            nodo = cola.pop(0)
            resultado.append(nodo.dato)
            if nodo.izquierdo:
                cola.append(nodo.izquierdo)
            if nodo.derecho:
                cola.append(nodo.derecho)
        return resultado

    def numero_total_nodos(self):
        """
        Retorna el número total de nodos en el árbol.
        """
        return self._numero_total_nodos(self.raiz)

    def _numero_total_nodos(self, nodo):
        """
        Método auxiliar que cuenta el número de nodos de forma recursiva.
        """
        if nodo is None:
            return 0
        return 1 + self._numero_total_nodos(nodo.izquierdo) + self._numero_total_nodos(nodo.derecho)

    def valor_maximo(self):
        """
        Retorna el valor máximo almacenado en el árbol.
        """
        if self.raiz is None:
            return None
        return self._valor_maximo(self.raiz)
    def _valor_maximo(self, nodo):
        """
        Método auxiliar que encuentra el valor máximo de forma recursiva.
        """
        current = nodo
        while current.derecho is not None:
            current = current.derecho
        return current.dato
    def altura(self):
        """
        Retorna la altura del árbol.
        """
        return self._altura(self.raiz)

    def _altura(self, nodo):
        """
        Método auxiliar que calcula la altura de forma recursiva.
        """
        if nodo is None:
            return 0
        altura_izquierda = self._altura(nodo.izquierdo)
        altura_derecha = self._altura(nodo.derecho)
        return 1 + max(altura_izquierda, altura_derecha)
    def mostrar_graficamente(self):
        def agregar_nodos_y_aristas(nodo, graph, pos=None, x=0, y=0, layer=1):
            if pos is None:
                pos = {}
            pos[nodo.dato] = (x, y)
            if nodo.izquierdo:
                graph.add_edge(nodo.dato, nodo.izquierdo.dato)
                l = x - 1 / layer
                agregar_nodos_y_aristas(nodo.izquierdo, graph, pos=pos, x=l, y=y-1, layer=layer+1)
            if nodo.derecho:
                graph.add_edge(nodo.dato, nodo.derecho.dato)
                r = x + 1 / layer
                agregar_nodos_y_aristas(nodo.derecho, graph, pos=pos, x=r, y=y-1, layer=layer+1)
            return graph, pos
        
        if self.raiz is None:
            print("El árbol está vacío.")
            return

        graph = nx.DiGraph()
        graph, pos = agregar_nodos_y_aristas(self.raiz, graph)
        
        fig, ax = plt.subplots(figsize=(12, 8))
        nx.draw(graph, pos, with_labels=True, arrows=False, node_size=5000, node_color="skyblue", ax=ax)
        plt.show()
# Crear un árbol de búsqueda binaria
abb = ArbolBinarioBusqueda()

# Insertar elementos en el árbol
abb.insertar(21)
abb.insertar(13)
abb.insertar(33)
abb.insertar(10)
abb.insertar(18)
abb.insertar(25)
abb.insertar(40)
# Mostrar el árbol gráficamente
abb.mostrar_graficamente()

# Cantidad de nodos
print("Número total de nodos:", abb.numero_total_nodos())

# Valor máximo
print("Valor máximo:", abb.valor_maximo())

# Altura
print("Altura del árbol:", abb.altura())

# Recorrido en preorden
print("\nRecorrido en preorden:")
print(abb.recorrido_preorden())

# Recorrido en inorden
print("\nRecorrido en inorden:")
print(abb.recorrido_inorden())

# Recorrido en postorden
print("\nRecorrido en postorden:")
print(abb.recorrido_postorden())

# Recorrido por niveles
print("\nRecorrido por niveles:")
print(abb.recorrido_por_niveles())

# Búsqueda de elementos
print("\nBúsqueda de elementos:")
print("Buscar 40:", abb.buscar(40))  # True
print("Buscar 9:", abb.buscar(9))  # False

# Otro ejemplo
abb1 = ArbolBinarioBusqueda()
abb1.insertar(68)
abb1.insertar(35)
abb1.insertar(90)
abb1.insertar(30)
abb1.insertar(60)
abb1.insertar(70)
abb1.insertar(98)
abb1.insertar(10)
abb1.insertar(54)
abb1.insertar(65)
abb1.insertar(92)
abb1.insertar(99)
# Mostrar el árbol gráficamente
abb1.mostrar_graficamente()
# Recorrido en preorden
print("\nRecorrido en preorden:")
print(abb1.recorrido_preorden())

# Recorrido en inorden
print("\nRecorrido en inorden:")
print(abb1.recorrido_inorden())

# Recorrido en postorden
print("\nRecorrido en postorden:")
print(abb1.recorrido_postorden())

# Recorrido por niveles
print("\nRecorrido por niveles:")
print(abb1.recorrido_por_niveles())

# Otro árbol
abb2 = ArbolBinarioBusqueda()
abb2.insertar(1)
abb2.insertar(2)
abb2.insertar(3)
abb2.insertar(4)
abb2.insertar(5)
abb2.insertar(6)
abb2.insertar(7)
abb2.insertar(8)
abb2.insertar(9)
abb2.insertar(10)
abb2.insertar(11)
abb2.insertar(12)
abb2.insertar(13)
abb2.insertar(14)
abb2.insertar(15)
abb2.insertar(16)
abb2.insertar(17)
abb2.insertar(18)
abb2.insertar(19)
# Mostrar el árbol gráficamente
abb2.mostrar_graficamente()

