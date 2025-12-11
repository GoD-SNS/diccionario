import os
from pathlib import Path
from datetime import datetime

RED_BG = '\033[41m\033[37m'
GREEN_BG = '\033[42m\033[30m'
BLUE_TX = '\033[34m'
RESET = '\033[0m'

def extract_title(file_path):
    """
    Extrae el título de un archivo markdown de la primera línea que empieza con #.
    Args:
        file_path: Ruta al archivo markdown   
    Returns:
        El título sin el símbolo # o el nombre del archivo si no se encuentra título
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('#'):
                    # Remover el # y espacios
                    return line.lstrip('#').strip()
        # Si no se encuentra título, usar el nombre del archivo
        return file_path.stem.replace('-', ' ').title()
    except Exception as e:
        print(f"{RED_BG}ERROR: Leyendo {file_path}: {e}{RESET}")
        return file_path.stem.replace('-', ' ').title()

def get_all_term_files(terminos_dir):
    """
    Obtiene todos los archivos markdown de términos, organizados por letra.
    Args:
        terminos_dir: Directorio raíz de términos
    Returns:
        Diccionario con estructura {letra: [(titulo, ruta_relativa)]}
    """
    terminos_dict = {}
    
    # Recorrer todas las carpetas de letras
    for letter_dir in sorted(terminos_dir.iterdir()):
        if not letter_dir.is_dir():
            continue
            
        letter = letter_dir.name
        md_files = [f for f in letter_dir.glob('*.md') if f.name != 'README.md'] # Saltar README.md
        
        if not md_files:
            continue
        
        # Extraer títulos y crear lista de tuplas (titulo, ruta_relativa)
        terms = []
        for md_file in sorted(md_files):
            title = extract_title(md_file)
            # Ruta relativa desde el directorio terminos (donde está el README.md)
            rel_path = md_file.relative_to(terminos_dir)
            terms.append((title, str(rel_path)))
        
        if terms:
            terminos_dict[letter] = sorted(terms, key=lambda x: x[0].lower())
    
    return terminos_dict

def generate_index(terminos_dict, output_file):
    """
    Genera el archivo de índice con todos los términos.
    Args:
        terminos_dict: Diccionario con términos organizados por letra
        output_file: Ruta del archivo de índice a generar
    """
    total_terms = sum(len(terms) for terms in terminos_dict.values())
    current_date = datetime.now().strftime("%d de %B de %Y")
    
    meses = {
        'January': 'enero', 'February': 'febrero', 'March': 'marzo',
        'April': 'abril', 'May': 'mayo', 'June': 'junio',
        'July': 'julio', 'August': 'agosto', 'September': 'septiembre',
        'October': 'octubre', 'November': 'noviembre', 'December': 'diciembre'
    }

    for eng, esp in meses.items():
        current_date = current_date.replace(eng, esp)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        # Encabezado
        f.write("# Índice\n\n")
        f.write("Este documento contiene un índice alfabético de todos los términos del diccionario de Gobernanza de Datos (GoD) con enlaces a sus definiciones.\n\n")
        f.write(f"> **Total de términos:** {total_terms}\n\n")
        f.write("<br>\n")
        
        # Contenido por letra
        for letter in sorted(terminos_dict.keys()):
            f.write(f"\n## {letter}\n\n")

            for title, rel_path in terminos_dict[letter]:
                # Usar forward slashes en todos los sistemas
                rel_path = rel_path.replace('\\', '/')
                f.write(f"- [{title}]({rel_path})\n")
        
        # Pie de página
        f.write("\n<br>\n<br>\n<br>\n\n")
        f.write("> **Nota:** Los enlaces utilizan rutas relativas desde la raíz del proyecto. Este índice se actualiza automáticamente mediante un script, si desea más información consulte [`scripts/README.md`](/scripts/README.md).\n")
        f.write("\n")
        f.write(f"> **Última actualización:** {current_date}\n")

def main():
    """Función principal del script."""
    # Obtener los directorios
    script_dir = Path(__file__).parent.parent
    terminos_dir = script_dir / 'terminos'
    output_file = terminos_dir / 'README.md'
    
    print("INFO: Escaneando términos...")
    
    if not terminos_dir.exists():
        print(f"{RED_BG}ERROR: No se encuentra el directorio \"{terminos_dir}\".{RESET}")
        return 1
    
    # Obtener todos los términos
    terminos_dict = get_all_term_files(terminos_dir)
    
    if not terminos_dict:
        print(f"{RED_BG}ERROR: No se encontraron archivos de términos.{RESET}")
        return 1
    
    total_terms = sum(len(terms) for terms in terminos_dict.values())
    print(f"{BLUE_TX}ÉXITO: Encontrados {total_terms} términos en {len(terminos_dict)} letras.{RESET}")
    
    # Generar el índice
    print(f"INFO: Generando {output_file}...")
    generate_index(terminos_dict, output_file)
    print(f"{GREEN_BG}ÉXITO: Índice actualizado exitosamente con {total_terms} términos en total para las letras {', '.join(sorted(terminos_dict.keys()))}.{RESET}")
    return 0

if __name__ == '__main__':
    exit(main())
