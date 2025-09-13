###################### Función para cargar un archivo como un dataframe################################

def cargar_dataset(archivo):  #La entrada es un archivo
    import pandas as pd
    import os
    #Si se desea agregar un input se coloca:
#   archivo=input("Por favor, ingresa el nombre del archivo: ")
    extension = os.path.splitext(archivo)[1].lower()
# Cargar el archivo según su extensión
    if extension == '.csv':
        df= pd.read_csv(archivo)
        return (df)
    elif extension == '.xlsx':
        df= pd.read_excel(archivo)
        return (df)
    elif extension == '.json':
        df= pd.read_json(archivo)
        return (df)
    elif extension == '.html':
        df= pd.read_html(archivo)
        return (df)
    else:
            raise ValueError(f"Formato de archivo no soportado: {extension}")


#Función_Nulos_Promedio_Dataframe
def nulos_ffill_df(df, valor_final=0):
    import pandas as pd
    df = df.fillna(method="ffill")
   # Rellenar cualquier NaN restante con valor_final
    df = df.fillna(valor_final)
    return df 

def nulos_bfill_df(df, valor_final=0):
    import pandas as pd
    # Rellenar NaN con backward fill
    df = df.fillna(method="bfill")
    # Rellenar cualquier NaN restante con valor_final
    df = df.fillna(valor_final)
    return df

def nulos_string_df(df, valor="Sin dato"):
    import pandas as pd
    #Separo columnas cuantitativas del dataframe
    cuantitativas= df.select_dtypes(include=['float64', 'int64','float','int'])
    #Separo columnas cualitativas del dataframe
    cualitativas = df.select_dtypes(include=['object', 'datetime','category'])
    # Sustituir valores nulos en cualitativas por un string concreto
    cualitativas = cualitativas.fillna(valor)
    # Unimos los dataframes
    df = pd.concat([cuantitativas, cualitativas], axis=1)
    return df

def nulos_prom_df(df):
    import pandas as pd
    #Separo columnas cuantitativas del dataframe
    cuantitativas= df.select_dtypes(include=['float64', 'int64','float','int'])
    cuantitativas = cuantitativas.apply(pd.to_numeric, errors='coerce')
    #Separo columnas cualitativas del dataframe
    cualitativas = df.select_dtypes(include=['object', 'datetime','category'])
    #Sustituir valores nulos con promedio o media
    cuantitativas = cuantitativas.fillna(round(cuantitativas.mean(), 1))
    # Unimos el dataframe cuantitativo limpio con el dataframe cualitativo
    df = pd.concat([cuantitativas, cualitativas], axis=1)
    return(df)

def nulos_mediana_df(df):
    import pandas as pd
    # Separo columnas cuantitativas del dataframe
    cuantitativas = df.select_dtypes(include=['float64', 'int64', 'float', 'int'])
    cuantitativas = cuantitativas.apply(pd.to_numeric, errors='coerce')
    # Separo columnas cualitativas del dataframe
    cualitativas = df.select_dtypes(include=['object', 'datetime', 'category'])
    # Sustituir valores nulos con mediana
    cuantitativas = cuantitativas.fillna(cuantitativas.median())
    # Unimos los dataframes
    df = pd.concat([cuantitativas, cualitativas], axis=1)
    return df

def nulos_constante_df(df, valor=0):
    import pandas as pd
    # Separo columnas cuantitativas del dataframe
    cuantitativas = df.select_dtypes(include=['float64', 'int64', 'float', 'int'])
    cuantitativas = cuantitativas.apply(pd.to_numeric, errors='coerce')
    # Separo columnas cualitativas del dataframe
    cualitativas = df.select_dtypes(include=['object', 'datetime', 'category'])
    # Sustituir valores nulos con constante
    cuantitativas = cuantitativas.fillna(valor)
    # Unimos los dataframes
    df = pd.concat([cuantitativas, cualitativas], axis=1)
    return df

def identificar_nulos_df(df):
    import pandas as pd
    # Contar valores nulos por columna
    nulos_columna = df.isna().sum()
    # Crear resumen
    resumen = pd.DataFrame({"nulos_por_columna": nulos_columna})
    # Imprimir total de nulos en el dataframe
    print(f"Total de valores nulos en el DataFrame: {df.isna().sum().sum()}")
    return resumen