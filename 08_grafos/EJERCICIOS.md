# Registro de ejercicios — Estructuras de Datos / 08_grafos

## Ejercicios

| ID | Título | Origen | Tratamiento | Temas (uso interno) | Dificultad | Archivo |
|----|--------|--------|-------------|---------------------|------------|---------|
| EJ-018 | Envíos con presupuesto exacto | Semilla del profesor | Propuesta nueva (relacionado con el ejercicio 3 de taller_1.ipynb, alcanzables con costo ≤ K: cambia la pregunta a enumerar rutas con costo = K desde cualquier origen) | grafo dirigido ponderado, DFS, backtracking, caminos simples, poda | Media-alta | simulacro_parcial_grafos.ipynb |
| EJ-019 | Cierre de estaciones | Semilla del profesor | Propuesta nueva | grafo dirigido no ponderado, BFS, distancia mínima en aristas, eliminación de nodos y aristas | Media | simulacro_parcial_grafos.ipynb |

## Bitácora

### 2026-11-03 — simulacro_parcial_grafos.ipynb (simulacro, nuevo)
- Agregados: EJ-018, EJ-019
- De plataformas, dados por el profesor: ninguno
- Desde semillas del profesor: EJ-018, EJ-019
- Propuestos por Claude: ninguno
- Notas: condición del simulacro: un punto con matriz de adyacencia y otro con lista de adyacencia, a elección del estudiante. Las clases de base.py van copiadas en la primera celda de código. Decisiones de redacción tomadas por Claude: en EJ-018 la ruta puede empezar en cualquier nodo, no repite nodos y tiene al menos una arista; en EJ-019 la distancia es la mínima en número de aristas respetando el sentido, los nodos inalcanzables no se eliminan y K ≥ 1. Casos verificados con solución de referencia no incluida. Los notebooks previos de esta carpeta aún no están registrados.
