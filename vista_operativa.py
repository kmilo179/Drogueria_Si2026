import pandas as pd
import solara
import datos

parametro = solara.reactive('10923019231098')


@solara.component
def VistaOperativa(conn):
    solara.InputText(label="Código de producto", value=parametro)
    filas = datos.consultar(conn, parametro.value)
    solara.DataFrame(pd.DataFrame(filas, columns=["ID Venta", "Medicamento", "Cantidad", "Fecha", "Total"]))
