import pyodbc
import pandas
import json
import sqlalchemy
import urllib

class db_connection():
    def __init__(self,**kwargs):
        quoted = urllib.parse.quote_plus(kwargs['con_str'])
        self.engine = sqlalchemy.create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))
        self.con = self.engine.connect()

    def getConnection(self):
        return self.con
    
    def getEngine(self):
        return self.engine

    def get_simple_result(self, query):
        data = pandas.read_sql(sql=sqlalchemy.text(query),con=self.con)
        try:
            return data.iloc[0][data.columns[0]]    
        except IndexError:
            return None


def build_json(**karg):
    return json.dumps(karg)

def build_function_query(**karg):
    query = "EXEC {function} N'{json}'".format(function = karg['function'], json = karg['json'])
    return query