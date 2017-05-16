from peewee import PostgresqlDatabase, Model, CharField, BooleanField, ForeignKeyField
from flask_security import UserMixin, RoleMixin
from playhouse.db_url import connect
from database import db

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


class User(Model, UserMixin):
	email = CharField(unique=True)
	password = CharField()
	active = BooleanField(default=True)

	class Meta:
		database = db

class Role(Model, RoleMixin):
	name = CharField(unique=True)
	description = CharField(null=True)

	class Meta:
		database = db

class UserRoles(Model):
	user = ForeignKeyField(User, related_name="roles")
	role = ForeignKeyField(User, related_name="users")
	name = property(lambda self: self.role.name)
	description = property(lambda self: self.role.description)

	class Meta:
		database = db