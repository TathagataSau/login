import psycopg2
def table():

    conn = psycopg2.connect(dbname = "postgres",user = "postgres", password = "Tathagata@124", host = "localhost", port = "5433")
    cursor = conn.cursor()
    cursor.execute('''create table employees(Name Text, ID int, Age int); ''')
    print("Table created successfully")
    conn.commit()
    conn.close()


def data():
    conn = psycopg2.connect(dbname = "postgres",user = "postgres", password = "Tathagata@124", host = "localhost", port = "5433")
    cursor = conn.cursor()
    name = input("Enter a name: ")
    id = input("Id?:")
    age = input("Age??:")
    query = '''insert into employees(Name, ID, Age) values(%s,%s,%s);'''
    #cursor.execute('''insert into employees(Name, ID, Age) values("Tathagata",12121,23); ''')

    cursor.execute(query,(name, id, age))
    print("data added successfully")
    conn.commit()
    conn.close()
"""
def extract():
    conn = psycopg2.connect(dbname = "postgres",user = "postgres", password = "Tathagata@124", host = "localhost", port = "5433")
    cursor = conn.cursor()
    cursor.execute('''select * from employees; ''')
    show = cursor.fetchone()
    print(show[2])
    conn.commit()
    conn.close()
"""

data()