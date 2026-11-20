import json
from pathlib import Path

import solara
import datos
from vista_encabezado import Encabezado
from vista_mis import ReporteMIS
from vista_operativa import VistaOperativa
from vista_registro import Registro

conn = datos.conectar()
EJEMPLOS = json.loads((Path(__file__).parent / "ejemplos.json").read_text(encoding="utf-8"))


@solara.component
def Page():
    solara.Title("Mi sistema de información")
    Encabezado()
    with solara.Columns([1, 1]):
        with solara.Card("Consulta"):
            VistaOperativa(conn)
        with solara.Card("Reporte"):
            ReporteMIS(conn, EJEMPLOS["reporte"][1][0])
    with solara.Card("Registrar"):
        Registro(conn)
