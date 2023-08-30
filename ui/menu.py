import pandas as pd
from tabulate import tabulate


def pantalla_de_inicio():
    print("+---------------------------------------------------------------------------------------+")
    print("| Bienvenido al consultor de “Resultados de Análisis de Laboratorio Suelos en Colombia” |")
    print("+---------------------------------------------------------------------------------------+")


def mostrar_error(mensaje):
    if mensaje == 0:
        print("\n   -> ERROR: No se pudo establecer conexión con el sevidor...")
    elif mensaje == 1:
        print("\n   -> Los datos ingresados no se encuentran en la base de datos...")
    elif mensaje == 2:
        print("\n   -> Dato inválido.\n")
    elif mensaje == 3:
        print("\n   -> Número de registros fuera de límite.\n")


def pedir_datos():
    verificar_limite = True
    departamento = input("Ingrese el departamento: ").upper()
    municipio = input("Ingrese el municipio: ").upper()
    cultivo = input("Ingrese el cultivo: ").title()
    while verificar_limite:
        limite = input("Ingrese el número de registros (Máximo 500): ")
        if limite.isnumeric():
            if int(limite) > 500:
                mostrar_error(3)
            else:
                verificar_limite = False
        else:
            mostrar_error(2)
    return departamento, municipio, cultivo, limite


def mostrar_tabla(results_df):
    titulos = ["Departamento", "Municipio", "Cultivo", "Topografía", "Mediana de pH", "Mediana de fósforo",
               "Mediana de potasio"]
    ph_mediana = pd.to_numeric(results_df["ph_agua_suelo_2_5_1_0"], errors='coerce').median()
    fosforo_mediana = pd.to_numeric(results_df["f_sforo_p_bray_ii_mg_kg"], errors='coerce').median()
    potasio_mediana = pd.to_numeric(results_df["potasio_k_intercambiable_cmol_kg"], errors='coerce').median()

    tabla_para_mostrar = [results_df["departamento"][0], results_df["municipio"][0], results_df["cultivo"][0],
                          results_df["topografia"][0], ph_mediana, fosforo_mediana, potasio_mediana]
    print(tabulate([tabla_para_mostrar], titulos, tablefmt="pretty"))
