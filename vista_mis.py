import matplotlib.pyplot as plt
import pandas as pd
import solara
import datos


@solara.component
def ReporteMIS(conn, argumento):
    filas = datos.reportar(conn, argumento)
    tabla = pd.DataFrame(filas, columns=["Categoria", "Medicamento", "Unidades", "Ventas"])
    solara.Markdown(f"**Total de unidades vendidas:** {tabla['Unidades'].sum()}")
    solara.DataFrame(tabla)
    fig, ax = plt.subplots(figsize=(5, 2.5))
    ax.barh(tabla["Medicamento"], tabla["Unidades"], color="#2a6fdb")
    ax.invert_yaxis()
    ax.set_xlabel("Unidades vendidas")
    ax.spines[["top", "right"]].set_visible(False)
    solara.FigureMatplotlib(fig)
    plt.close(fig)
