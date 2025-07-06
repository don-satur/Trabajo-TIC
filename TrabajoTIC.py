print("Hola Profesor!!")

listaNombres = ["Tomas", "Alejo","David","Luci"]
Notas = [8,6,7,10]
Total = len(listaNombres)
####MENU####
print("El Profesor debera elegir entre estas opciones.")
print("-----MENU-----")
print("Op1. Imprimir Nombres Alumnos")
print("Op2. Imprimir Notas")
print("Op3. Imprimir Total Alumnos")
opcion = input("Elegir Opción: ")
while True:
    if opcion == "1":
        print(f"Los nombres de los alumnos son: {listaNombres}")
        break
    elif opcion == "2":
        print(f"Las notas de los alumnos son: {Notas}")
        break
    elif opcion == "3": 
        print(f"La cantidad de alumnos es: {Total}")
        break
    else: print("Opcion incorrecta, seleccionar de nuevo")