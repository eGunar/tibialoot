from peewee import *

DATABASE = "tibialoot"
db = PostgresqlDatabase(DATABASE)

class Rashid(Model):
	item_name = CharField()
	price = CharField()

	class Meta:
		database = db


class Nahbob(Model):
	item_name = CharField()
	price = CharField()

	class Meta:
		database = db

class Haroun(Model):
	item_name = CharField()
	price = CharField()

	class Meta:
		database = db


class Alesar(Model):
	item_name = CharField()
	price = CharField()

	class Meta:
		database = db

class Yaman(Model):
	item_name = CharField()
	price = CharField()

	class Meta:
		database = db

class Yasir(Model):
	item_name = CharField()
	price = CharField()

	class Meta:
		database = db

class Lailene(Model):
	item_name = CharField()
	price = CharField()

	class Meta:
		database = db

class Telas(Model):
	item_name = CharField()
	price = CharField()

	class Meta:
		database = db

class Tesha(Model):
	item_name = CharField()
	price = CharField()

	class Meta:
		database = db

class Tamoril(Model):
	item_name = CharField()
	price = CharField()

	class Meta:
		database = db

class Alexander(Model):
	item_name = CharField()
	price = CharField()

	class Meta:
		database = db

class Esrik(Model):
	item_name = CharField()
	price = CharField()

	class Meta:
		database = db

class Bone_master(Model):
	item_name = CharField()
	price = CharField()

	class Meta:
		database = db

class Player_items(Model):
	item_name = CharField()
	price = CharField()

	class Meta:
		database = db

class Gold(Model):
	item_name = CharField()
	price = CharField()

	class Meta:
		database = db