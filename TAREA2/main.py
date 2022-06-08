from Lista_Doble_Circular import listaDoblementeCircular
lista= listaDoblementeCircular()


lista.insertarFinal(1)
lista.insertarFinal(4)
lista.insertarFinal(3)
lista.insertarFinal(6)
lista.insertarFinal(8)
lista.insertarFinal(9)
lista.insertarFinal(15)



lista.recorrer_inicioFin()

buscar=int(input("Ingrese el numero a buscar : "))
print("========================")
lista.buscar(buscar)
print("========================")
