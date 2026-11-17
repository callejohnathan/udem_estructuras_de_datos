# Registro de ejercicios — Estructuras de Datos / material_de_apoyo/parciales_anteriores/grafos

## Ejercicios

| ID | Título | Origen | Tratamiento | Temas (uso interno) | Dificultad | Archivo |
|----|--------|--------|-------------|---------------------|------------|---------|
| EJ-028 | Caminatas de distancia exacta | Semilla del profesor | Variación de EJ-018 (pregunta + estructura): de enumerar rutas de costo K en grafo dirigido a contar caminos simples de peso T con al menos N nodos en grafo no dirigido, sin contar dos veces una ruta y su inversa | grafo no dirigido ponderado, DFS, backtracking, caminos simples, poda por peso, conteo sin duplicar inversas | Media-alta | parcial_final_grafos_20262.ipynb |
| EJ-029 | Turnos del restaurante | Semilla de otra profesora del curso | Propuesta nueva (enunciado de la profesora adaptado al formato del curso) | grafo no dirigido como diccionario, bipartición, 2-coloreo con BFS/DFS, componentes conexas | Media | parcial_final_grafos_20262.ipynb |
| EJ-030 | Pares de nodos no alcanzables | LC 2316 (enunciado de otra profesora del curso) | Traducido (enunciado de la profesora adaptado al formato del curso) | grafo no dirigido, componentes conexas, BFS/DFS, conteo de pares con suma acumulada | Media-baja | parcial_final_grafos_20262.ipynb |

## Bitácora

### 2026-11-11 — parcial_final_grafos_20262.ipynb (parcial, nuevo)
- Agregados: EJ-028, EJ-029
- De plataformas, dados por el profesor: ninguno
- Desde semillas del profesor: EJ-028 (punto 1, del profesor), EJ-029 (punto 2, de otra profesora)
- Propuestos por Claude: ninguno
- Notas: parcial final de grafos preparado entre tres profesores; el punto 3 está pendiente (lo construye la tercera profesora). Fecha y hora límite pendientes en el encabezado. Decisiones de redacción tomadas por Claude en EJ-028: el grafo es no dirigido, la ruta no repite nodos, puede empezar en cualquier nodo, tiene al menos una arista, y una ruta y su inversa se cuentan una vez; T ≥ 1, N ≥ 2, hasta 15 nodos. EJ-029 conserva el enunciado y los ejemplos de la profesora (`posible`, `imposible`); como admite varios repartos válidos, la salida de los casos posibles es uno de ellos. Casos de estrés: en EJ-028, los dos últimos casos (K15 con pesos (i·j)%7+3, T=16 y T=15, N=5); la solución con poda por peso tarda ~0.1 s y la enumeración de todos los caminos simples sin poda no termina en tiempo razonable (K9 ya tarda 0.75 s y crece ~×10 por nodo). En EJ-029, los dos últimos casos (12 500 ciclos de 4 empleados; el segundo con un triángulo al final): BFS con conjunto/diccionario de visitados tarda ~0.03 s y la versión con lista de visitados y `pop(0)` tardó ~5 s con 20 000 empleados (cuadrática, ~30 s con 50 000). Las componentes de estrés son pequeñas a propósito para no castigar la DFS recursiva por el límite de recursión. EJ-029 incluye un caso que tumba la asignación voraz en orden del diccionario sin recorrer componentes. Todos los casos verificados con solución de referencia no incluida.

### 2026-11-13 — parcial_final_grafos_20262.ipynb (parcial, modificación)
- Agregados: EJ-030 (punto 3, que estaba pendiente)
- De plataformas: EJ-030 (LC 2316, compartido por la tercera profesora sin enlace; enunciado tal cual, traducido por ella)
- Desde semillas del profesor: ninguno
- Propuestos por Claude: ninguno
- Notas: se conservan el enunciado, el ejemplo de 7 nodos y la lista de los 14 pares de la profesora; la figura se pasó a un dibujo en texto. Restricciones agregadas por Claude (las de LC 2316): 1 ≤ n ≤ 10⁵, hasta 2·10⁵ aristas, sin lazos ni aristas repetidas. Casos de estrés: los dos últimos (n = 10⁵ sin aristas y n = 10⁵ con 50 000 componentes de dos nodos). La solución de referencia (BFS por componente y suma acumulada de tamaños) tarda ~0.05 s; la que suma tamaño_i·tamaño_j sobre todos los pares de componentes tardó 8.5 s con 2·10⁴ componentes (cuadrática, ~200 s estimados con 10⁵) y la que revisa la alcanzabilidad par por par es aún peor. Componentes pequeñas a propósito para no castigar la DFS recursiva. Las salidas superan 2³¹ (sin efecto en Python). Todos los casos verificados con solución de referencia y fuerza bruta, no incluidas. Balance: este punto es más corto que el punto 1 (conteo de caminos con backtracking); se avisó al profesor.
