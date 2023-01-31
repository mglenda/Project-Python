import bcrypt
 
def _genHash(pwd):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pwd.encode('utf-8'),salt)

def _checkPwd(pwd,h_str):
    return bcrypt.checkpw(pwd.encode('utf-8'), h_str.encode('utf-8'))