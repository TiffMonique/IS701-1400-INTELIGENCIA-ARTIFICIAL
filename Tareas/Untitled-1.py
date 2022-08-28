diccionario = {'valor1': 100, 'valor2': 200, 'valor3': 300, 'valor4': 300}


def invierte_diccionario(diccionario):
    """Retorna un nuevo diccinario en el cual las claves de <diccionario> son sus valores y sus
    valores son sus claves. Lanza excepción de tipo Valueerror si <diccionario> tiene valores
    repetidos.valor = 0
    unicos = diccionario
    for k, v in diccionario.items():
        if v in unicos.values():
           valor = valor +1

        if valor > 1:
            raise ValueError("Los valores estan duplicados no se puede invertir el diccionario")
        else:
             unicos[k] = v

    dct = {v: k for k, v in unicos.items()}
    print(dct)
    """
    reversed_dict = {}
    for k, v in diccionario.items():
        try:
            reversed_dict[v].append(k)
        except KeyError:
            reversed_dict[v] = [k]
            ValueError(
                "Los valores estan duplicados no se puede invertir el diccionario")
    reversed_dict[v] = [k]


invierte_diccionario(diccionario)
