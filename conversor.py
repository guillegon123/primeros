def conversion(tipo_pesos,valor_dolar): 
    pesos = input("¿Cuántos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos/valor_dolar
    dolares=round(dolares, 2)
    print("Tienes " + str(dolares) + " dolares")

menu = """ 
Bienvenido al conversor de monedas 😊💰

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Por favor Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    a = "Colombianos"
    valor = 3875
    conversion(a,valor)
elif opcion == 2:
    a = "Argentinos"
    valor = 65
    conversion(a,valor)
elif opcion == 3:
    a = "Mexicanos"
    valor = 24
    conversion(a,valor)
else:
    print("Ingresa una opción correcta por favor")


#dolares = input("¿Cuántos dolares tienes?: ")
#dolares = float(dolares)
#pesos = dolares*valor_dolar
#pesos = round(pesos,2)
#print("Tienes " + str(pesos) + " pesos colombianos")




