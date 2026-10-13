# Registro de ejercicios — Estructuras de Datos / 04_listas_enlazadas

Nota: los notebooks anteriores de esta carpeta (ejercicios_1, ejercicios_2, taller_1, taller_2, taller_3_listas_enlazadas, taller_3_transicion_pilas_colas, teoría) son previos a este registro y sus ejercicios no están catalogados aquí.

## Ejercicios

| ID | Título | Origen | Tratamiento | Temas (uso interno) | Dificultad | Archivo |
|----|--------|--------|-------------|---------------------|------------|---------|
| EJ-016 | Análisis de complejidad de cinco fragmentos | Propio (monitoría) | Propuesta nueva | notación O: O(1), O(n), O(n²), O(log n), término dominante | Fácil | taller_1_listas_enlazadas_monitoria.ipynb |
| EJ-017 | Implementación guiada de la lista simplemente enlazada | Propio (monitoría) | Propuesta nueva | lista enlazada simple: append con tail, borrar primero y último, casos borde | Fácil | taller_1_listas_enlazadas_monitoria.ipynb |

## Bitácora

### 2026-10-13 — taller_1_listas_enlazadas_monitoria.ipynb (taller de monitoría, Samuel Romaña; agregado al repo)
- Agregados: EJ-016, EJ-017
- De plataformas, dados por el profesor: ninguno
- Desde semillas del profesor: ninguno
- Propuestos por Claude: ninguno
- Notas: llegó como Taller_Listas_Enlazadas.ipynb. Correcciones al subirlo: "[Tu Nombre]" → "Samuel Romaña Acevedo"; el esqueleto tenía una clase SinglyLinkedList anidada dentro de otra (los métodos con TODO quedaban en la interna y __repr__/__len__ fallaban en la externa), se dejó una sola clase. Mismo día: en taller_3_listas_enlazadas.ipynb (taller 2 de la monitoría) se agregó __len__ a CircularLinkedList; no se subieron las soluciones hechas en clase porque tenían errores (ej. 1 retornaba sin borrar con cualquier lista no vacía; ej. 2 daba True para 1 ⇄ 2 ⇄ 3 ⇄ 4).
