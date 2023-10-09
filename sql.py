import mysql.connector
from mysql.connector import errorcode
import pandas as pd
from sqlalchemy import create_engine

try:
    engine = create_engine('mysql+mysqlconnector://root:@localhost/dev')
    print("Database connection made!")
    arquivo_csv = 'empresa_df_filtrado.csv'
    df = pd.read_csv(arquivo_csv, encoding='ISO-8859-1', sep=',')
    tabela_mysql = 'tabela_filtro'
    df.to_sql(name=tabela_mysql, con=engine, if_exists='replace', index=False)
except mysql.connector.Error as error:
    if error.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database doesn't exist")
    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("User name or password is wrong")
    else:
        print(error)
