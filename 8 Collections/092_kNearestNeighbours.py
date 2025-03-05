import operator


def distanciaEuclidiana(a, b):
    if (len(a) is not len(b)):
        raise Exception('Longitudes de a, b deben ser iguales')
    return pow(sum([(a[i] - b[i]) ** 2 for i in range(len(a))]), 0.5)


def knn(datos, clases, k, x):
    distancias = [-1] * len(datos)
    for i in range(len(datos)):
        distancias[i] = (datos[i], distanciaEuclidiana(datos[i], x), clases[i])
    distancias.sort(key = operator.itemgetter(1))
    cercanos = distancias[0:k]
    clases = {}
    for c in cercanos:
        if not c[2] in clases:
            clases[c[2]] = 1
        else:
            clases[c[2]] += 1
    return max(clases.items(), key=operator.itemgetter(1))[0]



datos = [(1,1), (1,0), (4,5), (3,3)]
clases = [0, 0, 1, 1]




print(str(knn(datos, clases, 3, (0, 0))))
print(str(knn(datos, clases, 3, (5, 5))))
