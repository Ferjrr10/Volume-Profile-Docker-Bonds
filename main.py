import pandas as pd
import openpyxl as op
import psycopg2
from sqlalchemy import create_engine
from psycopg2 import Error
import wget
from datetime import date
import os

today = date.today()
today_need = today.strftime("%d/%m/%Y")


#importing bond's prices 

t = "20/05/2020"

url_AL30D = "https://www.cohen.com.ar/Financial/GetExcelReporteCotizacionesHistoricas?simbolo=20902&fechaDesde=" + t + "&fechaHasta=" + today_need 
url_AL29D = "https://www.cohen.com.ar/Financial/GetExcelReporteCotizacionesHistoricas?simbolo=20900&fechaDesde=" + t + "&fechaHasta=" + today_need 
url_AL41D = "https://www.cohen.com.ar/Financial/GetExcelReporteCotizacionesHistoricas?simbolo=20907&fechaDesde=" + t + "&fechaHasta=" + today_need 
url_AE38D = "https://www.cohen.com.ar/Financial/GetExcelReporteCotizacionesHistoricas?simbolo=20903&fechaDesde=" + t + "&fechaHasta=" + today_need 
url_AL35D = "https://www.cohen.com.ar/Financial/GetExcelReporteCotizacionesHistoricas?simbolo=20905&fechaDesde=" + t + "&fechaHasta=" + today_need 
url_GD30D = "https://www.cohen.com.ar/Financial/GetExcelReporteCotizacionesHistoricas?simbolo=20916&fechaDesde=" + t + "&fechaHasta=" + today_need 
url_GD29D = "https://www.cohen.com.ar/Financial/GetExcelReporteCotizacionesHistoricas?simbolo=20914&fechaDesde=" + t + "&fechaHasta=" + today_need 
url_GD38D = "https://www.cohen.com.ar/Financial/GetExcelReporteCotizacionesHistoricas?simbolo=20932&fechaDesde=" + t + "&fechaHasta=" + today_need
url_AL30 = "https://www.cohen.com.ar/Financial/GetExcelReporteCotizacionesHistoricas?simbolo=20850&fechaDesde=" + t + "&fechaHasta=" + today_need 
url_AE38 = "https://www.cohen.com.ar/Financial/GetExcelReporteCotizacionesHistoricas?simbolo=20853&fechaDesde=" + t + "&fechaHasta=" + today_need
url_AL29 = "https://www.cohen.com.ar/Financial/GetExcelReporteCotizacionesHistoricas?simbolo=20849&fechaDesde=" + t + "&fechaHasta=" + today_need 
url_AL41 = "https://www.cohen.com.ar/Financial/GetExcelReporteCotizacionesHistoricas?simbolo=20851&fechaDesde=" + t + "&fechaHasta=" + today_need   
wget.download(url_AL30D, './AL30D.xlsx') 
wget.download(url_AL29D, './AL29D.xlsx')
wget.download(url_AL41D, './AL41D.xlsx')
wget.download(url_AE38D, './AE38D.xlsx')
wget.download(url_AL35D, './AL35D.xlsx')
wget.download(url_GD30D, './GD30D.xlsx')
wget.download(url_GD29D, './GD29D.xlsx')
wget.download(url_GD38D, './GD38D.xlsx')
wget.download(url_AL30, './AL30.xlsx')
wget.download(url_AE38, './AE38.xlsx')
wget.download(url_AL29, './AL29.xlsx')
wget.download(url_AL41, './AL41.xlsx')

#Read datas from Excel

Excel_worksheet_AL29D = pd.read_excel('./AL29D.xlsx')
Excel_worksheet_AL30D = pd.read_excel('./AL30D.xlsx')
Excel_worksheet_AL30 = pd.read_excel('./AL30.xlsx')
Excel_worksheet_AL41D = pd.read_excel('./AL41D.xlsx')
Excel_worksheet_AE38D = pd.read_excel('./AE38D.xlsx')
Excel_worksheet_AL41 = pd.read_excel('./AL41.xlsx')
Excel_worksheet_AE38 = pd.read_excel('./AE38.xlsx')
Excel_worksheet_AL29 = pd.read_excel('./AL29.xlsx')
Excel_worksheet_GD30D = pd.read_excel('./GD30D.xlsx')
#Clear the dataset

AL29D_DataFrame = pd.DataFrame(Excel_worksheet_AL29D)
AL30D_DataFrame = pd.DataFrame(Excel_worksheet_AL30D)
AL30_DataFrame = pd.DataFrame(Excel_worksheet_AL30)
AL41D_DataFrame = pd.DataFrame(Excel_worksheet_AL41D)
AE38D_DataFrame = pd.DataFrame(Excel_worksheet_AE38D)
AL29_DataFrame = pd.DataFrame(Excel_worksheet_AL29)
AL41_DataFrame = pd.DataFrame(Excel_worksheet_AL41)
AE38_DataFrame = pd.DataFrame(Excel_worksheet_AE38)
GD30D_DataFrame = pd.DataFrame(Excel_worksheet_GD30D)


#DEF FUNCTION

def connect_psql():
    try:
        host="pg_container"
        username="root"
        password="root"
        database="postgres"
        
        #conexion = psycopg2.connect(host=HOST,user=USERNAME,password=PASSWORD,database=DATABASE)
        conexion = create_engine("postgresql+psycopg2://root:root@pg_container:5432/postgres")
        boolean= 1
        print('CONEXIÓN EXITOSA')
    except:
        print("Error: Configuración no válida")
        boolean= 0
    # Establecer conexión automática
    if boolean==1:
        conexion.autocommit= True
        return conexion
    else:
        print("No existe conexión con postgre")

con = connect_psql()

#tablePsql = "postgres"
tablePsql = "AL29D"
tablePsql1 = "AL30D"
tablePsql12 = "AL30"
tablePsql3 = "AL41D"
tablePsql4 = "AE38D"
tablePsql5 = "AL29"
tablePsql6 = "AL41"
tablePsql7 = "AE38"
tablePsql8 = "GD30D"
tablePsql8 = "AL41"
# Enviar DF
try:
    #AL29D_Precio_Fecha = AL29D_DataFrame.drop(columns= ['Apertura', 'Máximo', 'Mínimo'])
    #AL30D_Precio_Fecha = AL30D_DataFrame.drop(columns= ['Apertura', 'Máximo', 'Mínimo'])
    #AL30_Precio_Fecha = AL30_DataFrame.drop(columns= ['Apertura', 'Máximo', 'Mínimo'])
    #AL41D_Precio_Fecha = AL41D_DataFrame.drop(columns= ['Apertura', 'Máximo', 'Mínimo'])
    #AE38D_Precio_Fecha = AE38D_DataFrame.drop(columns= ['Apertura', 'Máximo', 'Mínimo'])
    #AL29_Precio_Fecha = AL29_DataFrame.drop(columns= ['Apertura', 'Máximo', 'Mínimo'])
    #AL41_Precio_Fecha = AL41_DataFrame.drop(columns= ['Apertura', 'Máximo', 'Mínimo'])
    #AE38_Precio_Fecha = AE38_DataFrame.drop(columns= ['Apertura', 'Máximo', 'Mínimo'])
    #GD30D_Precio_Fecha = GD30D_DataFrame.drop(columns= ['Apertura', 'Máximo', 'Mínimo'])
    send_df = AL29D_DataFrame.to_sql(name=tablePsql, con=con, if_exists="append")
    send_df_1= AL30D_DataFrame.to_sql(name=tablePsql1, con=con, if_exists="append")
    send_df_2= AL30_DataFrame.to_sql(name=tablePsql12, con=con, if_exists="append")
    send_df_3= AL41D_DataFrame.to_sql(name=tablePsql3, con=con, if_exists="append")
    send_df_4= AE38D_DataFrame.to_sql(name=tablePsql4, con=con, if_exists="append")
    send_df_5= AL29_DataFrame.to_sql(name=tablePsql5, con=con, if_exists="append")
    send_df_6= AL41_DataFrame.to_sql(name=tablePsql6, con=con, if_exists="append")
    send_df_7= AE38_DataFrame.to_sql(name=tablePsql7, con=con, if_exists="append")
    send_df_8= GD30D_DataFrame.to_sql(name=tablePsql8, con=con, if_exists="append")

    print("DataFrame send to table:", tablePsql)
    print("DataFrame send to table:", tablePsql1)
    print("DataFrame send to table:", tablePsql12)
    print("DataFrame send to table:", tablePsql3)
    print("DataFrame send to table:", tablePsql4)
    print("DataFrame send to table:", tablePsql5)
    print("DataFrame send to table:", tablePsql6)
    print("DataFrame send to table:", tablePsql7)
    print("DataFrame send to table:", tablePsql8)

    os.remove("./AL30D.xlsx")
    os.remove("./AL30.xlsx")
    os.remove("./AL29D.xlsx")
    os.remove("./AL41D.xlsx")
    os.remove("./AL35D.xlsx")
    os.remove("./GD30D.xlsx")
    os.remove("./GD29D.xlsx")
    os.remove("./GD38D.xlsx")
    os.remove("./AE38D.xlsx")




except Exception as err:
    print(err)

# Query Database
try:
    query = """SELECT * FROM {};""" .format(tablePsql)
    df_database = pd.read_sql_query(query, con=con)
    print(df_database)
except Exception as err:
    print(err)
