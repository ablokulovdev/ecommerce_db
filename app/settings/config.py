from decouple import config


DBNAME=config("DB_NAME")
USER=config("DB_USER")
PASS=config("DB_PASS")
HOST=config("DB_HOST")
PORT=config("DB_PORT")