# Registro de ejercicios — Estructuras de Datos / material_de_apoyo/parciales_anteriores/recursion

Nota: los parciales anteriores de esta carpeta (2025-2 y 2026-1) son previos a este registro y sus ejercicios no están catalogados aquí.

## Ejercicios

| ID | Título | Origen | Tratamiento | Temas (uso interno) | Dificultad | Archivo |
|----|--------|--------|-------------|---------------------|------------|---------|
| EJ-007 | Unir dos listas ordenadas | LC 21 | Variación de LC 21 (estructura: listas de Python en vez de listas enlazadas) | recursión, mezcla de secuencias ordenadas | Fácil | parcial_recursion_20262.ipynb |
| EJ-008 | Contando unos | LC 233 | Traducido (con penalización del 50 % si convierte a cadena) | recursión, aritmética de dígitos | Difícil | parcial_recursion_20262.ipynb |
| EJ-009 | Columna de caracteres | Semilla del profesor | Propuesta nueva | recursión sobre listas, cadenas | Fácil | parcial_recursion_20262.ipynb |

## Bitácora

### 2026-10-07 — parcial_recursion_20262.ipynb (parcial, nuevo)
- Agregados: EJ-007, EJ-008, EJ-009
- De plataformas, dados por el profesor: EJ-007 (LC 21, como variación de estructura), EJ-008 (LC 233, traducido)
- Desde semillas del profesor: EJ-009
- Propuestos por Claude: ninguno
- Notas: parcial del 2026-10-08, envío por correo antes de las 8:50 a.m. (EDD62) o 9:50 a.m. (EDD61). Regla general: soluciones recursivas, sin ciclos ni comprensiones. En EJ-008, convertir a cadena se califica sobre el 50 %. En EJ-009 se asumió k ≥ 0 contado desde 0 y se limitó la lista a 500 cadenas para no superar el límite de recursión de Python. Dificultad desbalanceada (EJ-008 bastante más difícil que EJ-007 y EJ-009); el profesor decidió dejarla así. Sin enlaces a la fuente en el notebook. Casos de estrés (`# caso grande`): EJ-007 casos 8–9 (50 + 50 elementos); EJ-008 casos 10–12 (n hasta 10^9: contar número por número es inviable, ~10^9 iteraciones y además supera la profundidad de recursión); EJ-009 casos 9–11 (500 cadenas, k = 99 o 100). Salidas verificadas con soluciones propias: EJ-008 por posición decimal comparada contra conteo directo para n < 3000 y 30 valores aleatorios hasta 10^6, y además con una solución recursiva sin str; EJ-007 y EJ-009 con soluciones recursivas sin ciclos dentro del límite de recursión por defecto.
