# Tarea 1

Lista1= ['Motor','Frenos','Transmision', ['Bateria','Cableado','Luces']]
Lista1[1]='Direccion'
Lista1[3][1]='Motor de arranque'
print(Lista1)

# Tarea 2 

diccionaro1 ={'D1':(1,2,3),
              'D2':['casa', 'cama', 4, 'peo'],
              'D3':'La familia unida',
              'D4':['casa', 'cama', 4, 'peo']
}
print(diccionaro1)

# Tarea 3 

a = input('Comes Frutas:')
a = True
#a = False
if a == True:
    x = int(input('Cuantas veces a la semana comes frutas:'))
    if x>=5:
        print('Sigue asi')
    elif x>2 and x<5:
        print('Come mas frutas a la semana')
    elif x<=2:
        print('Necesitas comer frutas')
else:
    print('Necesitas comer fruta')