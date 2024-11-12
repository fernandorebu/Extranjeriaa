from typing import NamedTuple
import csv
 
RegistroExtranjeria = NamedTuple('RegistroExtranjeria', 
                                    [
                                        ("distrito", str),
                                        ("seccion", str),
                                        ("barrio", str),
                                        ("pais", str),
                                        ("hombres", int),
                                        ("mujeres", int)
                                    ])
 
def lee_datos_extranjeria(ruta_fichero: str) -> list[RegistroExtranjeria]:
    lista = []
    with open(ruta_fichero, encoding='utf-8')as f:
        lector = csv.reader(f)
        next(lector)
        for districto, seccion, barrio, pais, hombres, mujeres in lector:
            hombres = int(hombres)
            mujeres = int(mujeres)
            Registro = RegistroExtranjeria(districto, seccion, barrio, pais, hombres, mujeres)
            lista.append(Registro)
    return lista
 
def numero_nacionalidades_distintas(registros: list[RegistroExtranjeria]) -> int:
    conjunto = set()
    for r in registros:
        conjunto.add(r.pais)
    return len(conjunto)
 
def secciones_distritos_con_extranjeros_nacionalidades(
                    registros: list[RegistroExtranjeria],
                     paises: set[str]) -> list[tuple[str,str]]: 
    conjunto = set()
    for r in registros:
        if r.pais in paises:
            conjunto.add((r.distrito, r.seccion))
    return sorted(conjunto)
 
#Cuando tu haces un valor logico en los diccionarios en realidad estas preguntado por los valores
def total_extranjeros_por_pais(registros: list[RegistroExtranjeria]) -> dict[str,int]:
    res = {}
    for r in registros:
        if r.pais not in res:
            res[r.pais]  = 0
        res[r.pais] += r.hombres + r.mujeres
        
    return res 

#A partir de ahora voyu ausar el itemaas para pasar los diccionarios a tuplas

def top_n_extranjeria(registros, n= 3):
    datos = total_extranjeros_por_pais(registros)
    res = sorted(datos.items(), key = lambda t:t[1], reverse= True)
    return res[:n]

def barrio_mas_multicultueral(registros: list[RegistroExtranjeria]) -> dict[str,set[str]]:
    res = {}
    for r in registros:
        if r.barrio not in res:
            res[r.barrio] = set()
        res[r.barrio].add(r.pais)  #Esto se va ejecutar siempre
    return max(res.items(), key=lambda t:len(t[1]))[0] #He puesto el [0] porque solo quiero el primer elemento de la tupla





def barrio_con_mas_extranjeros(registros: list[RegistroExtranjeria], tipo=None):
    res = {}
    for r in registros:
        if tipo == 'HOMBRES':
            valor = r.hombres
        elif tipo == 'MUJERES':
            valor = r.mujeres
        else:
            valor = r.hombres + r.mujeres


        if r.barrio not in res:
            res[r.barrio]  = 0
        res[r.barrio] += valor 
        
    return max(res.items(), key=lambda t:t[1])[0]

#ULTIMO APARTADO (Hice funcion aux)

def pais_mas_representado_por_districto(registros: list[RegistroExtranjeria]):
    res = {}
    for r in registros:
        valor = max_extranjero_pais(registros, r.distrito)
        if r.distrito not in res:
            res[r.distrito] = valor
    return res

def max_extranjero_pais(registros: list[RegistroExtranjeria], districto):
    res = {}
    for r in registros:
        if r.distrito == districto:
            if r.pais not in res:
                res[r.pais] = 0
            res[r.pais] += r.mujeres + r.hombres
    return max(res.items(), key = lambda t:t[1])[0]


    