class Nodo:
    # Constructor: 
    # str int -> Nodo
    def __init__(self, nombre, rut):
        self.nombre = nombre
        self.rut = rut
        self.sgte = None
        self.ant = None
    

# Consiste en un repositorio de personas
# Se codifica como una lista circular doblemente enlazada.
class Directorio:

    def __init__(self):
        self.primero = None

    # agregarPersona: str int -> None
    # agrega una persona representada por su nombre
    # y su RUT.
    # ej: agregaPersona("Juan José",12345678)

    def agregarPersona(self, nombre, rut):
        nuevo_nodo = Nodo(nombre, rut)
        
        if self.primero is None:
            # La lista está vacía, así que inicializamos el primer nodo
            self.primero = nuevo_nodo
            self.primero.sgte = self.primero
            self.primero.ant = self.primero
        else:
            # Insertar el nuevo nodo al final de la lista circular
            ultimo = self.primero.ant
            ultimo.sgte = nuevo_nodo
            nuevo_nodo.ant = ultimo
            nuevo_nodo.sgte = self.primero
            self.primero.ant = nuevo_nodo

    # buscarPersona: int -> str
    # busca en el directorio una persona del rut 
    # ingresado y devuelte su nombre.
    # ej: buscarPersona(12345678) entrega "Juan José"

    def buscarPersona(self, rut):
        if self.primero is None:
            return "RUT NO ENCONTRADO"
        
        aux = self.primero

        while True:
            if aux.rut == rut:
                # encontramos a la persona
                return aux.nombre
            
            aux = aux.sgte

            if aux == self.primero:
                break

        return "RUT NO ENCONTRADO"

d = Directorio()
d.agregarPersona("Juan",123)
d.agregarPersona("Felipe",1234)
d.agregarPersona("Pedro",154623)
d.agregarPersona("Richard",444555)
d.agregarPersona("Mónica",66777)

print(d.buscarPersona(66777)) # imprime en pantalla "Mónica"

#Diferencias entre este y el anterior:
#Se agregaron dos atributos: sgte (siguiente) y ant (anterior) a la clase Nodo.
#Se agregó un atributo ultimo para mantener una referencia al último nodo de la lista a la clase directorio.
#Método agregarPersona:
#Se actualizan los enlaces para mantener la circularidad y doble enlace (tanto hacia adelante como hacia atrás).
#Si la lista está vacía, el primer nodo es tanto el primero como el ultimo, y se enlaza a sí mismo.
#Si la lista no está vacía, se inserta el nuevo nodo al final y se actualizan los enlaces correspondientes.
#Método buscarPersona:
#Se recorre la lista comenzando desde el primer nodo y se continúa hasta que se vuelva al primer nodo, manteniendo la circularidad.