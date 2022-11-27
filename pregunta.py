"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
from datetime import datetime
import re
def clean_data():
    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df.dropna(axis = 0, inplace = True)
    df.drop_duplicates(inplace = True)
    df['monto_del_credito']=df['monto_del_credito'].str.replace("\$[\s*]", "")
    df['monto_del_credito']=df['monto_del_credito'].str.replace(",", "")
    df['monto_del_credito']=df['monto_del_credito'].str.replace("\.00", "")
    df['monto_del_credito']=df['monto_del_credito'].astype(int)
    df['comuna_ciudadano']=df['comuna_ciudadano'].astype(float)
    df['fecha_de_beneficio']=df['fecha_de_beneficio'].apply(lambda x: datetime.strptime(x, "%Y/%m/%d") if (len(re.findall("^\d+/", x)[0]) - 1) == 4 else datetime.strptime(x, "%d/%m/%Y"))
    for i in ['idea_negocio','sexo','barrio','tipo_de_emprendimiento','línea_credito']:
        df[i] = df[i].str.lower()
        df[i] = df[i].apply(lambda x: x.replace('_', ' '))
        df[i] = df[i].apply(lambda x: x.replace('-', ' '))
    return df
