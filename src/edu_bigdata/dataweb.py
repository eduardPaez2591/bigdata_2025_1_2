import yfinance as yf
import pandas as pd
import os

def obtener_datos_usd_cop():
    # Descargar datos desde 2020 hasta hoy
    df = yf.download("COP=X", start="2020-01-01", progress=False)

    # Renombrar columnas
    df = df.reset_index().rename(columns={
        'Date': 'fecha',
        'Open': 'abrir',
        'High': 'alto',
        'Low': 'bajo',
        'Close': 'cerrar',
        'Adj Close': 'cierre_ajustado',
        'Volume': 'volumen'
    })

    return df

def guardar_csv(df):
    # Ruta
    ruta_csv = os.path.join(os.getcwd(), 'src', 'edu_bigdata', 'static', 'csv')
    
    # Crear la carpeta si no existe
    os.makedirs(ruta_csv, exist_ok=True)

    # Nombre del archivo CSV
    archivo = os.path.join(ruta_csv, 'USD_COP.csv')
    
    # Guardar el archivo
    df.to_csv(archivo, index=False)
    print(f"Archivo guardado exitosamente en: {archivo}")

