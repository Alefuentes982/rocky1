class Perros(object): #Declaramos la clase principal Perros
    def __init__(self, nombre): #Definimos los parámetros 
        self.__nombre = nombre #Declaramos los atributos (privados ocultos)
        #self.__peso = peso

    @property
    def nombre(self): #Definimos el método para obtener el nombre
       # "Documentación del método nombre" # Doc del método
        return self.__nombre

    @nombre.setter #Propiedad SETTER
    def nombre(self, nuevo):
        print ("Modificando nombre..")
        self.__nombre = nuevo
        print ("El nombre se ha modificado por")
        print (self.__nombre)


Rocky = Perros('Rocky')
print (Rocky.nombre)

Rocky.nombre = 'Rockycito'