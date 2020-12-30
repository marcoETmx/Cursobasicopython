menu = """BIENVENIDO AL CONVERSOR DE MODEDAS

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    valor_dolar = 3875
elif opcion == 2:
    valor_dolar = 65
elif opcion == 3:
    valor_dolar = 20
else:
    print('Ingresa una opción correcta por favor')
    exit()


pesos = input("¿Cuántos pesos tienes?: ")
pesos = float(pesos)
dolares = pesos / valor_dolar
dolares = str(dolares)
print("Tienes $ " + dolares + " dólares")