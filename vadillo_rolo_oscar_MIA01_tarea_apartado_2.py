import re
import unicodedata

#Problema 1: Divisón de una lista de enteros.
def dividir_lista():
    lista_por_defecto = [1, -2, 0, 3, 0, 4, -5, 0, 6]
    print("Introduce la lista de números (separados por comas):")
    print("Lista por defecto:", lista_por_defecto)
    entrada_usuario = input("Ingresa tu lista (deja vacío para usar la lista por defecto): ")

    if entrada_usuario.strip() == "":
        print("Se utilizará la lista por defecto.")
        lista = lista_por_defecto
    else:
        try:
            lista = [int(x) if x.strip().lstrip('-').isdigit() else x for x in entrada_usuario.split(',')]
            print("Lista introducida:", lista)
        except ValueError:
            print("\033[91mError: la lista introducida no es válida.\033[0m")
            return
        
    resultado = separar_numeros(lista)

    print("\033[94mResultados:\033[0m")
    if resultado["negativos"]:
        print("\033[92mNegativos:\033[0m", resultado["negativos"])
    if resultado["positivos"]:
        print("\033[92mPositivos:\033[0m", resultado["positivos"])
    if resultado["noEnteros"]:
        print("\033[92mNo enteros:\033[0m", resultado["noEnteros"])
    if resultado["contador_ceros"] > 0:
        print("\033[92mCantidad de ceros:\033[0m", resultado["contador_ceros"])
    input("\033[94mPulse INTRO para continuar...\033[0m")

def separar_numeros(lista):
    resultado = {"negativos": [], "positivos": [], "noEnteros": []}
    contador_ceros = 0

    for x in lista:
        # Verificar que no se comprueben posibles elementos nulos en el listado
        if x is None:
            continue

        if isinstance(x, int):
            if x < 0:
                resultado["negativos"].append(x)
            elif x > 0:
                resultado["positivos"].append(x)
            else:
                contador_ceros += 1
        else:
            resultado["noEnteros"].append(x)

    resultado["contador_ceros"] = contador_ceros
    return resultado

#Fin problema 1

#Problema 2: Frecuencia de palabaras en un texto
def texto():
    texto_usuario = input("Ingresa una frase o párrafo para calcular la frecuencia de palabras: ")
    # Normaliza el texto y elimina las tildes
    texto_normalizado = unicodedata.normalize('NFD', texto_usuario).encode('ascii', 'ignore').decode('utf-8').lower()
    palabras = texto_normalizado.split()
    total_palabras = len(palabras)
    frecuencia_palabras = {}

    for palabra in palabras:
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        else:
            frecuencia_palabras[palabra] = 1

    while True:
        print("\033[32mIndique orden que quiere visualizar el resultado:\033[0m")
        print("1. Ordenar por palabra de forma alfabética")
        print("2. Ordenar por palabras de mayor frecuencia")
        print("3. Ordenar por palabras de menor frecuencia")
        print("4. Salir")
        orden = input("\033[94mIngresa tu elección (1, 2, 3 o 4):\033[0m")

        if orden in ["1", "2", "3"]:
            ordenar_salida_texto(frecuencia_palabras, orden, total_palabras)
        elif orden == "4":
            print("\033[91mSaliendo...\033[0m")
            break
        else:
            print("\033[91mElección inválida. Saliendo.\033[0m")
            break
        input("\033[94mPulse INTRO para continuar...\033[0m")


def ordenar_salida_texto(frecuencia_palabras, orden, total_palabras):
    sorted_frecuencia_palabras = []
    if orden == "1":
        #Ordenar por palabra de forma alfabética
        sorted_frecuencia_palabras = sorted(frecuencia_palabras.items(), key=lambda x: x[0])
    elif orden == "2":
        #Ordenar por frecuencia de mayor a menor
        sorted_frecuencia_palabras = sorted(frecuencia_palabras.items(), key=lambda x: x[1], reverse=True)
    elif orden == "3":
        #Ordenar por frecuencia de menor a mayor
        sorted_frecuencia_palabras = sorted(frecuencia_palabras.items(), key=lambda x: x[1])
    else:
        print("\033[91mElección inválida. Saliendo.\033[0m")
        return
    
    print("Frecuencia de palabras:")
    for palabra, frecuencia in sorted_frecuencia_palabras:
        porcentaje = (frecuencia / total_palabras) * 100
        print(f"{palabra}: {frecuencia} ({porcentaje:.2f}%)")

#Fin problema 2

#Problema 3: Intersección y unión de conjuntos
def conjuntos():
    # Solicitar al usuario los números para el primer conjunto
    print("Ingresa los números para el primer conjunto:")
    mensaje_numero = "\033[94mNúmero (Pulse enter para terminar): \033[0m"
    conjunto1 = set()
    iterar = True
    while iterar:
        numero = input(mensaje_numero).strip()
        if numero == "":
            iterar = False
            continue
        elif not numero.lstrip('-').isdigit():
            print("Error: Por favor, introduce un número entero.")
            continue
        conjunto1.add(int(numero))
        print("\033[92mPrimer conjunto:\033[0m", conjunto1)

    # Solicitar al usuario los números para el segundo conjunto
    print("Ingresa los números para el segundo conjunto:")
    conjunto2 = set()
    iterar = True
    while iterar:
        numero = input(mensaje_numero).strip()
        if numero == "":
            iterar = False
            continue
        elif not numero.lstrip('-').isdigit():
            print("Error: Por favor, introduce un número entero.")
            continue
        conjunto2.add(int(numero))
        print("\033[92mSegundo conjunto:\033[0m", conjunto2)

    while True:
        print("\033[32mSelecciona la operación que deseas realizar:\033[0m")
        print("1. Intersección")
        print("2. Unión")
        print("3. Diferencia simétrica")
        print("4. Salir")
        eleccion = input("\033[94mIngresa tu elección (1, 2, 3 o 4):\033[0m")

        if eleccion in ["1", "2", "3"]:
            # Mostrar los conjuntos
            print("\033[92mPrimer conjunto:\033[0m",conjunto1)
            print("\033[92mSegundo conjunto:\033[0m ",conjunto2)

        if eleccion == "1":
            interseccion = conjunto1.intersection(conjunto2)
            if interseccion:
                print("\033[93mIntersección:\033[0m", interseccion)
            else:
                print("\033[91mNo hay intersección\033[0m")
        elif eleccion == "2":
            union = conjunto1.union(conjunto2)
            if union:
                print("\033[93mUnión:\033[0m", union)
            else:
                print("\033[91mNo hay unión\033[0m")
        elif eleccion == "3":
            diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)
            if diferencia_simetrica:
                print("\033[93mDiferencia simétrica:\033[0m", diferencia_simetrica)
            else:
                print("\033[91mNo hay diferencia simétrica\033[0m")
        elif eleccion == "4":
            print("\033[91mSaliendo...\033[0m")
            break
        else:
            print("\033[91mElección inválida. Saliendo.\033[0m")
            break
        input("\033[94mPulse INTRO para continuar...\033[0m")

#Fin problema 3

def main():
    while True:
        print("\033[95mPor favor, selecciona el programa que deseas probar:\033[0m")
        print("1. Divisón de una lista de enteros")
        print("2. Frecuencia de palabaras en un texto")
        print("3. Intersección y unión de conjuntos")
        print("4. Salir")

        eleccion = input("\033[94mIngresa tu elección (1, 2, 3 o 4):\033[0m")

        if eleccion == "1":
            dividir_lista()
        elif eleccion == "2":
            texto()
        elif eleccion == "3":
            conjuntos()
        elif eleccion == "4":
            print("\033[91mSaliendo...\033[0m")
            break
        else:
            print("\033[91mElección inválida. Saliendo.\033[0m")
            break


if __name__ == "__main__":
    main()


