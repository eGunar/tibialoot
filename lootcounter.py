from peewee import *
from models import *
import re



def remove_text_within_brackets(string):
    ret = ''
    skip1c = 0
    skip2c = 0
    for i in string:
        if i == '[':
            skip1c += 1
        elif i == '(':
            skip2c += 1
        elif i == ']' and skip1c > 0:
            skip1c -= 1
        elif i == ')'and skip2c > 0:
            skip2c -= 1
        elif skip1c == 0 and skip2c == 0:
            ret += i
    return ret

def arrange_list(loot_info):

	loot = loot_info
	try:
		if "Channel Server Log" in loot[1]:
			looted = list(loot[2:-1])
		else:
			looted = list(loot)
		loot = []
		for item in range(len(looted)):
			try:
				if "You see" in looted[item] or "weigh" in looted[item]:
					loot.append(looted[item])
			except IndexError:
				break

		loot = [loot[x:x+2] for x in range(0, len(loot), 2)]
		return loot
	except IndexError:
		return "error"
	
#requires the first letter of the npc to be CAPS
def count_loot(npc, lista):
	loot_value = 0
	loot = lista
	for item in loot:
		for i in npc.select():
			if i.item_name in item[0]:
				item[0] = remove_text_within_brackets(item[0])
				item_amount = [int(s) for s in item[0].split() if s.isdigit()]
				try:
					if item_amount[0] > 0:
						loot_value += int(i.price)*item_amount[0]
					else:
						loot_value += int(i.price)
				except IndexError:
					loot_value += int(i.price)
	return [str(npc.__name__),loot_value]

def run(serverlog):
	loot_list = arrange_list(serverlog)
	information_list = []
	npc_list = [Alesar, Rashid, Nahbob, Tesha, Haroun, Yaman, Yasir, Lailene, Telas, Tamoril, Alexander, Esrik, Bone_master, Player_items, Gold]
	for npcs in npc_list:
		information_list.append(count_loot(npcs, loot_list))
	return information_list

