import json
from pathlib import Path

import solara

FICHA = json.loads((Path(__file__).parent / "ficha.json").read_text(encoding="utf-8"))


@solara.component
def Encabezado():
    solara.Title(FICHA["organizacion"])

    # 1. Título con FICHA["organizacion"]; necesidad y quién decide
    solara.Markdown("#"+ FICHA['organizacion'])
    solara.Markdown("Necesidad:"+ FICHA['necesidad'])
    solara.Markdown("Quién decide:"+ FICHA['quien_decide'])

    # 2. Los cinco componentes: hardware, software, datos, personas, tic
    solara.Markdown("Hardware:" + FICHA['hardware'])
    solara.Markdown("Software:" + FICHA['software'])
    solara.Markdown("Datos:" + FICHA['datos'])
    solara.Markdown("Personas:" + FICHA['personas'])
    solara.Markdown("TIC:" + FICHA['tic'])
