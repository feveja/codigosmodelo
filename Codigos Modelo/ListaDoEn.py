class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None
class ListaDolementeenlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    def estavacia(self):
        return self.primero is None
    def agregaralfinal(self,dato):
        nuevonodo = Nodo(dato)
        if self.estavacia():
            self.primero = nuevonodo
            self.ultimo = nuevonodo
        else:
            nuevonodo.anterior = self.ultimo
            self.ultimo.anterior = nuevonodo
            self.ultimo = nuevonodo
    def agregarinicio(self,dato):
        nuevonodo = Nodo(dato)
        if self.estavacia():
            self.primero = nuevonodo
            self.ultimo = nuevonodo
        else:
            nuevonodo.siguiente = self.primero
            self.ultimo.siguiente = nuevonodo
            self.ultimo = nuevonodo
    def obtenercabeza(self):
        return self.primero.dato if self.primero else None
    def obtenercola(self):
        return self.ultimo.dato if self.ultimo else None
    def existe(self,buscado):
        actual = self.primero
        while actual:
            if actual.dato == buscado:
                return True
            actual = actual.siguiente
        return False
    def eliminar(self,buscado):
        actual = self.primero
        while actual:
            if actual.dato == buscado:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.primero = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.ultimo = actual.anterior 
                break
            actual = actual.siguiente                       
    def imprimir(self):
        actual= self.primero
        while actual:
            print(actual.dato)
            actual = actual.siguiente       