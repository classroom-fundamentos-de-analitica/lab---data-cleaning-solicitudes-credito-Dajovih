"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
from datetime import datetime
def clean_data():
    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df['comuna_ciudadano']=df['comuna_ciudadano'].astype(float)
    df['fecha_de_beneficio']=df['fecha_de_beneficio'].apply(lambda x: datetime.strptime(x, "%Y/%m/%d") if (len(re.findall("^\d+/", x)[0]) - 1) == 4 else datetime.strptime(x, "%d/%m/%Y"))
    df.dropna(axis = 0, inplace = True)
    df.drop_duplicates(inplace = True)
    return df
