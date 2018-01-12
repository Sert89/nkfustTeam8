import sqlite3
def queryTableList():
    connection=sqlite3.connect('../DB/login.db')
    try:
        connection.execute("CREATE TABLE USERS(USERNAME TEXT NOT NULL,EMAIL TEXT NOT NULL,"
                           "PASSWORD TEXT NOT NULL )")
        connection.commit()
    except:
        pass
    result=connection.execute("SELECT * FROM USERS")
    for data in result:
        print("使用者名稱:{}\nEmail電子郵件:{}\n密碼:{}\n".format(
            data[0],data[1],data[2]
        ))
    connection.close()
queryTableList()