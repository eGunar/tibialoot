from models import *

DATABASE = "tibialoot"
db = PostgresqlDatabase(DATABASE)

db.connect()
db.create_tables([
				Rashid, Nahbob,
				Haroun, Alesar,
			  	Yaman, Yasir,
			   	Lailene, Telas,
			    Tesha, Tamoril,
		    	Alexander, Esrik,
		      	Bone_master, Player_items,
		        Gold, User,
		        Role, UserRoles
		        ], safe=True)

