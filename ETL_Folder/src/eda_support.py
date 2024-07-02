#%%
import pandas as pd
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
#%%
def dataframe_exploration(df,df_name):
    print("*" * 50)
    print(f"--- DATAFRAME EXPLORATION: {df_name} ---")
    print("*" * 50)
    
    # Estructura del dataframe y tipos de datos
    print(f"\nEl DataFrame tiene {df.shape[0]} filas y {df.shape[1]} columnas.\n")
    print("_" * 50)
    
    print("\nMuestra de filas aleatorias:\n")
    print(df.sample(5))
    print("_" * 50)
    
    print(f"\nTipos de datos por columna:\n")
    print(df.dtypes)
    print("_" * 50)
    
    print(f"\nInformación del DataFrame:\n")
    df.info()
    print("_" * 50)
    
    # Valores duplicados
    duplicated_values = df.duplicated().sum()
    duplicated_percentage = round(duplicated_values / df.shape[0] * 100, 2)
    print(f"\nNúmero de duplicados en el conjunto de datos: {duplicated_values}, un {duplicated_percentage}%.\n")
    print("_" * 50)
    
    # Valores nulos
    print("\nValores nulos por columna:\n")
    null_values = df.isnull().sum()
    null_percentage = (null_values / df.shape[0]) * 100
    df_nulos = pd.DataFrame({'nulos': null_values, 'porcentaje_nulos': null_percentage})
    print(df_nulos[df_nulos['porcentaje_nulos'] > 0])
    print("_" * 50)
    
    # Estadísticas básicas para columnas numéricas
    col_num = df.select_dtypes(include=["number"])
    if not col_num.empty:
        print("\nEstadísticas básicas de columnas numéricas:\n")
        print(col_num.describe().T)
        print("_" * 50)
    else:
        print("\nNo hay columnas numéricas en el DataFrame.\n")
        print("_" * 50)
    
    # Estadísticas básicas para columnas categóricas
    col_cat = df.select_dtypes(include=["object", "category"])
    if not col_cat.empty:
        print("\nEstadísticas básicas de columnas categóricas:\n")
        print(col_cat.describe().T)
    else:
        print("\nNo hay columnas categóricas en el DataFrame.\n")
    
    print("\n\n")
#%%
def csv_to_dataframe(file):
    return pd.read_csv(file)
#%%
def verify_common_columns(df1, df2):
    common_columns = df1.columns.intersection(df2.columns)
    if common_columns.empty:
        print("No hay columnas con el mismo nombre en ambos DataFrames.")
        return
    else:
        print(f"Ambos DataFrames tienen las siguientes columnas en comun: {common_columns.tolist()}")
    
    for col in common_columns:
        values_df1 = set(df1[col])
        values_df2 = set(df2[col])
        
        if values_df1 == values_df2:
            print(f"Los valores de la columna '{col}' son idénticos en ambos DataFrames.")
        elif values_df1.issubset(values_df2) and values_df2.issubset(values_df1):
            print(f"Los valores de la columna '{col}' son simétricos entre ambos DataFrames.")
        else:
            print(f"Los valores de la columna '{col}' no son simétricos entre ambos DataFrames.")
            
        print(f"La columna {col} del primer DataFrame tiene {df1[col].duplicated().sum()} valores duplicados.")
        print(f"La columna {col} del segundo DataFrame tiene {df2[col].duplicated().sum()} valores duplicados.")
#%%
def merge_dataframes(df_left, df_right, col_left, col_right, how):
    df = df_left.merge(df_right, how=how, left_on=col_left, right_on=col_right)
    return df
#%%
def clean_data(df):
    if df.duplicated().any():
        print(f"Hay {df.duplicated().sum()} registros duplicados encontrados y eliminados.")
        df = df.drop_duplicates(keep='first')
    else:
        print("No se encontraron duplicados.")
    
    null_percentage = df.isnull().mean()
    cols_to_remove = null_percentage[null_percentage > 0.3].index

    if not cols_to_remove.empty:
        df = df.drop(columns=cols_to_remove)
        print(f"Columnas eliminadas con más del 30% de valores nulos: {list(cols_to_remove)}")
    else:
        print("No se eliminaron columnas por valores nulos.")
        
    cols_one_value = [col for col in df.columns if df[col].nunique() == 1]
    if cols_one_value:
        df = df.drop(columns=cols_one_value)
        print(f"Columnas eliminadas con solo un valor unico: {cols_one_value}")
    else:
        print("No se encontraron columnas con solo un valor unico.")
        
    col_num = df.select_dtypes(include=['number'])
    cols_negative = [col for col in col_num.columns if (col_num[col] < 0).any()]
    if cols_negative:
        print(f"Columnas con valores negativos convertidos a absolutos: {cols_negative}")
        df[cols_negative] = df[cols_negative].abs()
    else:
        print("No se encontraron columnas con valores negativos.")
    
    cols_float = df.select_dtypes(include=[float]).columns
    if cols_float.any():
        print(f"Columnas tipo float redondeadas a dos decimales o convertidas a enteros: {list(cols_float)}")
        for col in cols_float:
            df[col] = df[col].apply(lambda x: round(x, 2) if x % 1 != 0 else int(x))
    else:
        print("No se encontraron columnas tipo float.")
        
    df.columns = df.columns.str.replace(' ', '_').str.lower()
    print(f"Nombres de columnas cambiados a minuscula y con guiones bajos en vez de espacios.")
       
    return df
#%%
def iterative_imputation(df):
    imputer_iterative = IterativeImputer(max_iter=20, random_state=42)
    imputer_iterative_imputado = imputer_iterative.fit_transform(df[["salary"]])
    df["salary_iterative"] = imputer_iterative_imputado
    print(f"Despues de la imputación 'Iterative' tenemos: \n{df['salary_iterative'].isnull().sum()} nulos en la columna 'Salary'.")
    df.drop(["salary"], axis = 1, inplace = True)
    df.rename(columns={"salary_iterative": "salary"}, inplace=True)
    return df