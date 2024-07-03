class Nodo:
    dato = None
    siguiente = None
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None
class ListaEnlazada:
    def __init__(self):
        self.inicio = None
        self.fin = None
    def agregar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.fin is None:
            self.inicio = nuevo_nodo
            self.fin = nuevo_nodo
        else:
            self.fin.siguiente = nuevo_nodo
            self.fin = nuevo_nodo
    def agregar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.inicio is None:
            self.inicio = nuevo_nodo
            self.fin = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.inicio
            self.inicio = nuevo_nodo
    def imprimir_lista(self):
        if self.inicio is None:
            print("La lista está vacía.")
        else:
            actual = self.inicio
            while actual is not None:
                print(actual.dato, end=" ")
                actual = actual.siguiente
            print()
    def existe(self, dato):
        actual = self.inicio
        while actual is not None:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False
    def eliminar(self, dato):
        if self.inicio is None:
            return
        if self.inicio.dato == dato:
            if self.inicio == self.fin:
                self.inicio = None
                self.fin = None
            else:
                self.inicio = self.inicio.siguiente
        else:
            anterior = self.inicio
            actual = self.inicio.siguiente
            while actual is not None:
                if actual.dato == dato:
                    if actual == self.fin:
                        self.fin = anterior
                    anterior.siguiente = actual.siguiente
                    return
                anterior = actual
                actual = actual.siguiente