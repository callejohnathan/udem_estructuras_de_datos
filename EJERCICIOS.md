# Índice de ejercicios — Estructuras de Datos

| ID | Origen | Idea central | Carpeta |
|----|--------|--------------|---------|
| EJ-001 | LC 2073 | Simular fila circular donde cada uno compra una boleta y vuelve al final; tiempo hasta que termina la persona k (o suma de min(t[i], t[k]) / min(t[i], t[k]-1)) | material_de_apoyo/parciales_anteriores/mixtos |
| EJ-002 | LC 3829 | Dos colas FIFO (conductores y pasajeros) emparejadas por orden de llegada, con cancelación de un pasajero en espera | material_de_apoyo/parciales_anteriores/mixtos |
| EJ-003 | LC 2375 | Menor número con dígitos 1-9 sin repetir que cumple patrón I/D: apilar índices y vaciar la pila en cada 'I' y al final | material_de_apoyo/parciales_anteriores/mixtos |
| EJ-004 | LC 2000 | Invertir el prefijo hasta la primera aparición de un carácter usando una pila | material_de_apoyo/parciales_anteriores/mixtos |
| EJ-005 | LC 2289 | Pasos de eliminación simultánea de nodos menores que su anterior: simulación en lista enlazada revisando solo vecinos afectados, o pila monótona con el paso en que cae cada elemento | material_de_apoyo/parciales_anteriores/mixtos |
| EJ-006 | LC 725 | Partir una lista enlazada en k partes consecutivas de tamaños n//k (+1 para las primeras n%k) cortando enlaces | material_de_apoyo/parciales_anteriores/mixtos |
| EJ-007 | LC 21 (var.) | Mezclar recursivamente dos listas de Python ordenadas comparando las cabezas y avanzando en la que tiene el menor | material_de_apoyo/parciales_anteriores/recursion |
| EJ-008 | LC 233 | Contar los dígitos 1 de 0 a n descomponiendo por el dígito más significativo (o por posición decimal) sin convertir a cadena | material_de_apoyo/parciales_anteriores/recursion |
| EJ-009 | Semilla del profesor | Recorrer recursivamente una lista de cadenas tomando el carácter k de cada una o "XXX" si la posición no existe | material_de_apoyo/parciales_anteriores/recursion |
| EJ-010 | Propio (monitoría) | Recorrer recursivamente una lista anidada de profundidad variable con índice, multiplicando los impares | 06_recursion |
| EJ-011 | Propio (monitoría) | Recorrer una cadena con índice y omitir las letras seguidas de un dígito impar | 06_recursion |
| EJ-012 | Propio (monitoría) | Contar con recursión de cola y acumulador los dígitos de n mayores que k usando % 10 y // 10 | 06_recursion |
| EJ-013 | Propio (monitoría) | Recorrer una matriz en zigzag por filas con recursión que lleva fila, columna y dirección | 06_recursion |
| EJ-014 | Propio (monitoría) | Eliminar vocales cuyos vecinos izquierdo y derecho son la misma consonante, recorriendo con índice | 06_recursion |
| EJ-015 | Propio (monitoría) | Verificar que los dígitos de n alternan paridad comparando el último dígito con el siguiente vía % 10 y // 10 | 06_recursion |
| EJ-016 | Propio (monitoría) | Determinar la complejidad O de cinco fragmentos de código (acceso directo, recorrido, doble ciclo, división por 2, suma de partes) | 04_listas_enlazadas |
| EJ-017 | Propio (monitoría) | Completar la lista simplemente enlazada con head/tail/size: append en O(1), borrar primero y último manejando lista vacía y de un elemento | 04_listas_enlazadas |
| EJ-018 | Semilla del profesor | Enumerar todos los caminos simples (cualquier origen, ≥1 arista) de un grafo dirigido ponderado cuyo peso suma exactamente K, con DFS y backtracking podando cuando la suma supera K | 08_grafos |
| EJ-019 | Semilla del profesor | En un grafo dirigido no ponderado, calcular distancias mínimas en aristas desde N (BFS) y eliminar los nodos a distancia exactamente K junto con sus aristas entrantes y salientes | 08_grafos |
| EJ-020 | Propio | Construir a mano el árbol de Huffman de una palabra corta con desempate por (frecuencia, menor carácter Unicode del subárbol), y obtener códigos, bits, bytes con relleno y L | material_de_apoyo/practicas_anteriores/arboles/practica_arboles_20262 |
| EJ-021 | Semilla del profesor | Recorrer por niveles (BFS con cola) el árbol de Huffman generado y mostrar los nodos de cada nivel de izquierda a derecha | material_de_apoyo/practicas_anteriores/arboles/practica_arboles_20262 |
| EJ-022 | LC 1342 (var.) | Reducir n recursivamente (par: n//2; impar: n-1) acumulando la secuencia de valores hasta 0 | material_de_apoyo/parciales_anteriores/mixtos |
| EJ-023 | LC 394 (var.) | Calcular la longitud de una cadena con repeticiones anidadas k[...] sin expandirla: cada bloque resuelve su contenido por recursión y multiplica | material_de_apoyo/parciales_anteriores/mixtos |
| EJ-024 | LC 2243 (var.) | Rondas de reemplazo de bloques de k dígitos por su suma, con recursión anidada por rondas, bloques y dígitos, devolviendo cada ronda | material_de_apoyo/parciales_anteriores/mixtos |
| EJ-025 | LC 938 (var.) | Suma y cantidad de valores de un BST en [L, R], descartando subárboles según el orden del BST | material_de_apoyo/parciales_anteriores/mixtos |
| EJ-026 | LC 543 (var.) | Diámetro de un árbol general: en cada nodo combinar las dos alturas mayores de sus hijos mientras la recursión devuelve la altura | material_de_apoyo/parciales_anteriores/mixtos |
| EJ-027 | LC 2641 (var.) | Reemplazar cada nodo por el máximo de sus primos: BFS por niveles guardando los máximos de las dos mejores familias de cada nivel | material_de_apoyo/parciales_anteriores/mixtos |
