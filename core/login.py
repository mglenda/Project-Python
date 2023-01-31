import db_actions as db_actions
import constants as const

db = db_actions.db_connection(con_str=("Driver={SQL Server Native Client 11.0};"
            "Server=10.10.10.218;"
            "Database=Mcga_Test_DB;"
            "UID=sa;"
            "PWD=AVESoft4lidi.;"
            "Trusted_Connection=no;"))

q = db_actions.build_function_query(function=const.proc_get_pwd,json=db_actions.build_json(uid='glenda',bcrypt_pwd='159753'))
print(db.get_simple_result(q))