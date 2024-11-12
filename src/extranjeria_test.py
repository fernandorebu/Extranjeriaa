from extranjeria import *

def test_lee_datos_extranjeria(ruta_fichero: str):
    datos = lee_datos_extranjeria(ruta_fichero)
    print(len(datos),datos[:3])

def test_numero_nacionalidades_distintas(registros: str):
    datos = numero_nacionalidades_distintas(registros)
    print(datos)

def test_secciones_distritos_con_extranjeros_nacionalidades(registros, paises) -> list[tuple[str,str]]:
    datos = secciones_distritos_con_extranjeros_nacionalidades(registros, paises)
    print(len(datos), datos)

def test_total_extranjeros_por_pais(registros: list[RegistroExtranjeria]) -> dict[str,int]:
    datos = total_extranjeros_por_pais(registros) 
    print(datos)


def test_top_n_extranjeria(registros, n= 3):
        datos = top_n_extranjeria(registros, n= 3)
        print(datos)

def test_barrio_mas_multicultueral(registros):
    datos = barrio_mas_multicultueral(registros)
    print(datos)

def test_barrio_con_mas_extranjeros(registros: list[RegistroExtranjeria], tipo=None):
    datos = barrio_con_mas_extranjeros(registros, tipo)
    print(datos)    


def test_pais_mas_representado_por_districto(registros: list[RegistroExtranjeria]):
     datos = pais_mas_representado_por_districto(registros)
     print(datos)

if __name__=='__main__':
    ruta_fichero = 'data/extranjeriaSevilla.csv'
    registros = lee_datos_extranjeria(ruta_fichero)
    paises = {'ALEMANIA', 'ITALIA'}

    

    #test_lee_datos_extranjeria(ruta_fichero)
    #test_numero_nacionalidades_distintas(registros)
    #test_secciones_distritos_con_extranjeros_nacionalidades(registros, paises)
    #test_total_extranjeros_por_pais(registros)
    #test_top_n_extranjeria(registros, n= 3)
    #test_barrio_mas_multicultueral(registros)

    #test_barrio_con_mas_extranjeros(registros, tipo=None)
    #test_barrio_con_mas_extranjeros(registros, 'HOMBRES')
    #test_barrio_con_mas_extranjeros(registros, 'MUJERES')

    test_pais_mas_representado_por_districto(registros)    
