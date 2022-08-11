import db_con

#result = db_con.run_query('SELECT TOP 10 IdPripad FROM Pripady ORDER BY IdPripad DESC')
#db_con.transpose_result(result)
def scope_test():
    spam = None
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = None
        def do_nonlocal_2():
            nonlocal spam
            spam = "nonlocal spam"
        do_nonlocal_2()

    def do_global():
        global spam
        spam = "global spam"
    do_nonlocal()
    do_global()
    print("After global assignment:", spam)

def test():
    print(spam)

scope_test()
test()