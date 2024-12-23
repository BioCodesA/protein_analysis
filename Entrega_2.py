
"""Please read the READMY.md and Licence documents before using this code"""

'''The files I tested this code with are named bacterias_protein.tsv and uniprotkb_2024_12_23.tsv, you can also use them to test this code'''

'''If you want to analyze your own data make sure they are in .tsv format and have columns named Organism, Sequence, Gene Names'''


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Función para calcular la longitud de una proteína

def calcular_longitud_proteina(secuencia):
    return len(secuencia)


# Función para calcular la frecuencia de aminoácidos

def calcular_frecuencia_aminoacidos(secuencias):
    from collections import Counter
    todas_secuencias = ''.join(secuencias)
    return Counter(todas_secuencias)


# Función para leer archivos TSV

def leer_archivo_tsv(ruta):
    try:
        df = pd.read_csv(ruta, sep='\t')
        print(f"Archivo cargado correctamente: {ruta}")
        return df
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None


# Función principal para análisis

def analizar_datos(df):
    if df is None:
        print("No se proporcionaron datos para el análisis.")
        return

    
    columnas_relevantes = ['Organism', 'Sequence', 'Gene Names']          # Filtrar columnas relevantes
    df = df[columnas_relevantes].dropna()

    
    df['Protein Length'] = df['Sequence'].apply(calcular_longitud_proteina)     # Calcular longitud de proteínas

    generar_graficos(df)

# Función para generar gráficos

def generar_graficos(df):

                                                            ''' GRAFICO 1: Distribución de la longitud de las proteínas'''

    sns.histplot(df['Protein Length'], bins=30, kde=True, color="blue")
    plt.title("Distribución de la Longitud de las Proteínas")
    plt.xlabel("Longitud (aminoácidos)")
    plt.ylabel("Frecuencia")
    plt.show()

                                                             '''GRAFICO 2: Frecuencia de aminoácidos individuales'''


    frecuencias = calcular_frecuencia_aminoacidos(df['Sequence'])
    amino_df = pd.DataFrame(frecuencias.items(), columns=['Amino Acid', 'Frequency'])
    amino_df = amino_df.sort_values(by='Frequency', ascending=False)

    sns.barplot(data=amino_df, x='Amino Acid', y='Frequency', color='skyblue')
    plt.title("Frecuencia de Aminoácidos")
    plt.xlabel("Aminoácido")
    plt.ylabel("Frecuencia")
    plt.show()

                                                          '''GRAFICO 3: Comparación de longitud promedio de proteínas entre especies'''

    
    promedio_longitud = df.groupby('Organism')['Protein Length'].mean().reset_index()

    sns.barplot(data=promedio_longitud, x='Organism', y='Protein Length', palette='Set2')
    plt.title("Longitud Promedio de las Proteínas entre Especies")
    plt.xlabel("Especie")
    plt.ylabel("Longitud Promedio (aminoácidos)")
    plt.xticks(rotation=90)
    plt.show()


                                                             '''GRAFICO 4: Relación entre genes y longitud promedio de proteínas'''

    promedio_por_gen = df.groupby('Gene Names')['Protein Length'].mean().reset_index()

    sns.barplot(data=promedio_por_gen, x='Gene Names', y='Protein Length', color='teal')
    plt.title("Relación entre Genes y Longitud Promedio de Proteínas")
    plt.xlabel("ID del Gen")
    plt.ylabel("Longitud Promedio (aminoácidos)")
    plt.xticks(rotation=90)
    plt.show()



                                                          '''GRAFICO 5: Relación entre especies y composición promedio de aminoácidos'''

    composicion_aminoacidos = df['Sequence'].apply(calcular_frecuencia_aminoacidos)
    composicion_df = pd.DataFrame(composicion_aminoacidos.tolist()).fillna(0)
    composicion_df['Organism'] = df['Organism'].values
    promedio_composicion = composicion_df.groupby('Organism').mean()


    sns.heatmap(promedio_composicion, cmap="YlGnBu", annot=True, fmt=".1f")
    plt.title("Composición Promedio de Aminoácidos por Especie")
    plt.xlabel("Aminoácidos")
    plt.ylabel("Especies")
    plt.show()




                                           
if __name__ == "__main__":
    ruta_tsv = input("Ingrese la ruta del archivo TSV: ")       # Solicitar al usuario la ruta del archivo TSV: en la consola o terminal pones la dirección en la que se encuentra el archivo para ser procesado 
    datos = leer_archivo_tsv(ruta_tsv)                                           
    analizar_datos(datos)
