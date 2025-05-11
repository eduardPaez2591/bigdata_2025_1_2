import sqlite3
import pandas as pd
import os

def cargar_csv_a_sqlite():
    try:
        ruta_csv = os.path.join('src', 'edu_bigdata', 'static', 'csv', 'USD_COP.csv')
        ruta_db = os.path.join('src', 'edu_bigdata', 'static', 'db', 'historico_dolar.db') 

        # Verificar existencia del archivo CSV
        if not os.path.exists(ruta_csv):
            print(f" Archivo CSV no encontrado en: {ruta_csv}")
            return

        # Leer el archivo CSV
        df = pd.read_csv(ruta_csv)

        # Verificar si columnas necesarias existen
        columnas_esperadas = ['fecha', 'cerrar', 'alto', 'bajo', 'abrir', 'volumen']
        if not all(col in df.columns for col in columnas_esperadas):
            print(" El archivo CSV no contiene las columnas necesarias.")
            print("Columnas encontradas:", df.columns.tolist())
            return

        # Convertir columnas numéricas
        columnas_a_convertir = ['abrir', 'alto', 'bajo', 'cerrar']
        for col in columnas_a_convertir:
            df[col] = pd.to_numeric(df[col], errors='coerce')

        df['volumen'] = pd.to_numeric(df['volumen'], errors='coerce')

        # Crear carpeta si no existe
        os.makedirs(os.path.dirname(ruta_db), exist_ok=True)

        # Conectar y guardar en SQLite
        conn = sqlite3.connect(ruta_db)
        df.to_sql('historico_dolar', conn, if_exists='replace', index=False)
        conn.close()

        print(f" Base de datos creada exitosamente en: {ruta_db}")
    
    except Exception as e:
        print(" Error durante la carga del CSV a SQLite:")
        print(e)

#mostrar que la bd se creo 
def mostrar_info_db():
    ruta_db = os.path.join('src', 'edu_bigdata', 'static', 'db', 'historico_dolar.db')

    if not os.path.exists(ruta_db):
        print(" El archivo de base de datos no existe.")
        return

    try:
        conn = sqlite3.connect(ruta_db)
        cursor = conn.cursor()

        # Mostrar tablas existentes
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tablas = cursor.fetchall()
        print(" Tablas en la base de datos:")
        for t in tablas:
            print("   -", t[0])

        # Mostrar los primeros 5 registros de la tabla principal
        if ('historico_dolar',) in tablas:
            print("\n Primeros registros de 'historico_dolar':")
            cursor.execute("SELECT * FROM historico_dolar LIMIT 5;")
            for fila in cursor.fetchall():
                print(fila)
        else:
            print(" No se encontró la tabla 'historico_dolar'.")

        conn.close()

    except Exception as e:
        print(" Error al acceder a la base de datos:", e)



