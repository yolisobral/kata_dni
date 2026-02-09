 Proyecto realizado por:
- [Dalila Teodosio](https://github.com/DalilaManu)
- [Yolanda Sobral](https://github.com/yolisobral)

# Kata: Cálculo de letra de NIF con Programación Orientada a Objetos

## Introducción

Este proyecto es un kata diseñado para aprender **Programación Orientada a Objetos (POO)** y principios **SOLID**, implementando un programa que calcula la letra del NIF dado un número de DNI. 

Al desarrollar este programa, deberás tomar múltiples decisiones arquitectónicas basadas en los principios SOLID, utilizando la documentación sobre Programación Defensiva para el manejo de errores y programación por contrato.

## Marcos teóricos - Principios SOLID

El desarrollo debe basarse en los siguientes principios:

- **SRP (Single Responsibility Principle)**: Cada clase o componente debe tener una única razón para cambiar.
- **OCP (Open/Closed Principle)**: Las entidades de software (clases, módulos, funciones) deben estar "abiertas" a la extensión pero "cerradas" a la modificación.
- **LSP (Liskov Substitution Principle)**: Los objetos de un programa deben ser reemplazables por instancias de sus tipos base sin alterar el funcionamiento correcto del programa, mediante herencia y polimorfismo.

Para profundizar en estos principios, consulta [_Agile Principles Patterns and Practices in C, by Micah Martin, Robert C. Martin_](https://www.oreilly.com/library/view/agile-principles-patterns/0131857258/)

## El Problema

### Especificación del Algoritmo

Crear un programa que, dado un número de DNI, determine la letra correspondiente del NIF mediante este proceso:

1. Dividir el número de DNI entre `23` y obtener el resto.
2. Usar ese resto como índice para buscar la letra en la tabla de asignación:

![Tabla de asignación](./doc/tabla_asignacion.png)

**Restricciones de letras**: La tabla excluye las letras `I`, `Ñ`, `O`, `U` para evitar confusiones con caracteres similares (`1`, `l`, `0`).

### Diseño arquitectónico

El programa debe implementarse en **tres capas**, tal como se muestra en el diagrama:

![Arquitectura en 3 capas](./doc/n-tier.png)

Debes diseñar un **ADT (Abstract Data Type)** que encapsule la estructura de datos más apropiada: un vector para almacenar las letras de la tabla, un diccionario, u otra estructura que consideres oportuna.

La separación entre la **capa de lógica** y la **capa de acceso a datos** es fundamental para que los cambios en la estructura de datos utilizada (vector, diccionario u otra) no requieran modificaciones en el código de la lógica de negocio.

## Diseño de Clases Propuesto

Se sugiere la siguiente arquitectura orientada a objetos:

| Clase | Propósito |
|-------|-----------|
| `DNI` | Objeto valor que valida y almacena el número del DNI con control de rango y formato válido |
| `NIFCalculator` | Encapsula la lógica para calcular la letra; método público: `calculate(dni: DNI) -> str` sin estados persistentes |
| `LetterTable` (ADT) | Abstracción de la tabla de letras que proporciona `get_letter(index)` sin exponer la estructura interna; puede ser array o diccionario |
| `Repository` | Gestión opcional de persistencia y carga/salida de datos |

### Responsabilidades clave:

- `DNI`: validación de rango válido y formato
- `NIFCalculator`: cálculo de la letra mediante el algoritmo especificado
- `LetterTable`: encapsulación de la colección de letras y acceso por índice

## Objetivos de Aprendizaje

- Practicar diseño orientado a objetos: modelado de clases, responsabilidades y colaboración entre objetos
- Aplicar principios SOLID, enfatizando SRP y OCP
- Separar la lógica de negocio de la capa de acceso a datos mediante un ADT
- Escribir y ejecutar tests automatizados con `pytest`
- Practicar conceptos de herencia, polimorfismo y encapsulación

## Estructura del Repositorio

```
.
├── README.md                     # Este documento
├── src/                          # Código fuente del proyecto
│   ├── __init__.py
│   └── tablaAsignacion.py        # Implementaciones de DNI, NIFCalculator y LetterTable
├── test/                         # Suite de pruebas automatizadas con pytest
│   ├── __init__.py
│   ├── test_dni_cif.py           # Tests del cálculo de NIF
│   ├── test_tabla_asignacion.py  # Tests de la tabla de letras
│   ├── dni_correctos.py          # Datos de prueba: DNI válidos
│   ├── dni_incorrectos.py        # Datos de prueba: DNI inválidos
│   └── dni_formato_incorrecto.py # Datos de prueba: formato incorrecto
└── doc/                          # Imágenes y diagramas
    ├── tabla_asignacion.png
    └── n-tier.png
```

## Instrucciones de Uso

### Preparar el entorno

Activar el entorno virtual de Python:

```bash
source venv/bin/activate
```

### Instalar dependencias

Instalar las herramientas necesarias:

```bash
pip install -r requirements.txt
pip install pytest
```

### Ejecutar los tests

Lanzar la suite de pruebas para validar la implementación:

```bash
pytest
```

