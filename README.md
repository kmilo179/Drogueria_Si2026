# Drogueria Farma

**App:** (pendiente)  
**Repositorio:** https://github.com/kmilo179/Drogueria_Si2026

**Necesidad:** ¿Que tipo de medicamento se vendio más en cada mes. **Quién decide:** Gerente de inventario. **Tipo de SI:** MIS.

## Componentes del sistema de información

- **hardware:** Computador y lector de barras
- **software:** Sistema de Punto de Venta
- **datos:** Una fila = cod_producto, cantidad_vendida, fecha, total
- **personas:** Cajero y gerente de inventario
- **tic:** Red lan de la droguería y conexión a bd

## Proceso

1. El cajero registra la venta escaneando el codigo de barras
2. El sistema almacena la venta y genera un reporte de total por producto al final de cada mes
3. El gerente consulta el reporte para luego tomar decisiones.

## Cómo se usa

1. En (Consulta), ingresa el código de barras de un medicamento para poder revisar el historial de ventas. 2. En (Reporte), analiza las unidades vendidas y el total recaudado por categoría y producto en el mes. 3. En (Registrar), ingresa una nueva venta con el: (código, cantidad, fecha y total) para actualizar el sistema. Con esto, el gerente de inventario podra decidir qué medicamentos reabastecer con los proveedores.

## Datos personales (Ley 1581 de 2012)

Este sistema solo almacena los códigos de productos farmacéuticos, cantidades vendidas, fechas y precio. No almacena datos personalescumple con el principio de minimización de datos de la Ley 1581 de 2012 (Habeas Data en Colombia).

## Correr en su equipo

```
conda activate si2026
solara run app.py
```

## Uso de IA

Se utilizo inteligencia Artifical (Gemini), para identificar errores y verficiar el cumplimiento de los requisitos de la rubrica de entrega.
