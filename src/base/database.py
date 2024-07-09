import pyodbc 

class Database:
    def __init__(self):
        # "Driver={SQL Server Native Client 11.0};" 
        self.conn_str = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=172.16.0.3;"
            "DATABASE=Otimizah.Sankhya.Teste;" 
            #"DATABASE=Otimizah.Rinen.Teste;"
            "UID=sa;"
            "PWD=Xibat@69;"
        )
    
    def connect(self):
        conn = pyodbc.connect(self.conn_str)
        return conn
        
    def sql_query(self, sql):
        try:
            with pyodbc.connect(self.conn_str) as conn:
                with conn.cursor() as cursor:
                    cursor.execute(sql)
                    rows = cursor.fetchall()
                    return rows
        except pyodbc.Error as e:
            print(f'Error connecting to SQL Server: {e}')
        except Exception as ex:
            print(f'Error connecting to SQL Server: {ex}')            
