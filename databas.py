import pymysql as ps

conn = ps.connect(host='localhost', user='root', passwd='1234', db='test')

curs = conn.cursor()

def db_insert(sql) :
    curs.execute(sql)
    conn.commit()
    
def db_select(sql) :
    curs.execute(sql)
    return curs.fetchall()