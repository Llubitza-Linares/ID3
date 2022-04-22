
# /usr/bin/env python
# -*- coding:utf-8 -*-
 


def createC1(dataSet):
    '''
         Este método consiste en obtener un conjunto de elementos con 1 elemento, es decir, un conjunto de elementos.
    '''
         C1 = [] # Conjunto de elementos con 1 elemento (conjunto de elementos poco frecuente, porque no se ha comparado con el soporte mínimo)
    for transaction in dataSet:
        for item in transaction:
            if [item] not in C1:
                C1.append([item])
    C1.sort()
         return map (frozenset, C1) #Convertir C1 de una lista de Python a un conjunto invariante (frozenset, una estructura de datos en Python)
 
 
def scanD(D, Ck, minSupport):
    '''
         Donde D es el conjunto de datos completo (una colección de todos los registros de transacciones).
         Ck es un conjunto candidato de tamaño k (que contiene k elementos). Por ejemplo, si contiene un elemento, entonces Ck es C1, y así sucesivamente.
         minSupport es el soporte mínimo establecido.
         Este método se utiliza para filtrar los conjuntos de elementos frecuentes más grandes que minupport
    '''
         ssCnt = {} #Almacenar todos los elementos combinados aleatoriamente (1 conjunto de elementos, 2 conjuntos de elementos, etc.) y el número de ocurrencias de un subconjunto de registros de transacciones
    for tid in D:
        for can in Ck:
            if can.issubset(tid):
                ssCnt[can] = ssCnt.get(can, 0) + 1
    numItems = float(len(D))
         retList = [] #retList es el conjunto de elementos frecuentes que se encuentra en Ck (el soporte es mayor que minSupport)
         supportData = {} #supportData registra el soporte de cada conjunto de elementos frecuentes
    for key in ssCnt:
        if support >= minSupport:
            retList.insert(0, key)
            supportData[key] = support
    return retList, supportData
 
 
def aprioriGen(Lk, k):
    '''
         Esta función genera un conjunto de elementos candidatos C (k + 1) a través de la lista de conjuntos de elementos frecuentes Lk y el número de conjuntos de elementos k.
         Todos los conjuntos binomiales formados por la combinación libre de un conjunto de elementos, si el primer elemento de dos conjuntos binomiales es igual, se generan tres conjuntos de elementos.
         Tenga en cuenta que en el proceso de generación, cada conjunto de elementos se ordena primero por elemento y luego se comparan dos conjuntos de elementos cada vez.
         Los dos elementos se combinan solo cuando los primeros elementos k-1 son iguales. Esto se hace porque la función no fusiona las colecciones en pares.
         No todos los conjuntos generados de esa manera tienen k + 1 elementos.
         Bajo la premisa de que el número de elementos restringidos es k + 1, solo cuando los primeros k-1 elementos son iguales y el último elemento es diferente, la combinación puede ser el nuevo conjunto de elementos candidatos requerido.
    '''
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i + 1, lenLk):
                         # Cuando los primeros elementos k-2 sean iguales, combine los dos conjuntos
                         L1 = lista (Lk [i]) [: k-2] #Convierte el conjunto en una lista y toma rodajas. Por ejemplo, el conjunto ([1,3]) se convierte en una lista y se convierte en [1,3]
            L2 = list(Lk[j])[:k-2]
            L1.sort()
            L2.sort()
            if L1 == L2:
                                 retList.append (Lk [i] | Lk [j]) # Encuentra la unión del conjunto y agrégala a retList
    return retList
 
 
def apriori(dataSet,minSupport=0.5):
    '''
         Función total
    '''
    C1 = createC1(dataSet)
    D = map(set, dataSet)
    L1, supportData = scanD(D, C1, minSupport)
    L = [L1]
    k = 2
    while (len(L[k-2]) > 0):
        Ck = aprioriGen(L[k-2], k)
        Lk, supK = scanD(D, Ck, minSupport)
        supportData.update(supK)
        L.append(Lk)
        k += 1
    return L,supportData
