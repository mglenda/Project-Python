import pyodbc 

def connect():
    return pyodbc.connect('Driver={SQL Server};'
                        'Server=10.10.10.218;'
                        'Database=E8_PROD_MCGA;'
                        'UID=sa;'
                        'PWD=AVESoft4lidi.;')
    

def run_query(query):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor

def transpose_result(cursor:pyodbc.Cursor):
    try:
        result = cursor.fetchall()
        for row in result:
            print(row,end=',')
        result.sort(key=lambda row:row[0])
        for row in result:
            print(row,end=',')
    finally:
        cursor.close()