from collections import Counter


def cuenta_palabras(cadena):
    """Retorna un diccionario cuyas claves son todas la palabras que estén en <cadena> y sus valores
    son la cantidad de veces que aparece cada palabra en <cadena>.

    Por ejemplo si <cadena> contiene un total de 7 palabras por ejemplo:

    "hola mundo, Hola hola. Hola mundo. mundo"

    de las cuales 2 son la palabra 'hola', 2 son 'Hola' y 3 son la palabra 'mundo', retornará un
    diccionario, (no una cadena), cuya representación sería:

    {'hola': 4, 'mundo': 3}

    Observe que no se distingue entre mayúsculas y minúsculas, cualquier otro caracter se considera
    un separador de palabras."""

    diccionario = {}
    caracteres = ".,"

    for x in range(len(caracteres)):
        cadena = cadena.replace(caracteres[x], "")

    lst_palabras = cadena.split()
    """Split Divide una cadena en una lista donde cada palabra es un elemento de la lista"""
    for palabra in lst_palabras:  # recorrer las palabras dentro de la lista de palabras obtenidas de la cadena
        if palabra.lower() in diccionario:  # si la palabra  se encuentra en el diccionario se le suma 1
            diccionario[palabra.lower()] += 1
        else:  # si la palabra no se encuentra en el diccionario se le asigna 1
            diccionario[palabra] = 1

    print(diccionario)


cuenta_palabras("hola mundo, Hola hola. Hola mundo. mundo")

###########


def vuelto(cantidad_pagar, cantidad_entregada):
    """Retorna un diccionario con la cantidad de billetes y monedas que deben ser entregas como
    vuelto a un cliente.

    El proceso se hace de acuerdo a la cantidad a pagar y a la cantidad que el cliente entregó. Para
    crear el diccionario utilice el sistema monetario hondureño considerando que la cantidad de
    monedas y billetes sea lo menos posible entregando primero las denominaciones más grandes, las
    claves de los billetes en el diccionario serán números flotantes que representan la denominación
    y sus valores serán números enteros que indican la cantidad de billetes.

    Por ejemplo, si se invoca de esta manera vuelto(86.5, 100), el diccionario sería:

    {10.0: 1, 2.0: 1, 1.0: 1, 0.5: 1}
    """
    pass


def reemplazo_multiple(texto, originales, nuevos):
    """Reemplaza en <texto> las cadenas contenidas en <originales> por las las cadenas respectivas en
    <nuevos>. No se diferencia entre mayúsculas y minúsculas. Se asumen que <texto> es tipo str, y
    <originales> y <nuevos> son listas del mismo tamaño que contienen objetos tipo str.

    Por ejemplo, si <texto> es "Cinco patitos salieron a pasear...", <originales> es ["Patitos",
    "pasear"] y <nuevos> es ["gatitos", "jugar"] entonces se retorna: "Cinco gatitos salieron a
    jugar..."
    """
    pass


def elimina_columna(texto_csv, indice):
    """Recibe en <texto_csv> una str que representa un texto en formato csv, asume que el texto está
    bien formado (sin errores), se elimina un columna de este texto indicada por <indice> donde 
    la primera columna tiene un índice igual a 0.

    Se retorna <texto_csv> con la columna eliminada.
    """


dict_1 = {'valor1': 100, 'valor2': 200, 'valor3': 300}
dict_2 = {'valor2': 400, 'valor4': 12, 'valor5': 13}


def combinar_diccionarios(dict_1, dict_2):
    """Recibe dos diccionarios <dict_1> y <dict_2> con claves strings y valores numéricos
    retorna un nuevo diccionario que contiene tanto las claves y valores de <dict_1> como 
    los de <dict_2>.
    En el caso de que una clave esté presente en ambos diccionarios el valor de la misma
    en el resultado se sumará.

    """
    resultado = Counter(dict_1) + Counter(dict_2)
    print(resultado)


def invierte_diccionario(diccionario):
    """Retorna un nuevo diccinario en el cual las claves de <diccionario> son sus valores y sus
    valores son sus claves. Lanza excepción de tipo Valueerror si <diccionario> tiene valores
    repetidos.
    """
    unicos = {}
    for k, v in diccionario.items():
        if v not in unicos.values():
            unicos[k] = v
        else:
            raise ValueError(
                "Los valores estan duplicados no se puede invertir el diccionario")
    dct = {v: k for k, v in unicos.items()}
    print(dct)


def funcion_de_costo(etiquetas_predecidas, etiquetas_reales):
    """Calcula el costo como el promedio de las pérdidas para los parámetros recibidos.

    La pérdida de la instancia <i> se calcula como la función L de <etiquetas_predecidas[i]> y 
    <etiquetas_reales[i]> usando la función de pérdida vista en clase.

    Se asume que ambos parámetros recibidos son listas de números flotantes del mismo tamaño, 
    <etiquetas_predecidas> contiene números en el intervalo ]0, 1[ y <etiquetas_reales> 
    contiene números que son 0.0 o 1.0.
    """
    pass
