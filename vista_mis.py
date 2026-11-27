import matplotlib.pyplot as plt
import pandas as pd
import solara
import datos

mes_seleccionado = solara.reactive("2026-01")


@solara.component
def ReporteMIS(conn, argumento):
    solara.Select(
        label="Mes del reporte",
        value=mes_seleccionado,
        values=["2026-01", "2026-02", "2026-03"],
    )
    filas = datos.reportar(conn, mes_seleccionado.value)
    tabla = pd.DataFrame(filas, columns=["Categoria", "Medicamento", "Unidades", "Ventas"])
    
    if tabla.empty:
        solara.Info("No hay ventas registradas para este periodo.")
        return

    solara.Markdown(f"**Total de unidades vendidas:** {tabla['Unidades'].sum()}")

    alta_demanda = tabla[tabla["Unidades"] >= 5]
    if not alta_demanda.empty:
        productos = ", ".join(alta_demanda["Medicamento"])
        solara.Warning(f"Alerta de inventario: {productos} superaron las 5 unidades vendidas en el mes. Debe priorizar reabastecimiento.")

    solara.DataFrame(tabla)
    fig, ax = plt.subplots(figsize=(5, 2.5))
    ax.barh(tabla["Medicamento"], tabla["Unidades"], color="#2a6fdb")
    ax.invert_yaxis()
    ax.set_xlabel("Unidades vendidas")
    ax.spines[["top", "right"]].set_visible(False)
    solara.FigureMatplotlib(fig)
    plt.close(fig)
