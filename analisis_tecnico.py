import numpy as np

def aperturas_clave_reducidas(apertura, sesiones, var):
    indices_aperturas = []

    for i in range(sesiones, len(apertura) - sesiones, 1):
        flag = 0
        cont_max_apertura = 0
        cont_min_apertura = 0
        for j in range(sesiones + 1):
            if apertura[i + j] >= apertura[i]:
                cont_max_apertura = cont_max_apertura + 1
            if apertura[i - j] >= apertura[i]:
                cont_max_apertura = cont_max_apertura + 1
            if apertura[i + j] <= apertura[i]:
                cont_min_apertura = cont_min_apertura + 1
            if apertura[i - j] <= apertura[i]:
                cont_min_apertura = cont_min_apertura + 1

        if cont_max_apertura >= 2 * (sesiones) + 1:
            indices_aperturas.append(i)
        if cont_min_apertura >= 2 * (sesiones) + 1:
            indices_aperturas.append(i)
    aperturas_clave = []

    for i in indices_aperturas:
        aperturas_clave.append(apertura[i])

    for i in range(len(indices_aperturas)):
        cont = 1
        for j in range(len(indices_aperturas)):
            if i < j and abs((apertura[indices_aperturas[i]] - apertura[indices_aperturas[j]])) < 5 * var:
                cont = cont + 1
                aperturas_clave[i] = aperturas_clave[i] + aperturas_clave[j]
                indices_aperturas[j] = 0
                aperturas_clave[j] = 0
        aperturas_clave[i] = aperturas_clave[i] / cont
    aperturas_clave_reducidas = []

    for i in range(len(indices_aperturas)):
        if indices_aperturas[i] != 0:
            aperturas_clave_reducidas.append(aperturas_clave[i])

    if np.amin(aperturas_clave_reducidas) > np.amin(apertura):
        aperturas_clave_reducidas.append(np.amin(apertura))
    if np.amax(aperturas_clave_reducidas) < np.amax(apertura):
        aperturas_clave_reducidas.append(np.amax(apertura))

    aperturas_clave_reducidas.sort()
    return aperturas_clave_reducidas;

def media_movil(apertura, periodos):
    media_movil=np.zeros(len(apertura))

    for i in range(len(apertura)):
        if i<periodos:
            media_movil[i] = apertura[i]
        if i >= periodos:
            media_movil[i] = sum(apertura[i-periodos:i])/periodos

    return media_movil;