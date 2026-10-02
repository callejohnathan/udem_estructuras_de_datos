# Registro de ejercicios — Estructuras de Datos / material_de_apoyo/parciales_anteriores/mixtos

Nota: los notebooks anteriores de esta carpeta (parciales y recuperaciones 2025-2 y 2026-1) son previos a este registro y sus ejercicios no están catalogados aquí.

## Ejercicios

| ID | Título | Origen | Tratamiento | Temas (uso interno) | Dificultad | Archivo |
|----|--------|--------|-------------|---------------------|------------|---------|
| EJ-001 | Fila para comprar boletas | LC 2073 | Traducido | colas, simulación | Fácil | recuperacion_listas_pilas_colas_20262.ipynb |
| EJ-002 | Emparejamiento de viajes compartidos | LC 3829 | Traducido | colas, diseño de sistema | Media | recuperacion_listas_pilas_colas_20262.ipynb |
| EJ-003 | El número más pequeño según un patrón | LC 2375 | Traducido | pilas, greedy | Media | recuperacion_listas_pilas_colas_20262.ipynb |
| EJ-004 | Invertir el comienzo de una palabra | LC 2000 | Traducido | pilas, cadenas | Fácil | recuperacion_listas_pilas_colas_20262.ipynb |
| EJ-005 | Purga de descensos | LC 2289 | Traducido (enunciado sobre lista enlazada en vez de arreglo) | listas enlazadas, simulación eficiente, pila monótona | Difícil | recuperacion_listas_pilas_colas_20262.ipynb |
| EJ-006 | Repartir una lista en partes | LC 725 | Traducido | listas enlazadas, partición | Media | recuperacion_listas_pilas_colas_20262.ipynb |

## Bitácora

### 2026-10-02 — recuperacion_listas_pilas_colas_20262.ipynb (recuperación evaluada en sesión, nuevo)
- Agregados: EJ-001, EJ-002, EJ-003, EJ-004, EJ-005, EJ-006
- De plataformas, dados por el profesor: EJ-001 (LC 2073), EJ-002 (LC 3829), EJ-003 (LC 2375), EJ-004 (LC 2000), EJ-005 (LC 2289), EJ-006 (LC 725)
- Desde semillas del profesor: ninguno
- Propuestos por Claude: ninguno
- Notas: encabezado adaptado (no se envía; evaluación en sesión hasta las 3:30 p.m.; cada punto vale 1.7 y baja 0.1 por persona hasta 1.0). Estructuras auxiliares restringidas a las del curso según el tema del punto. Sin enlaces a la fuente en el notebook. Casos de estrés (`# caso grande`): EJ-001 casos 8-11 (n=100, t=100), EJ-002 casos 8-9 (1000 operaciones), EJ-003 casos 8-10 (n=8), EJ-004 casos 8-10 (longitud 250), EJ-005 casos 9-11 (n=10^5), EJ-006 casos 8-10 (n=1000, k=50). Solo en EJ-005 los límites separan complejidades: con [10^5, 1, 2, …, 99999] la simulación ingenua O(n²) tarda 17 s con n=20001 (estimado varios minutos con n=10^5) frente a 0.006 s de la pila monótona. En EJ-001 a EJ-004 y EJ-006 los límites originales de LeetCode son pequeños y una solución ingenua también pasa. Salidas verificadas con soluciones propias y, en EJ-001, EJ-003 y EJ-005, comparadas contra fuerza bruta en entradas aleatorias.
