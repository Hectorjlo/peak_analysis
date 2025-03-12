### Casos de Prueba para el Módulo 1: Extractor y Creador de Secuencias FASTA


1.  **Caso: Archivo del genoma no se encuentra.**
    
    -   **Entradas:**
        -   Ruta incorrecta o inexistente para el archivo FASTA del genoma.
        -   Archivo de picos válido.
        -   Directorio de salida.
    -   **Esperado:** `"Error: Genome file not found"`
    
    ```python
    mk_fasta_from_peaks.py -i peak_file.txt -g Ecoli.fna -o fasta_peaks/ 
    ```
    ```
    Error: "Ecoli.fna" genome file not found
    ```
2.  **Caso: Archivo de picos vacío.**
    
    -   **Entradas:**
        -   Archivo de picos vacío.
        -   Archivo FASTA del genoma.
        -   Directorio de salida.
    -   **Esperado:** `"Error: the peak file is empty."`

 ```python
    mk_fasta_from_peaks.py -i peak_file.txt -g Ecoli.fna -o fasta_peaks/ 
```
  
```
Error: the peak file is empty
```

3.  **Caso: Posiciones `Peak_start` y `Peak_end` fuera del rango del genoma.**
    
    -   **Entradas:**
        -   Archivo de picos con algunas posiciones `Peak_start` y `Peak_end` fuera del tamaño del genoma.
        -   Archivo FASTA del genoma válido.
        -   Directorio de salida.
    -   **Esperado:**
        -   El sistema debe imprimir un mensaje de advertencia: `"Warning: Some peaks are bigger than the genome". Check the log.out file`
        
        -   Generar un archivo de log indicando los picos fuera de rango. El archivo debe contener las líneas del archivo de picos que tienen problemas.

```python
    mk_fasta_from_peaks.py -i peak_file.txt -g Ecoli.fna -o fasta_peaks/ 
```

```bash
ls
```

```bash
log.out
fasta_peaks/
```
<!--Agregaré casoso donde el archivo de picos tiene un formato incorrecto y otro que se verifique que la salida tenga los datos esperados-->

4.  **Caso: Formato incorrecto del archivo de picos.**
    
    -   **Entradas:**
        -   Archivo de picos con columnas mal formateadas o faltantes.
        -   Archivo FASTA del genoma válido.
        -   Directorio de salida.
    -   **Esperado:** `"Error: The peak file format is incorrect. Check column structure."`

```python
    mk_fasta_from_peaks.py -i malformed_peak_file.txt -g Ecoli.fna -o fasta_peaks/ 
```
  
```
Error: The peak file format is incorrect. Check column structure.
```

5.  **Caso: Verificación de la correcta generación de archivos FASTA.**
    
    -   **Entradas:**
        -   Archivo de picos válido con coordenadas correctas.
        -   Archivo FASTA del genoma válido.
        -   Directorio de salida.
    -   **Esperado:**
        -   Se deben generar archivos FASTA por cada `TF_name` en el directorio de salida.
        -   El contenido de los archivos debe corresponder con las secuencias extraídas.

```python
    mk_fasta_from_peaks.py -i peak_file.txt -g Ecoli.fna -o fasta_peaks/ 
```

```bash
ls fasta_peaks/
```

```bash
TF1.fa  TF2.fa  TF3.fa
```

```bash
cat fasta_peaks/TF1.fa
```

```bash
>peak_1
ATCGGCTA...
```