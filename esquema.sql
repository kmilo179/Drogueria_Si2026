CREATE TABLE medicamentos (
    cod_producto TEXT PRIMARY KEY,
    nombre   TEXT NOT NULL,
    categoria TEXT NOT NULL,
    precio    REAL NOT NULL
);
CREATE TABLE ventas (
    id_venta        INTEGER PRIMARY KEY,
    cod_producto  TEXT NOT NULL REFERENCES medicamentos (cod_producto),
    cantidad   INTEGER NOT NULL,
    fecha  TEXT NOT NULL,
    total REAL NOT NULL
);
