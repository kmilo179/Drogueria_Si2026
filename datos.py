"""Capa de datos de mi proyecto: funciones con ?, sin tablero interactivo."""
import sqlite3
from pathlib import Path

AQUI = Path(__file__).parent  # la carpeta de este archivo; nunca una ruta fija de su equipo


def conectar():
    """Abre base.db. Si no existe (p. ej. en la nube), la crea con esquema.sql y semilla.sql."""
    nueva = not (AQUI / "base.db").exists()
    conn = sqlite3.connect(AQUI / "base.db", check_same_thread=False)
    conn.execute("PRAGMA foreign_keys = ON")  # que SQLite revise las llaves foráneas
    if nueva:
        conn.executescript((AQUI / "esquema.sql").read_text(encoding="utf-8"))
        conn.executescript((AQUI / "semilla.sql").read_text(encoding="utf-8"))
        conn.commit()
    return conn


def consultar(conn, parametro):
    """Consulta (TPS): filas de mi tabla de hechos filtradas por parametro."""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT v.id_venta, m.nombre, v.cantidad, v.fecha, v.total
        FROM ventas v
        JOIN medicamentos m ON v.cod_producto = m.cod_producto
        WHERE v.cod_producto = ?
    """, (parametro,))
    filas = cursor.fetchall()
    return filas


def reportar(conn, parametro):
    """Reporte (MIS): resumen con JOIN y GROUP BY, filtrado por parametro."""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT m.categoria, m.nombre, SUM(v.cantidad) AS total_unidades, SUM(v.total) AS total_ventas
        FROM ventas v
        JOIN medicamentos m ON v.cod_producto = m.cod_producto
        WHERE v.fecha LIKE ?
        GROUP BY m.categoria, m.nombre
        ORDER BY total_unidades DESC
    """, (f"{parametro}%",))
    filas = cursor.fetchall()
    return filas


def registrar(conn, cod_producto, cantidad, fecha, total):
    """Registro (TPS): True si la base acepta la fila; False si la rechaza."""
    sql = """INSERT INTO ventas (cod_producto, cantidad, fecha, total)
            VALUES (?, ?, ?, ?)"""
    try:
        conn.execute(sql, (cod_producto, cantidad, fecha, total))
        conn.commit()
        return True
    except sqlite3.IntegrityError as error:  # la base rechazó la fila: se avisa, no se esconde
        conn.rollback()
        print("Rechazado por la base:", error)
        return False
