# <img src="https://github.com/GoD-SNS/diccionario/blob/main/diccionario_god_sns.jpg" alt="Diccionario de Gobernanza de Datos (GoD) de la Superintendencia Nacional de Salud (SNS)">

<br>

> Para ver el índice del diccionario y los términos haz [clic aquí](/terminos/README.md) o ve a [`terminos/README.md`](/terminos/README.md).

<br>

Este diccionario constituye una herramienta fundamental para la comprensión y aplicación de los conceptos asociados a la Gobernanza de Datos (GoD) y a la Inteligencia de Negocios y Analítica (BI&A) en la Superintendencia Nacional de Salud (SNS). Su propósito es ofrecer un lenguaje común, preciso y estandarizado que facilite la comunicación entre las áreas técnicas, administrativas y estratégicas, asegurando la alineación entre las políticas y los objetivos institucionales.

Este proyecto es un diccionario interactivo y estructurado que contiene términos relacionados con la Gobernanza de Datos e Inteligencia de Negocios. Cada término está documentado en su propio archivo *Markdown* (es un archivo de texto enriquecido y fácil lectura) con su definición detallada y referencias bibliográficas.

## Contenido
1. [Estructura del proyecto](#estructura-del-proyecto)
2. [¿Cómo funciona?](#¿cómo-funciona)
    1. [Organización de términos](#organización-de-términos)
    2. [Navegación](#navegación)
3. [Guía de trabajo](#guía-de-trabajo)
    1. [Paso 1. Clonar el repositorio](#paso-1-clonar-el-repositorio)
    2. [Paso 2. Hacer cambios en el diccionario](#paso-2-hacer-cambios-en-el-diccionario)
    3. [Paso 3. Actualizar el índice automáticamente](#paso-3-actualizar-el-índice-automáticamente)
    4. [Paso 4. Revisa los cambios](#paso-4-revisa-los-cambios)
    5. [Paso 5. Preparar los cambios en el repositorio](#paso-5-preparar-los-cambios-en-el-repositorio)
    6. [Paso 6. Hacer commit](#paso-6-hacer-commit)
    7. [Paso 7. Publicar los cambios en el repositorio (hacer push)](#paso-7-publicar-los-cambios-en-el-repositorio-hacer-push)
    8. [Buenas prácticas](#buenas-prácticas)
4. [© Copyright](#-copyright)

<br>
<br>

## Estructura del proyecto
```
diccionario-god/
├── README.md                   # Este archivo
├── scripts/                    # Scripts de automatización
│   ├── README.md               # Documentación de scripts
│   └── actualizar.py           # Script para actualizar el índice
└── terminos/                   # Directorio de términos organizados
    ├── README.md               # Índice alfabético auto-generado
    ├── A/                      # Términos que inician con A
    ├── B/                      # Términos que inician con B
    └── ...                     # Letras restantes hasta la Z
```

<br>
<br>

## ¿Cómo funciona?

### Organización de términos
- Cada término está en su propio archivo `.md` dentro de una carpeta correspondiente a su letra inicial.
- Los nombres de archivo usan guiones en lugar de espacios: `gobernanza-de-datos.md`.
- El índice completo se encuentra en [`terminos/README.md`](/terminos/README.md) y se actualiza automáticamente.

### Navegación
1. **Índice alfabético**: Consulta [`terminos/README.md`](/terminos/README.md) para ver el índice con todos los términos organizados.
2. **Búsqueda directa**: Navega a `terminos/[LETRA]/[nombre-del-termino].md`.

<br>
<br>

## Guía de trabajo

### Paso 1. Clonar el repositorio
Clonar el repositorio de GitHub en tu equipo local:
```bash
git clone https://github.com/GoD-SNS/diccionario.git
```
**Importante:** Esto solo se hace la primera vez.

<br>

### Paso 2. Hacer cambios en el diccionario
#### Agregar un nuevo término
1. Crear el archivo en la carpeta correspondiente: `terminos/[LETRA]/[nombre-del-termino].md`
2. Abrir el archivo y agregar el contenido con el siguiente formato:
    ```markdown
    # Nombre del término
    [Definición detallada del término]

    ## Referencias
    [Referencias bibliográficas si aplican]
    ```

#### Modificar un término existente
1. Abrir el archivo correspondiente: `terminos/[LETRA]/[nombre-del-termino].md`
2. Editar y guardar los cambios en el archivo.

#### Eliminar un término existente
1. Buscar el archivo correspondiente: `terminos/[LETRA]/[nombre-del-termino].md`
2. Eliminar el archivo.

<br>

### Paso 3. Actualizar el índice automáticamente
> Antes de continuar lee la guía para realizar la actualización automática en [`scripts/README.md`](/scripts/README.md).

Si ya has leído la guía de actualización automática, ejecuta el script para actualizar el índice:
```bash
python scripts/actualizar.py

# Si hay porblemas, también puedes usar:
python3 scripts/actualizar.py
```

<br>

### Paso 4. Revisa los cambios
- Para ver qué archivos fueron modificados
    ```bash
    git status
    ```
- Para ver los cambios específicos en los archivos
    ```bash
    git diff
    ```
- Para ver solo los nombres de archivos cambiados
    ```bash
    git diff --name-only
    ```

<br>

### Paso 5. Preparar los cambios en el repositorio
Agregar todos los archivos modificados:
```bash
git add .
```
O para agregar archivos específicos:
```bash
git add terminos/{LETRA}/{TERMINO}.md terminos/README.md
```

<br>

### Paso 6. Hacer commit
1. Seleccionar el prefijo correspondiente según el tipo de cambio:

| Prefijo | Uso | Ejemplo |
|---------|-----|---------|
| `feat:` | Nuevo término | `feat: agregar término GoD` |
| `fix:` | Corrección de definiciones | `fix: corregir definición de GoD` |
| `docs:` | Cambios en documentación | `docs: actualizar README` |
| `chore:` | Mantenimiento | `chore: actualizar script de automatización` |
| `refactor:` | Reestructuración de contenido | `refactor: reorganizar términos de letra D` |
| `style:` | Formato sin cambio de contenido | `style: corregir formato markdown` |

2. Realizar el commit:
    ```bash
    git commit -m "{PREFIJO}: {DESCRIPCIÓN}"
    ```
    Por ejemplo, para agregar un término nuevo:
    ```bash
    git commit -m "feat: agregar término Gobernanza de Datos"
    ```

<br>

### Paso 7. Publicar los cambios en el repositorio (hacer push)
Enviar los cambios a la rama principal
```bash
git push origin main
```
Si es la primera vez o trabajas en otra rama
```bash
git push origin [nombre-de-tu-rama]
```

<br>

### Buenas prácticas
- Asegurate de siempre ejecutar `scripts/actualizar.py` después de agregar, modificar o eliminar términos para actualizar el diccionario.
- Revisa los cambios con `git diff` antes de hacer commit.
- Haz commits pequeños y específicos, un término a la vez es ideal.
- Verifica que el push fue exitoso revisando el repositorio en línea ingresando a [github.com/GoD-SNS/diccionario](https://github.com/GoD-SNS/diccionario.git).

<br>
<br>

## © Copyright
- **Organización.** Superintendencia Nacional de Salud (SNS).
- **Desarrollado por** Julian Vanegas López.

<br>

    CONTRATO 116 DE 2025 SUPERINTENDENCIA NACIONAL DE SALUD – UNIVERSIDAD DE ANTIOQUIA.
    Para desarrollar e implementar el programa de Gobernanza de Datos en las etapas restantes de diseño y arquitectura, implementación, y operación y control, y el programa de inteligencia de negocios y analítica de la Superintendencia Nacional de Salud (SNS).
