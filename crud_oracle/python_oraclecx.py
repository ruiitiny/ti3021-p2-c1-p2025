import oracledb 
import os 
from dotenv import load_dotenv 

load_dotenv()

un = "SYS"
cs = "localhost/orclpdb"
pw = "inacap" #os.getenv("ORACLE_PASSWORD")

with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
    with connection.cursor() as cursor:
        sql = "select sysdate from dual"
        respuesta = cursor.execute(sql)
        for fila in respuesta:
            print(fila)
            