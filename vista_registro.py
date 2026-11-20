import inspect
import json
from pathlib import Path

import solara
import datos

EJ = json.loads((Path(__file__).parent / "ejemplos.json").read_text(encoding="utf-8"))
REGISTRO = getattr(datos, EJ["registro_valido"][0])
CAMPOS = list(inspect.signature(REGISTRO).parameters)[1:]
campos = {c: solara.reactive("") for c in CAMPOS}
mensaje = solara.reactive("")


def procesar(conn, valores):
    "Valida y registra. Devuelve 'Registrado' o 'Rechazado:"
    if any(str(x).strip() == "" for x in valores.values()):
        return "Rechazado: no deben quedar campos vacios"
    try:
        cantidad = int(valores["cantidad"])
        total = float(valores["total"])
    except ValueError:
        return "Rechazado: La cantidad y total deben ser números"
    if cantidad <= 0 or total <= 0:
        return "Rechazado: La cantidad y total deben ser mayores a 0"
    ok = datos.registrar(conn, valores["cod_producto"], cantidad, valores["fecha"], total)
    return "Registrado" if ok else "Rechazado por la base, el código de producto no existe"


@solara.component
def Registro(conn):
    for nombre, estado in campos.items():
        solara.InputText(nombre, value=estado)
    def guardar():
        mensaje.set(procesar(conn, {k: e.value for k, e in campos.items()}))
    solara.Button("Guardar", on_click=guardar, color="primary")
    solara.Markdown(mensaje.value)
