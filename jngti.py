
def ordenamiento_por_insercion(arreglo):
 
    for i in range(1, len(arreglo)):
        clave = arreglo[i]
        j = i - 1
        
        while j >= 0 and clave < arreglo[j]:
            arreglo[j + 1] = arreglo[j]
            j -= 1
            

        arreglo[j + 1] = clave
        
    return arreglo


mi_lista = [12, 11, 13, 5, 6]
print("Lista original:", mi_lista)

lista_ordenada = ordenamiento_por_insercion(mi_lista)
print("Lista ordenada:", lista_ordenada)