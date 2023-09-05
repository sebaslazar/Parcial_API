from sodapy import Socrata


def conectar():
    try:
        client = Socrata("www.datos.gov.co", None)
        return client
    except ValueError:
        return False


def consultar_con_api(client, departamento, municipio, cultivo, limite):
    results = client.get("ch4u-f3i5", limit=limite, departamento=departamento, municipio=municipio, cultivo=cultivo)
    results_df = pd.DataFrame.from_records(results)
    results_df = results_df.filter(items=["departamento", "municipio", "cultivo", "topografia", "ph_agua_suelo_2_5_1_0",
                                          "f_sforo_p_bray_ii_mg_kg", "potasio_k_intercambiable_cmol_kg"])
    ph_mediana = pd.to_numeric(results_df["ph_agua_suelo_2_5_1_0"], errors='coerce').median()
    fosforo_mediana = pd.to_numeric(results_df["f_sforo_p_bray_ii_mg_kg"], errors='coerce').median()
    potasio_mediana = pd.to_numeric(results_df["potasio_k_intercambiable_cmol_kg"], errors='coerce').median()
    return results_df, ph_mediana, fosforo_mediana, potasio_mediana
