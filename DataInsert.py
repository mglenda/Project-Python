import pandas as pd
import sqlalchemy as sa
from sqlalchemy import create_engine
import urllib
import pyodbc

df = pd.read_excel('C:\\Users\\mrmgl\\Desktop\\ph_Imports\\imports_ph.xlsx', engine = 'openpyxl')

quoted = urllib.parse.quote_plus("DRIVER={SQL Server Native Client 11.0};SERVER=10.40.10.30;DATABASE=E8_PROD_MCGA;UID=sa;PWD=AVESoft4lidi!!!;Trusted_Connection=no;")
engine = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))

df.to_sql(name='insertor',con=engine,schema='cust_data',if_exists='replace',index=False,method='multi',chunksize=1000
,dtype={'VS': sa.types.NVARCHAR(length=50),'IMPORT_DATE':  sa.types.DATE()})