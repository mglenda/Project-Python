import pyodbc
import pandas
import json
import sqlalchemy
import urllib

class db_connection():
    con = None
    
    def __init__(self,**kwargs):
        quoted = urllib.parse.quote_plus(kwargs['con_str'])
        engine = sqlalchemy.create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))
        self.con = engine.connect()

    def getConnection(self):
        return self.con

    def get_simple_result(self, query):
        data = pandas.read_sql(sql=query,con=self.con)
        pandas.read_sql()
        return data.iloc[0][data.columns[0]]    

def build_json(**karg):
    return json.dumps(karg)

def build_function_query(**karg):
    query = "EXEC {function} N'{json}'".format(function = karg['function'], json = karg['json'])
    return query

db = db_connection(con_str=("Driver={SQL Server Native Client 11.0};"
            "Server=10.10.10.218;"
            "Database=Mcga_Test_DB;"
            "UID=sa;"
            "PWD=AVESoft4lidi.;"
            "Trusted_Connection=no;"))

q = build_function_query(function='cust_project_python.get_bcrypt_pwd',json=build_json(uid='glenda',bcrypt_pwd='159753'))
print(q)
db_connection.get_simple_result(db,q)