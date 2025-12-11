# Scripts de automatización

[guide]: ../README.md#guía-de-trabajo

Este directorio contiene los scripts para automatizar tareas de mantenimiento del diccionario. El script `actualizar.py` permite actualizar automáticamente el índice de términos del diccionario.

## Contenido
1. [Operación](#operación)
    - [Advertencias](#advertencias)
2. [Requisitos](#requisitos)
3. [Ejecución](#ejecución)
    1. [Paso 1. Instalar Python (si no lo tienes)](#paso-1-instalar-python-si-no-lo-tienes)
    2. [Paso 2. Verificar la instalación](#paso-2-verificar-la-instalación)
    3. [Paso 3. Ejecutar el script](#paso-3-ejecutar-el-script)
    4. [Paso 4. Verificar la ejecución exitosa](#paso-4-verificar-la-ejecución-exitosa)
4. [Solución de problemas](#solución-de-problemas)

<br>
<br>

## Operación
El script realiza las siguientes operaciones:
1. Escaneo de archivos: Recorre todas las subcarpetas en `terminos/` (A, B, C, etc.).
2. Homogeneización de títulos: Lee la primera línea con `#` de cada archivo `.md` para obtener el título del término.
3. Organización alfabética: Agrupa los términos por letra inicial.
4. Generación del índice: Crea el índice en archivo `terminos/README.md`.

### Advertencias
- El archivo `terminos/README.md` se sobrescribe completamente cada vez.
- Asegúrate de que todos los archivos `.md` tengan una línea que comience con `#` para el título.

<br>
<br>

> Para un correcto uso de los scripts sigue todos los pasos de la [guía de trabajo][guide].

<br>
<br>

## Requisitos
- Python 3.6 o superior

<br>
<br>

## Ejecución

La siguiente información complementa la [guía de trabajo][guide], y detalla la ejecución del script.

Ejecuta el script cuando:
1. Agregues un nuevo término al diccionario.
2. Elimines un término existente.
3. Cambies el título principal (línea con `#`) de un término.
4. Reorganizes la estructura de carpetas.
5. NO es necesario ejecutarlo si solo modificas el contenido (no el título) de un término.

<br>

### Paso 1. Instalar Python (si no lo tienes)
- **En macOS:** Descargar desde [python.org/downloads/macos](https://www.python.org/downloads/macos/).
- **En Windows:** Descargar el instalador desde [python.org/downloads/windows](https://www.python.org/downloads/windows/). Y durante la instalación, marca "Add Python to PATH".
- **En Linux:** Generalmente Python 3 ya viene preinstalado; pero si no, instalar con:
    ```bash
    # Para Debian/Ubuntu
    sudo apt update
    sudo apt install python3 python3-pip
    
    # Para Fedora/RHEL
    sudo dnf install python3 python3-pip
    ```

### Paso 2. Verificar la instalación
Verifica tu instalación de Python ejecutando:
```bash
# En macOS y Linux
python3 --version

# En Windows (puede ser python, python3 o py)
python3 --version
python --version
py --version
```
Deberías ver una salida como: `Python 3.12.x` o similar (versión 3.6 o superior).

### Paso 3. Ejecutar el script
1. Desde el directorio raíz del proyecto:
    ```bash
    cd scripts
    ```
2. Después de ubicarte en el directorio de scripts ejecuta:
    ```bash
    # En macOS y Linux
    python3 actualizar.py

    # En Windows (puede ser python, python3 o py)
    python3 actualizar.py
    python actualizar.py
    py actualizar.py
    ```

### Paso 4. Verificar la ejecución exitosa
Si después de ejecutar el script recibes la siguiente salida, el proceso se completó exitosamente.
```
INFO: Escaneando términos...
ÉXITO: Encontrados 289 términos en 20 letras.
INFO: Generando .../terminos/README.md...
ÉXITO: Índice actualizado exitosamente con # términos en total para las letras A, B, ..., Z.
```
En caso contrario, ve a la sección de [Solución de problemas](#solución-de-problemas) para ver las soluciones a errores comunes.

<br>

## Solución de problemas
1. **ERROR: No se encuentra el directorio terminos.**
    Verifica que estés ejecutando el script desde la ruta correcta. Revisa el [paso 3](#paso-3-ejecutar-el-script) incluído en esta guía sobre la ejecución del script.
2. **ERROR: No se encontraron archivos de términos.**
    Verifica que existan archivos `.md` en las subcarpetas de `terminos/` y asegúrate de que las subcarpetas no estén vacías.
3. **El título no aparece correctamente.**
    Verifica que el archivo incie con una línea que comience con `#`.

<br>
<br>

## © Copyright
- **Organización.** Superintendencia Nacional de Salud (SNS).
- **Desarrollado por** Julian Vanegas López.

<br>

    CONTRATO 116 DE 2025 SUPERINTENDENCIA NACIONAL DE SALUD – UNIVERSIDAD DE ANTIOQUIA.
    Para desarrollar e implementar el programa de Gobernanza de Datos en las etapas restantes de diseño y arquitectura, implementación, y operación y control, y el programa de inteligencia de negocios y analítica de la Superintendencia Nacional de Salud (SNS).
