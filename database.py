import os
from playhouse.db_url import connect
from peewee import PostgresqlDatabase

DATABASE_URL = os.environ.get("DATABASE_URL")
if DATABASE_URL:
	db = connect(DATABASE_URL)
else:
	DATABASE = "tibialoot"
	db = PostgresqlDatabase(DATABASE)

