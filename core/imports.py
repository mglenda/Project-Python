import pandas as p
from zipfile import BadZipFile

def load_import(filename):
    if filename.lower().endswith(('.xlsm','xlsx')):
        try:
            data = p.read_excel(io=filename,engine="openpyxl")
            return True,data
        except FileNotFoundError:
            return False,'File was not found.'
        except BadZipFile:
            return False,'ZipFileError occured while opening the file.'
    elif filename.lower().endswith(('.xls')):
        data = p.read_excel(io=filename,engine="xlrd")
    elif filename.lower().endswith(('.csv')):
        pass
    elif filename.lower().endswith(('.xml')):
        pass
    else:
        return False,'Not supported file format.'
    return True,'File was loaded successfully.'


data = p.read_xml('C:\Project-Python\core\import_templates.xml')
print(data)