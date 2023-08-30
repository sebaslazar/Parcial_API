from ui import menu as ui
from api import conexion as api

ui.pantalla_de_inicio()
cliente = api.conectar()
if not cliente:
    ui.mostrar_error(0)
else:
    departamento, municipio, cultivo, limite = ui.pedir_datos()
    results_df = api.consultar_con_api(cliente, departamento, municipio, cultivo, limite)
    if results_df.empty:
        ui.mostrar_error(1)
    else:
        ui.mostrar_tabla(results_df)
