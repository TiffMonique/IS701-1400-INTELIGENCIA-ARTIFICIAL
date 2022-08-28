#Roger Ponce 20181004394


def cuenta_palabras(cadena):
  diccionario={}
  palabras= cadena.split(sep=" ")
  for i in range(len(palabras)):
    palabras[i]=palabras[i].strip(',')
    palabras[i]=palabras[i].strip('.')
    palabras[i]=palabras[i].strip('?')
    palabras[i]=palabras[i].strip('¿')
    palabras[i]=palabras[i].strip('!')
    palabras[i]=palabras[i].strip('¡')
    palabras[i]=palabras[i].lower()
  palabras_duplicadas=set(palabras)
  nueva_lista=list(palabras_duplicadas)
  for i in range(len(nueva_lista)):
    palabras.count(nueva_lista[i])
    diccionario[nueva_lista[i]] = palabras.count(nueva_lista[i])
  return diccionario

  
def vuelto_unidad(billete, vueltoTotal):
    div = vueltoTotal/billete
    if(div > 0.99):
        cantidad = int(div)
        vueltoTotal = vueltoTotal - cantidad * billete 
        return (cantidad, vueltoTotal)
    return (0, vueltoTotal)

def vuelto_billetes(vueltoTotal):
    billetes = [500, 100, 50, 20, 10, 5, 2, 1]
    billetesDict = {}
    for billete in billetes:
        cantidad, vueltoTotal = vuelto_unidad(billete, vueltoTotal)
        if( cantidad > 0):
            billetesDict[billete] = cantidad

    return [billetesDict, vueltoTotal]

def vuelto_monedas(vueltoTotal):
    vueltoTotal = vueltoTotal * 100
    monedas = [50, 20, 10, 5, 2, 1]
    monedaDict = {}
    for moneda in monedas:
        cantidad, vueltoTotal = vuelto_unidad(moneda, vueltoTotal)
        if( cantidad > 0):
            monedaDict[moneda/100] = cantidad

    return [monedaDict, vueltoTotal]


    

def vuelto(cantidad_pagar, cantidad_entregada):
  vueltoTotal=cantidad_entregada-cantidad_pagar
  billetesDict, vueltoTotal = vuelto_billetes(vueltoTotal)
  monedaDict, vueltoTotal = vuelto_monedas(vueltoTotal)
  vueltoDict = {**billetesDict, **monedaDict}
  return vueltoDict

  """vuelto=cantidad_entregada-cantidad_pagar
  diccionario={}
  if vuelto/500 >0.99:
    cantidad=int(vuelto/500)
    vuelto=vuelto-(cantidad*500)
    diccionario[500.0] = cantidad
  if vuelto/100 >0.99:
    cantidad=int(vuelto/100)
    vuelto=vuelto-(cantidad*100)
    diccionario[100.0] = cantidad
  if vuelto/50 >0.99:
    cantidad=int(vuelto/50)
    vuelto=vuelto-(cantidad*500) 
    diccionario[50.0] = cantidad 
  if vuelto/20 >0.99:
    cantidad=int(vuelto/20)
    vuelto=vuelto-(cantidad*20)
    diccionario[20.0] = cantidad
  if vuelto/10 >0.99:
    cantidad=int(vuelto/10)
    vuelto=vuelto-(cantidad*10)  
    diccionario[10.0] = cantidad
  if vuelto/5 >0.99:
    cantidad=int(vuelto/5)
    vuelto=vuelto-(cantidad*5)
    diccionario[5.0] = cantidad
  if vuelto/2 >0.99:
    cantidad=int(vuelto/2)
    vuelto=vuelto-(cantidad*2)
    diccionario[2.0] = cantidad
  if vuelto/1 >0.99:
    cantidad=int(vuelto/1)
    vuelto=vuelto-(cantidad*1)
    diccionario[1.0] = cantidad

  centavos=vuelto*100
  if centavos/50>0.99:
    cantidad=int(centavos/50)
    vuelto=vuelto-(cantidad*0.5)
    centavos=vuelto*100
    diccionario[0.5] = cantidad
  if centavos/20 > 0.99:
    cantidad=int(centavos/20)
    vuelto=vuelto-(cantidad*0.1)
    centavos=vuelto*100
    diccionario[0.2] = cantidad
  if centavos/10>0.99:
    cantidad=int(centavos/10)
    vuelto=vuelto-(cantidad*0.1)
    centavos=vuelto*100
    diccionario[0.1] = cantidad
  if centavos/5>0.99:
    cantidad=int(centavos/5)
    vuelto=vuelto-(cantidad*0.05)
    centavos=vuelto*100
    diccionario[0.05] = cantidad
  if centavos/2>0.99:
    cantidad=int(centavos/2)
    vuelto=vuelto-(cantidad*0.02)
    centavos=vuelto*100
    diccionario[0.02] = cantidad
  if centavos/1>0.99:
    cantidad=int(centavos/1)
    vuelto=vuelto-(cantidad*0.01)
    centavos=vuelto*100
    diccionario[0.01] = cantidad

  return diccionario"""
  






def reemplazo_multiple(texto, originales, nuevos):
  txt=texto.lower()
  for j in range(len(originales)):
    originales[j]=originales[j].lower()
    nuevos[j]=nuevos[j].lower()
    txt=txt.replace(originales[j],nuevos[j])
  return txt.lower()

  


def elimina_columna(texto_csv, indice):
  cadena = texto_csv.split("\n")
  for i in range (len(cadena)):
      cadena[i] = cadena[i].split(",")
      cadena[i].pop(indice)
  texto_csv = str(cadena)[1:-1]
  texto_csv = texto_csv.replace(" ","").replace("[","").replace("'","").replace("],",'\n').replace("]",'')
  texto_csv = texto_csv + "\n"
  return texto_csv

  
def combinar_diccionarios(dict_1, dict_2):
  from collections import Counter
  combinacion = ((dict(Counter(dict_1)+Counter(dict_2))))
  return combinacion


def invierte_diccionario(diccionario):
  diccionario = {v: k for k, v in diccionario.items()}
  return diccionario


def funcion_de_costo(etiquetas_predecidas, etiquetas_reales):
  import math
  y = etiquetas_reales
  y_hat = etiquetas_predecidas
  param = 0.0
  resul = 0.0
  suma = 0.0 
  for i in range(len(y)):
    if y[i] == 0:
      param = math.log(1-y_hat[i])
      resul = -(param)
      suma += resul
    else:
      if y[i] == 1:
        param = math.log(y_hat[i])
        resul = -param
        suma += resul
  y_longitud = len(y)
  prom = suma/y_longitud
  return prom
  


