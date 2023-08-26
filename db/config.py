DATABASE_PATH = "postgres:5432"
DATABASE_NAME = "mydatabase"
USER_NAME = "myuser"
USER_PASSWORD = "mypassword"
DATABASE_URL = (
    f"postgresql+psycopg2://{USER_NAME}:{USER_PASSWORD}@{DATABASE_PATH}/{DATABASE_NAME}"
)
