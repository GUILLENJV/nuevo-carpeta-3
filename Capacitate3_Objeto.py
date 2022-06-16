class Persona:
    def __init__(self):
        self.edad=18
        self.nombre='Juan'
        print('Se ha creado a', self.nombre, 'de', self.edad)

    def hablar(self,palabras="No se que decir"):
        print(self.nombre,':',palabras)

juan=Persona()
juan.hablar()
juan.hablar('Hola estoy hablando')


##############
print('------------------------------------------------')

class Persona:
    def __init__(self, edad, nombre):
        self.edad=edad
        self.nombre=nombre
        print('Se ha creado a', self.nombre, 'de', self.edad)

    def hablar(self,palabras="No se que decir"):
        print(self.nombre,':',palabras)

juan=Persona(18,'Juan')
juan.hablar('Hola estoy hablando')
luis = Persona(20,'Luis')
luis.hablar('Hola estoy hablando')

######### TUPLAS EN LOS PARAMETROS ##################
print('------------------------------------------------')

class Persona:
    def __init__(self, edad, nombre):
        self.edad=edad
        self.nombre=nombre
        print('Se ha creado a', self.nombre, 'de', self.edad)

    def hablar(self,* palabras):
        for frase in palabras:
            print(self.nombre,':',frase)

juan=Persona(18,'Juan')
juan.hablar('Hola estoy hablando', 'Este soy yo ')
luis = Persona(20,'Luis')
luis.hablar('Hola estoy hablando', 'Este soy yo ')

######### DICCIONARIO  EN LOS PARAMETROS ##################

class Persona:
    def __init__(self, edad, nombre):
        self.edad=edad
        self.nombre=nombre
        print('Se ha creado a', self.nombre, 'de', self.edad)

    def hablar(self,** palabras):
        for frase in palabras:
            print(self.nombre,':',palabras[frase])

juan=Persona(30,'Juan')
juan.hablar(t1='Hola estoy hablando', t2='Este soy yo ')
luis = Persona(20,'Luis')
luis.hablar(t1='Hola estoy hablando', t2= 'Este soy yo ')


##########  EJERCICIO ############33

class Mamifero:
    def __init__(self,tipo,cola=True,garras=True):
        self.cola = cola
        self.garras = garras
        self.tipo = tipo
        self.nacer()

    def nacer(self):
        print (self.tipo,": ha nacido")

    def comer(self):
        print (self.tipo,": ha comido")

    def rugir(self):
        print (self.tipo,": ha rugido")

perro = Mamifero("perro", True,True)
perro.comer()
ballena = Mamifero("ballena",True, False)
ballena.comer()


