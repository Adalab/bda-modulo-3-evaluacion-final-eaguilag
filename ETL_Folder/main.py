#%%
from src import eda_support as eda
#%%
df_loyalty = eda.csv_to_dataframe("files/Customer Loyalty History.csv")
df_flight = eda.csv_to_dataframe("files/Customer Flight Activity.csv")

eda.dataframe_exploration(df_loyalty, "Customer Loyalty History")
eda.dataframe_exploration(df_flight, "Customer Flight Activity")
# %%
eda.verify_common_columns(df_loyalty,df_flight)
#%%
df_merged = eda.merge_dataframes(df_loyalty, df_flight, 'Loyalty Number','Loyalty Number', 'right')
#%%
df_cleaned = eda.clean_data(df_merged)
#%%
df_imputed = eda.iterative_imputation(df_cleaned)
#%%
df_imputed.to_csv("files/customer-data.csv",index=False)
print("Proceso EDA finalizado. Archivo customer-data.csv guardado correctamente.")