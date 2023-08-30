from ui import menu as ui
from api import conexion as api


def main():
    ejecutar = True
    ui.pantalla_de_inicio()
    while ejecutar:
        cliente = api.conectar()
        if not cliente:
            ui.mostrar_error(0)
            ejecutar = False
        else:
            departamento, municipio, cultivo, limite = ui.pedir_datos()
            results_df = api.consultar_con_api(cliente, departamento, municipio, cultivo, limite)
            if results_df.empty:
                ui.mostrar_error(1)
            else:
                respuesta = ui.mostrar_tabla(results_df)
                if respuesta == "N":
                    ejecutar = False


main()
