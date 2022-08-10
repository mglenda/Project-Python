import db_con

result = db_con.run_query('SELECT TOP 10 IdPripad FROM Pripady')
db_con.transpose_result(result)