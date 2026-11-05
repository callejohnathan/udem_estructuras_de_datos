# Registro de ejercicios — Estructuras de Datos / material_de_apoyo/practicas_anteriores/arboles/practica_arboles_20262

Nota: el enunciado del proyecto (`práctica_árboles_20262.html`) es previo a este registro y no se cataloga como ejercicio.

## Ejercicios

| ID | Título | Origen | Tratamiento | Temas (uso interno) | Dificultad | Archivo |
|----|--------|--------|-------------|---------------------|------------|---------|
| EJ-020 | Codificación a mano | Propio | Propuesta nueva | árboles de Huffman, cola de prioridad, desempate, empaquetado de bits | Fácil | sustentacion_reto.md |
| EJ-021 | Árbol por niveles | Semilla del profesor | Propuesta nueva | recorrido por niveles, colas, árboles binarios | Fácil | sustentacion_reto.md |

## Bitácora

### 2026-11-04 — sustentacion_reto.md y sustentacion_guia_docente.md (sustentación individual, nuevo)
- Agregados: EJ-020, EJ-021
- De plataformas, dados por el profesor: ninguno
- Desde semillas del profesor: EJ-020 (idea del profesor: codificación a mano de una palabra), EJ-021 (mostrar los nodos por nivel como nueva opción del menú)
- Propuestos por Claude: ninguno
- Notas: EJ-020 tiene 6 variantes (A `tetera`, B `rococó`, C `mamá ama`, D `cacatúa`, E `coco loco`, F `barbacoa`), elegidas para que cada una tenga al menos un empate decidido por el menor carácter. Las soluciones y las salidas esperadas de EJ-021 están en `sustentacion_guia_docente.md` y se calcularon con una implementación de referencia que reproduce el ejemplo del enunciado (0xDD 0xD3 0x40, L = 2.1). La guía docente contiene las respuestas: no publicarla antes de terminar las sustentaciones. Sin casos de estrés: es un ejercicio de sustentación en vivo.

### 2026-11-04 — archivos_prueba/ (sustentación individual, nuevo)
- Agregados: ninguno (material de apoyo para la sustentación, no son ejercicios)
- Notas: `prueba_sustentacion_1.txt` (295 caracteres, 60 símbolos, 320 bytes; `\r\n`, tabulador, tildes y un emoji de 4 bytes) y `prueba_sustentacion_2.txt` (71 049 caracteres, 343 símbolos, `e` repetida 70 004 veces). Generados por script en binario para conservar `\r\n`. Los valores esperados del reporte están en `sustentacion_guia_docente.md` y se calcularon con la implementación de referencia.
