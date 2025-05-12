from dataweb import obtener_datos_usd_cop, guardar_csv
from database import cargar_csv_a_sqlite, mostrar_info_db
import pandas as pd



def main():
    datos = obtener_datos_usd_cop()
    guardar_csv(datos)
    cargar_csv_a_sqlite()
    mostrar_info_db()



if __name__ == "__main__":
    main()