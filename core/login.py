import core.db_actions as db_actions
import core.constants as const
import core._encryptor as e

def login_verify(uid,pwd):
    db = db_actions.db_connection(con_str=("Driver={SQL Server Native Client 11.0};"
                "Server=10.10.10.218;"
                "Database=Mcga_Test_DB;"
                "UID=sa;"
                "PWD=AVESoft4lidi.;"
                "Trusted_Connection=no;"))

    q = db_actions.build_function_query(function=const.proc_get_pwd,json=db_actions.build_json(uid=uid,bcrypt_pwd=pwd))
    
    h_pwd = db.get_simple_result(q)
    if h_pwd == None:
        return False
    else:
        return e._checkPwd(pwd,h_pwd)