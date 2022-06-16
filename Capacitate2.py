F = 3.141516
# Area del cuadrado
def acuadrado():
    lado = int(input("Cual es el valor del lado:"))
    x=lado**2
    print('\nEl area del cuadrado es', x, 'unidades cuadradas')

# Area del triangulo
def atriangulo():
    base= int(input('Cual es el valor de la base:'))
    altura = int(input('Cual es el valor de la altura:'))
    y = base*altura/2
    print('\nEl area del triangulo es',  y,  'unidades cuadradas' )

# Area del circulo 

def acirculo():
    radio = int(input('Cual es el valor del radio:'))
    z = (F*radio)**2
    print('\nEl area del circulo es', z, 'unidades cuadradas' )

i = True
while i == True:
    area = int(input('\nElige la figura geometrica para calcuar su area \nCuadrado = 1\nTriangulo = 2\nCirculo = 3\n'))
    if area ==1:
        acuadrado()
    elif area == 2:
        atriangulo()
    elif area == 3:
        acirculo()
    else:
        print('Ingresa una opcion valida')
    
    j = input('\nQuieres calcular el area de otra figura?\nSi=True\nNo=False\n')
    if j==True:
        while j == True:
            area = int(input('\nElige la figura geometrica para calcuar su area \nCuadrado = 1\nTriangulo = 2\nCirculo = 3\n'))
            if area ==1:
                acuadrado()
            elif area == 2:
                atriangulo()
            elif area == 3:
                acirculo()
            else:
                print('Ingresa una opcion valida')
    else:
        print('\nNo deseas realizar mas calculos')
#print('\nNo deseas realizar mas calculos')