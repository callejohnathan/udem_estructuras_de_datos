# Sustentación individual: compresor de Huffman

Universidad de Medellín. Ingeniería de Sistemas. Estructuras de Datos. Semestre 2026-2.

El reto es individual. No se comparte información con otros estudiantes durante la sustentación. El reto tiene dos partes:

- **Parte 1**: en papel y sin computador.
- **Parte 2**: sobre el código de su proyecto.

Al terminar la parte 1, entréguele la hoja al docente antes de empezar la parte 2.

## Parte 1. Codificación a mano

El docente le asigna una de estas variantes. Cada variante es el contenido completo de un archivo: no tiene salto de línea al final, y `␣` representa un espacio.

| Variante | Texto |
|---|---|
| A | `tetera` |
| B | `rococó` |
| C | `mamá␣ama` |
| D | `cacatúa` |
| E | `coco␣loco` |
| F | `barbacoa` |

Aplique las reglas del enunciado del proyecto:

- Tiene prioridad la menor frecuencia.
- En caso de empate, tiene prioridad el menor carácter del subárbol, según su código Unicode.
- Al unir dos nodos, el primero extraído es el hijo izquierdo (agrega `0`) y el segundo es el hijo derecho (agrega `1`).

Escriba en la hoja:

1. La tabla de frecuencias, con el código Unicode de cada carácter.
2. La tabla de construcción del árbol, paso a paso: primer nodo extraído, segundo nodo extraído y nodo nuevo, cada uno con su par (frecuencia, menor carácter del subárbol).
3. El dibujo del árbol resultante.
4. La tabla de códigos, con la frecuencia y el código de cada carácter.
5. La secuencia completa de bits que resulta de codificar el texto.
6. Los bytes de la carga útil, en binario y en hexadecimal, indicando cuántos bits de relleno lleva el último byte.
7. La longitud media L en bits por carácter.

## Parte 2. Árbol por niveles

Agregue al menú de su programa una nueva opción: **Mostrar árbol por niveles**.

La opción recibe la ruta de un archivo de texto, construye el árbol de Huffman de ese archivo y lo muestra nivel por nivel. El árbol debe ser el mismo que usa su compresor para ese archivo.

Formato de salida:

- Una línea por nivel. La raíz está en el nivel 0.
- Dentro de cada nivel, los nodos van de izquierda a derecha, separados por un espacio.
- Un nodo interno se muestra como `(frecuencia)`.
- Una hoja se muestra como `'carácter':frecuencia`. Los caracteres no visibles se muestran con el mismo nombre legible que en el reporte (por ejemplo, `␣` para el espacio y `\n` para el salto de línea).
- Si el archivo está vacío, el programa muestra `El árbol está vacío.`

Ejemplo con el archivo del enunciado, cuyo contenido es `papá apaña`:

```
Nivel 0: (10)
Nivel 1: 'a':4 (6)
Nivel 2: (3) 'p':3
Nivel 3: 'ñ':1 (2)
Nivel 4: '␣':1 'á':1
```

Cuando la opción funcione:

1. Ejecútela con un archivo que contenga el texto de su variante de la parte 1.
2. Compare la salida con el árbol que dibujó a mano.
3. Compruebe que las demás opciones del menú siguen funcionando.
