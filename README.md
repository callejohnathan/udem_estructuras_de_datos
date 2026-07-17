# Estructuras de Datos — Recursos del Curso

Este repositorio es la base de tu proceso formativo en el curso: introducciones conceptuales, implementaciones base, ejercicios y talleres, organizados en el mismo orden en que se ven en clase. Está pensado para que **descargues o clones lo que necesites cada semana y trabajes directamente sobre esos archivos**.

## 🧭 Cómo navegar el repositorio

Las carpetas numeradas (`01_...` a `07_...`) son el curso en sí, en orden. Dentro de cada una hay teoría, implementaciones base y ejercicios de ese tema. Fuera de esa numeración hay dos carpetas de apoyo:

| Carpeta | Qué contiene |
| --- | --- |
| `00_curso/` | Introducción al curso, plan del semestre, rúbricas de evaluación, reto diagnóstico y la presentación de bienvenida. Empieza por aquí. |
| `01` a `07` | El contenido de clase, un tema por carpeta, en el orden en que se dictan. |
| `material_de_apoyo/` | Parciales y prácticas **de semestres anteriores**, como referencia para estudiar. No es contenido nuevo — son evaluaciones reales ya aplicadas. |

### Orden de los temas

| Carpeta | Tema |
| --- | --- |
| `01_fundamentos_programacion/` | Variables, condicionales, ciclos, funciones (repaso antes de arrancar) |
| `02_tipos_de_datos_abstractos/` | Qué es un ADT y por qué importa la abstracción |
| `03_listas_enlazadas/` | Listas simples, dobles y circulares |
| `04_pilas_y_colas/` | Pilas, colas y colas de prioridad |
| `05_recursion/` | Recursión, call stack, recursión de cola |
| `06_arboles/` | Árboles binarios, generales y árboles de búsqueda (BST) |
| `07_grafos/` | Representación de grafos, recorridos (BFS/DFS), ordenamiento topológico |

Este orden coincide con el de `00_curso/plan_semestre.md`, así que si vas siguiendo el plan del semestre, vas siguiendo estas carpetas en el mismo orden.

## 📄 Qué significa cada nombre de archivo

Dentro de cada carpeta de tema vas a encontrar siempre el mismo tipo de archivos, nombrados de forma consistente:

| Prefijo / nombre | Qué es |
| --- | --- |
| `teoria_*.ipynb` | Introducción conceptual del tema. Explica el *por qué* antes que el *cómo*. Algunas van construyendo una implementación paso a paso como parte de la explicación — ahí sí vas a ver código ya resuelto, porque es el ejemplo guiado. |
| `base.py` | Las clases base del tema (nodos, estructuras) **ya implementadas**, con typehints. La importas en vez de reescribirla en cada notebook: `from base import ...`. Ver la sección de abajo. |
| `ejercicios_*.ipynb` | Enunciados para practicar por tu cuenta. Las celdas de código están vacías a propósito — son tu espacio de trabajo. |
| `taller_*.ipynb` | Ejercicios guiados para resolver en clase, generalmente con acompañamiento del profesor. |
| `preparatorio_*.ipynb` / `simulacro_*.ipynb` | Guías de repaso antes de un parcial. Mismo formato que un parcial real, para practicar bajo ese formato. |

**Ninguno de los notebooks de ejercicios trae la solución desarrollada.** Si necesitas revisar cómo resolver algo parecido, ese es el propósito de `material_de_apoyo/` (parciales y prácticas ya resueltas de semestres anteriores) y de las sesiones de clase.

## 🧩 Cómo usar `base.py`

Varios temas (`03`, `04`, `06`, `07`) traen un archivo `base.py` con las clases que vas a necesitar para resolver los ejercicios de esa carpeta (por ejemplo, `Stack`, `Queue`, `GraphL`, `BinaryTree`). La idea es que **no tengas que copiar y pegar la misma clase en cada notebook** — la implementas una vez (o la revisas en el notebook de teoría, donde se construye desde cero) y luego la importas donde la necesites:

```python
from base import Stack, Queue
```

Para que el `import` funcione, el notebook y el `base.py` deben estar **en la misma carpeta** — que es justo como está organizado el repo. Si descargas notebooks sueltos, asegúrate de descargar también el `base.py` de esa misma carpeta.

| Carpeta | Qué trae `base.py` |
| --- | --- |
| `03_listas_enlazadas/` | `NodeSingly`/`SinglyLinkedList`, `NodeDoubly`/`DoublyLinkedList`, `NodeCircular`/`CircularLinkedList` |
| `04_pilas_y_colas/` | `Stack`, `Queue`, `PriorityQueue` |
| `06_arboles/` | `BinaryNode`/`BinaryTree`, `BinarySearchTree`, `GeneralNode`/`GeneralTree` |
| `07_grafos/` | `GraphL`/`GraphM` (sin peso) y `GraphWL`/`GraphWM` (con peso) — lista y matriz de adyacencia, cada una soporta grafos dirigidos y no dirigidos con el parámetro `directed` |

`05_recursion` no tiene `base.py`: la recursión trabaja sobre funciones, no sobre estructuras con estado, así que no hay una clase que reutilizar entre ejercicios.

## ▶️ Cómo empezar

1. No hay dependencias externas — todo el código usa solo la librería estándar de Python (`typing`, `collections`). Cualquier entorno con Python 3 reciente (Jupyter, VS Code, Google Colab) sirve.
2. Descarga o clona la carpeta del tema que estés viendo en clase (notebooks + `base.py` si aplica).
3. Si usas Google Colab: sube también el `base.py` de esa carpeta al mismo entorno antes de correr el notebook, o monta el repo completo desde Drive/GitHub.
4. Empieza siempre por el `teoria_*.ipynb` del tema. Luego pasa a `ejercicios_*` y `taller_*`.

## 📚 Sobre `material_de_apoyo/`

Contiene parciales y prácticas **reales de semestres anteriores**, organizados por tema:

```text
material_de_apoyo/
├── parciales_anteriores/   (listas_enlazadas, pilas_y_colas, recursion, arboles, grafos, mixtos)
└── practicas_anteriores/   (listas_enlazadas, pilas_y_colas, recursion, arboles, grafos)
```

Úsalo para practicar bajo el formato real de evaluación — no para adivinar el contenido exacto del parcial de este semestre, que puede cambiar. Cuando un mismo parcial tiene versiones para distintos grupos (por ejemplo, sufijo `_grupoA` / `_grupoB`), son enunciados distintos aplicados en paralelo, no la misma pregunta repetida.

## 📊 Evaluación

El detalle completo de fechas, temas por clase y ponderaciones está en `00_curso/plan_semestre.md`. Las rúbricas de calificación (parciales, seguimiento en clase, y exención del examen final) están en `00_curso/rubrica_*.md`.

## 👋 Antes de la semana 1

`00_curso/introduccion_curso.md` reúne todo lo de la presentación de bienvenida (objetivos, metodología, acuerdos del curso, comunicación, recursos recomendados) en texto plano, y `00_curso/reto_diagnostico.ipynb` es el ejercicio de autoevaluación de fundamentos con el que arranca el curso.
