# Registro de personas identificadas por su nombre y su RUT.
# Se implementa mediante una lista enlazada donde cada nodo de esta
# contiene el nombre y el rut de cada persona.

class Nodo:

    # Constructor: 
    # str int -> Nodo
    def __init__(self, nombre, rut, sgte=None):

        self.nombre = nombre
        self.rut = rut
        self.sgte = sgte
    

# Consiste en un repositorio de personas
# Se codifica como una lista lista enlazada.
class Directorio:

    def __init__(self):
        self.primero = None

    # agregarPersona: str int -> None
    # agrega una persona representada por su nombre
    # y su RUT.
    # ej: agregaPersona("Juan José",12345678)

    def agregarPersona(self, nombre, rut):

        self.primero = Nodo(nombre, rut, self.primero)

    # buscarPersona: int -> str
    # busca en el directorio una persona del rut 
    # ingresado y devuelte su nombre.
    # ej: buscarPersona(12345678) entrega "Juan José"

    def buscarPersona(self, rut):
        aux = self.primero

        while aux != None:

            if aux.rut == rut:
                # encontramos a la persona
                return aux.nombre
            
            aux = aux.sgte

        return "RUT NO ENCONTRADO"

d = Directorio()
d.agregarPersona("Juan",123)
d.agregarPersona("Felipe",1234)
d.agregarPersona("Pedro",154623)
d.agregarPersona("Richard",444555)
d.agregarPersona("Mónica",66777)

print(d.buscarPersona(66777)) 




#def nombreMetodo(param1, param2):
#    # instrucciones:
#    valor = 1
#    return valor
