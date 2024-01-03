import sqlite3
def connection (db_name):
    connetion=None
    try:
        connetion = sqlite3.connect(db_name)
    except sqlite3.Error as error:
        print(error)
    return connetion
def result(connection,ask):
    sql='''SELECT s.first_name, s.last_name,o.title, g.title,g.area AS city FROM student AS s
    INNER JOIN cities AS g ON g.id=s.city_id
    INNER JOIN countries AS o ON o.id=g.country_id
    WHERE g.id=?'''
    try:
        cursor=connection.cursor()
        cursor.execute(sql,(ask,))
        result=cursor.fetchall()
        for i in result:
            print(*i)
    except sqlite3.Error as error:
        print(error)

def listofcity(connection):
    sql = '''SELECT id,title FROM cities'''
    try:
        cursor=connection.cursor()
        cursor.execute(sql)
        row=cursor.fetchall()
        for i in row:
            print(*i)
    except sqlite3.Error as g:
        print(g)

print("Вы можете отобразить список учеников \n"
          "по выбранному id города из перечня городов ниже,\n"
          " для выхода из программы введите 0 ")
my_con=connection("hw8.db")
listofcity(my_con)
my_con.close()
while True:
    my_con = connection("hw8.db")
    s=int(input("Ваш запрос: "))
    if s != 0 and s<=7:
        result(my_con,s)
        my_con.close()
    else:
        my_con.close()
        break