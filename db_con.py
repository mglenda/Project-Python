import pyodbc 

def connect():
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=10.10.10.218;'
                        'Database=E8_PROD_MCGA;'
                        'UID=sa;'
                        'PWD=AVESoft4lidi.;')
    return conn

def run_query(query):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor

def transpose_result(cursor:pyodbc.Cursor):
    try:
        for row in cursor:
            print(row)
    finally:
        cursor.close()