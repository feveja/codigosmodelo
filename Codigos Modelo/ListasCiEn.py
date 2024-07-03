class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaCircularSimple:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def esta_vacia(self):
        return self.primero is None

    def obtener_cabeza(self):
        return self.primero.dato if self.primero else None

    def obtener_cola(self):
        return self.ultimo.dato if self.ultimo else None

    def agregar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
            nuevo_nodo.siguiente = self.primero
        else:
            nuevo_nodo.siguiente = self.primero
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo

    def agregar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
            nuevo_nodo.siguiente = self.primero
        else:
            nuevo_nodo.siguiente = self.primero
            self.primero = nuevo_nodo
            self.ultimo.siguiente = self.primero

    def imprimir_lista(self):
        if self.esta_vacia():
            print("La lista está vacía.")
        else:
            actual = self.primero
            while True:
                print(actual.dato, end=" ")
                actual = actual.siguiente
                if actual == self.primero:
                    break
            print()
    def existe(self, dato):
        if self.esta_vacia():
            return False
        actual = self.primero
        while True:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
            if actual == self.primero:
                break
        return False

    def eliminar(self, dato):
        if self.esta_vacia():
            return
        if self.primero.dato == dato:
            if self.primero == self.ultimo:
                self.primero = None
                self.ultimo = None
            else:
                self.ultimo.siguiente = self.primero.siguiente
                self.primero = self.primero.siguiente
        else:
            anterior = self.primero
            actual = self.primero.siguiente
            while True:
                if actual.dato == dato:
                    if actual == self.ultimo:
                        self.ultimo = anterior
                    anterior.siguiente = actual.siguiente
                    break
                anterior = actual
                actual = actual.siguiente
                if actual == self.primero:
                    break
