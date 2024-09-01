"""fetch2.py"""

import psycopg2
from psycopg2 import Error
try:
    with psycopg2.connect(
    user="postgres",
    password="2015karl",
    host="127.0.0.1",
    port="5432",
    database="postgre_db") as connection:
        with connection.cursor() as cursor:
            query = """
                SELECT * FROM Salary
                WHERE id = 1;
                """
            cursor.execute(query)
            rows = cursor.fetchall()
            print("Данные из таблицы Salary:") 
            for row in rows: 
                print(row) 
except (Exception, Error) as error:
    print("Error", error)