import psycopg2
import time

while True:
    try:
        conn = psycopg2.connect(
            dbname="mydatabase", user="myuser", password="mypassword", host="postgres"
        )
        conn.close()
        print("Postgres is ready!")
        break
    except psycopg2.OperationalError:
        print("Waiting for postgres...")
        time.sleep(2)
