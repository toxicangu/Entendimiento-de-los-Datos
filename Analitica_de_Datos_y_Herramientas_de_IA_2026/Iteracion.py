import pandas as pd

df = pd.read_csv('Datos_Facturacion.csv')
#print(df)

#print(df.head(5))  

##Inciso 1
def inciso_1(df):
    filtered_df = df[(df['CVE_CLPV'] >= 1000) & (df['CVE_CLPV'] <= 2000)]
    filtered_df.to_csv('Inciso1.csv') 

inciso_1(df)

#Inciso 2
def inciso_2(df):
    filtered_df = df[(df['CVE_VEND'] != 5 ) & (df['CVE_VEND'] != 4)]
    filtered_df.to_csv('Inciso2.csv')

inciso_2(df)


#Inciso 3
def inciso_3(df):
    fecha_ent = pd.to_datetime(df['FECHA_ENT'], format='mixed', errors='coerce')
    filtered_df = df[fecha_ent.dt.date == pd.Timestamp('2022-02-28').date()]
    filtered_df.to_csv('Inciso3.csv')

inciso_3(df)

#Inciso 4
def inciso_4(df):
    filtered_df = df[(df['CAN_TOT'] < 5951.7) & (df['STATUS'] == 'E')]
    filtered_df.to_csv('Inciso4.csv')

inciso_4(df)

#Inciso 5
def inciso_5(df):
    filtered_df = df[['CVE_DOC', 'FECHA_ENT', 'FECHA_VEN', 'CAN_TOT']]
    filtered_df.to_csv('Inciso5.csv')

inciso_5(df)

#Inciso 6 Filas de 7001 a 7099
def inciso_6(df):
    filtered_df = df[(df.index >= 7001) & (df.index <= 7099)]
    filtered_df.to_csv('Inciso6.csv')

inciso_6(df)