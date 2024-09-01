"""delete.py"""

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
                DELETE FROM Salary
                WHERE id = 3;
                """
            cursor.execute(query)
except (Exception, Error) as error:
    print("Error", error)