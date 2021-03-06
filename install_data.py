from peewee import *
from database import db
from models import *



db.connect()

rashid = {"abyss hammer":20000,
        "albino plate":1500,
        "amber staff":8000,
        "ancient amulet":200,
        "assassin dagger":20000,
        "bandana":150,
        "beastslayer axe":1500,
        "beetle necklace":1500,
        "berserker":40000,
        "blacksteel sword":6000,
        "blessed sceptre":40000,
        "bone shield":80,
        "bonelord helmet":7500,
        "brutetamer's staff":1500,
        "buckle":7000,
        "castle shield":5000,
        "chain bolter":40000,
        "chaos mace":9000,
        "cobra crown":50000,
        "coconut shoes":500,
        "composite hornbow":25000,
        "cranial basher":30000,
        "crocodile boots":1000,
        "crystal crossbow":35000,
        "crystal mace":12000,
        "crystal necklace":400,
        "crystal ring":250,
        "crystal sword":600,
        "crystalline armor":16000,
        "daramian mace":110,
        "daramian waraxe":1000,
        "dark shield":400,
        "death ring":1000,
        "demon shield":30000,
        "demonbone amulet":32000,
        "demonrage sword":36000,
        "devil helmet":1000,
        "diamond sceptre":3000,
        "divine plate":55000,
        "djinn blade":15000,
        "doll":200,
        "dragon scale mail":40000,
        "dragon slayer":15000,
        "dragonbone staff":3000,
        "dreaded cleaver":10000,
        "dwarven armor":30000,
        "earth blacksteel sword":6000,
        "earth cranial basher":30000,
        "earth dragon slayer":15000,
        "earth headchopper":6000,
        "earth heroic axe":30000,
        "earth mystic blade":30000,
        "earth orcish maul":6000,
        "earth relic sword":25000,
        "earth war axe":12000,
        "elvish bow":2000,
        "emerald bangle":800,
        "energy blacksteel sword":6000,
        "energy cranial basher":30000,
        "energy dragon slayer":15000,
        "energy headchopper":6000,
        "energy heroic axe":30000,
        "energy mystic blade":30000,
        "energy orcish maul":6000,
        "energy relic sword":25000,
        "energy war axe":12000,
        "epee":8000,
        "fiery blacksteel sword":6000,
        "fiery cranial basher":30000,
        "fiery dragon slayer":15000,
        "fiery headchopper":6000,
        "fiery heroic axe":30000,
        "fiery mystic blade":30000,
        "fiery orcish maul":6000,
        "fiery relic sword":25000,
        "fiery war axe":12000,
        "flower dress":1000,
        "flower wreath":500,
        "fur boots":2000,
        "furry club":1000,
        "glacier amulet":1500,
        "glacier kilt":11000,
        "glacier mask":2500,
        "glacier robe":11000,
        "glacier shoes":2500,
        "gold ring":8000,
        "golden armor":20000,
        "golden legs":30000,
        "goo shell":4000,
        "griffin shield":3000,
        "guardian halberd":11000,
        "hammer of wrath":30000,
        "headchopper":6000,
        "heavy mace":50000,
        "heavy machete":90,
        "heavy trident":2000,
        "helmet of the lost":2000,
        "heroic axe":30000,
        "hibiscus dress":3000,
        "hieroglyph banner":1500,
        "horn (ring)":300,
        "icy blacksteel sword":6000,
        "icy cranial basher":30000,
        "icy dragon slayer":15000,
        "icy headchopper":6000,
        "icy heroic axe":30000,
        "icy mystic blade":30000,
        "icy orcish maul":6000,
        "icy relic sword":25000,
        "icy war axe":12000,
        "jade hammer":25000,
        "krimhorn helmet":200,
        "lavos armor":16000,
        "leaf legs":500,
        "leopard armor":1000,
        "leviathan's amulet":3000,
        "light shovel":300,
        "lightning boots":2500,
        "lightning headband":2500,
        "lightning legs":11000,
        "lightning pendant":1500,
        "lightning robe":11000,
        "lunar staff":5000,
        "magic plate armor":90000,
        "magma amulet":1500,
        "magma boots":2500,
        "magma coat":11000,
        "magma legs":11000,
        "magma monocle":2500,
        "mammoth fur cape":6000,
        "mammoth fur shorts":850,
        "mammoth whopper":300,
        "mastermind shield":50000,
        "medusa shield":9000,
        "mercenary sword":12000,
        "model ship":1000,
        "mycological bow":35000,
        "mystic blade":30000,
        "naginata":2000,
        "nightmare blade":35000,
        "noble axe":10000,
        "norse shield":1500,
        "orcish maul":6000,
        "oriental shoes":15000,
        "pair of iron fists":4000,
        "paladin armor":15000,
        "patched boots":2000,
        "pharaoh banner":1000,
        "pharaoh sword":23000,
        "pirate boots":3000,
        "pirate hat":1000,
        "pirate knee breeches":200,
        "pirate shirt":500,
        "pirate voodoo doll":500,
        "platinum amulet":2500,
        "ragnir helmet":400,
        "relic sword":25000,
        "rift bow":45000,
        "rift crossbow":45000,
        "rift lance":30000,
        "rift shield":50000,
        "ring of the sky":30000,
        "royal axe":40000,
        "ruby necklace":2000,
        "ruthless axe":45000,
        "sacred tree amulet":3000,
        "sapphire hammer":7000,
        "scarab amulet":200,
        "scarab shield":2000,
        "shockwave amulet":3000,
        "silver brooch":150,
        "silver dagger":500,
        "skull helmet":40000,
        "skullcracker armor":18000,
        "spiked squelcher":5000,
        "steel boots":30000,
        "swamplair armor":16000,
        "taurus mace":500,
        "tempest shield":35000,
        "terra amulet":1500,
        "terra boots":2500,
        "terra hood":2500,
        "terra legs":11000,
        "terra mantle":11000,
        "the justice seeker":40000,
        "tortoise shield":150,
        "vile axe":30000,
        "voodoo doll":400,
        "war axe":12000,
        "war horn":8000,
        "witch hat":5000,
        "wyvern fang":1500}


alesar = {"ancient shield":900,
          "black shield":800,
          "bonebreaker":10000,
          "dark armor":400,
          "dark helmet":250,
          "dragon hammer":2000,
          "dreaded cleaver":15000,
          "earth knight axe":2000,
          "energy knight axe":2000,
          "fiery knight axe":2000,
          "giant sword":17000,
          "haunted blade":8000,
          "icy knight axe":2000,
          "knight armor":5000,
          "knight axe":2000,
          "knight legs":5000,
          "mystic turban":150,
          "onyx flail":22000,
          "ornamented axe":20000,
          "poison dagger":50,
          "scimitar":150,
          "serpent sword":900,
          "skull staff":6000,
          "strange helmet":500,
          "titan axe":4000,
          "tower shield":8000,
          "vampire shield":15000,
          "warrior helmet":5000}


nahbob = {"angelic axe":5000,
          "blue robe":10000,
          "bonelord shield":1200,
          "boots of haste":30000,
          "broadsword":500,
          "butcher's axe":18000,
          "crown armor":12000,
          "crown helmet":2500,
          "crown legs":12000,
          "crown shield":8000,
          "crusader helmet":6000,
          "dragon lance":9000,
          "dragon shield":4000,
          "earth spike sword":1000,
          "earth war hammer":1200,
          "energy spike sword":1000,
          "energy war hammer":1200,
          "fiery spike sword":1000,
          "fiery war hammer":1200,
          "fire axe":8000,
          "fire sword":4000,
          "glorious axe":3000,
          "guardian shield":2000,
          "ice rapier":1000,
          "icy spike sword":1000,
          "icy war hammer":1200,
          "noble armor":900,
          "obsidian lance":500,
          "phoenix shield":16000,
          "queen's sceptre":20000,
          "royal helmet":30000,
          "shadow sceptre":10000,
          "spike sword":1000,
          "thaian sword":16000,
          "war hammer":1200}

yaman = {"ankh":100,
          "dragon necklace":100,
          "dwarven ring":100,
          "energy ring":100,
          "glacial rod":6500,
          "hailstorm rod":3000,
          "life ring":50,
          "might ring":250,
          "moonlight rod":200,
          "muck rod":6000,
          "mysterious fetish":50,
          "necrotic rod":1000,
          "northwind rod":1500,
          "protection amulet":100,
          "ring of healing":100,
          "silver amulet":50,
          "snakebite rod":100,
          "springsprout rod":3600,
          "strange talisman":30,
          "terra rod":2000,
          "time ring":100,
          "underworld rod":4400,}

haroun = {"axe ring":100,
          "bronze amulet":50,
          "club ring":100,
          "elven amulet":100,
          "garlic necklace":50,
          "life crystal":50,
          "magic light wand":35,
          "mind stone":100,
          "orb":750,
          "power ring":50,
          "stealth ring":200,
          "stone skin amulet":500,
          "sword ring":100,
          "wand of cosmic energy":2000,
          "wand of decay":1000,
          "wand of defiance":6500,
          "wand of draconia":1500,
          "wand of dragonbreath":200,
          "wand of everblazing":6000,
          "wand of inferno":3000,
          "wand of starstorm":3600,
          "wand of voodoo":4400,
          "wand of vortex":100}

yasir = {"acorn":10,
         "antlers":50,
         "ape fur":120,
          "badger fur":15,
          "bamboo stick":30,
          "banana sash":55,
          "basalt fetish":210,
          "basalt figurine":160,
          "bat decoration":2000,
          "bat wing":50,
          "bear paw":100,
          "behemoth claw":2000,
          "black hood":190,
          "black wool":300,
          "blazing bone":610,
          "blood preservation":320,
          "blood tincture in a vial":360,
          "bloody dwarven beard":110,
          "bloody pincers":100,
          "blue piece of cloth":200,
          "boggy dreads":200,
          "bola":35,
          "bone fetish":150,
          "bone shoulderplate":150,
          "bonecarving knife":190,
          "bonelord eye":80,
          "bony tail":210,
          "book of necromantic rituals":180,
          "book of prayers":120,
          "bowl of terror sweat":500,
          "brimstone fangs":380,
          "brimstone shell":210,
          "broken crossbow":30,
          "broken draken mail":340,
          "broken halberd":100,
          "broken helmet":20,
          "broken key ring":8000,
          "broken ring of ending":4000,
          "broken shamanic staff":35,
          "broken slicer":120,
          "broken throwing axe":230,
          "broken visor":1900,
          "brown piece of cloth":100,
          "bunch of troll hair":30,
          "bundle of cursed straw":800,
          "carniphila seeds":50,
          "carrion worm fang":35,
          "cat's paw":2000,
          "centipede leg":28,
          "cheese cutter":50,
          "cheesy figurine":150,
          "chicken feather":30,
          "cliff strider claw":800,
          "cobra tongue":15,
          "colourful feather":110,
          "compass":45,
          "compound eye":150,
          "condensed energy":260,
          "corrupted flag":700,
          "countess sorrow's frozen tear":50000,
          "crab pincers":35,
          "crawler head plating":210,
          "crystal bone":250,
          "crystallized anger":400,
          "cultish mask":280,
          "cultish robe":150,
          "cultish symbol":500,
          "curious matter":430,
          "cursed shoulder spikes":320,
          "cyclops toe":55,
          "damselfly eye":25,
          "damselfly wing":20,
          "dangerous proto matter":300,
          "dark rosary":48,
          "dead weight":450,
          "deepling breaktime snack":90,
          "deepling claw":430,
          "deepling guard belt buckle":230,
          "deepling ridge":360,
          "deepling scales":80,
          "deepling warts":180,
          "deeptags":290,
          "demon dust":300,
          "demon horn":1000,
          "demonic finger":1000,
          "demonic skeletal hand":80,
          "dirty turban":120,
          "downy feather":20,
          "dowser":35,
          "dracola's eye":50000,
          "dracoyle statue":5000,
          "dragon claw":8000,
          "dragon priest's wandtip":175,
          "dragon's tail":100,
          "draken sulphur":550,
          "draken wristbands":430,
          "dung ball":130,
          "earflap":40,
          "elder bonelord tentacle":150,
          "elven astral observer":90,
          "elven hoof":115,
          "elven scouting glass":50,
          "elvish talisman":45,
          "enchanted chicken wing":20000,
          "energy ball":300,
          "energy vein":270,
          "essences of a bad dream":360,
          "essence of a bad dream":360,
          "eye of a deepling":150,
          "eye of a weeper":650,
          "eye of corruption":390,
          "fiery heart":375,
          "fir cone":25,
          "fish fin":150,
          "flask of embalming fluid":30,
          "flask of warrior's sweat":10000,
          "frazzle skin":400,
          "frazzle tongue":700,
          "frost giant pelt":160,
          "frosty ear of a troll":30,
          "frosty heart":280,
          "frozen lightning":270,
          "gauze bandage":90,
          "geomancer's robe":80,
          "geomancer's staff":120,
          "ghastly dragon head":700,
          "ghostly tissue":90,
          "ghoul snack":60,
          "giant eye":380,
          "girlish hair decoration":30,
          "gland":500,
          "glistening bone":250,
          "glob of acid slime":25,
          "glob of mercury":20,
          "glob of tar":30,
          "gloom wolf fur":70,
          "goblin ear":20,
          "golden lotus brooch":270,
          "goosebump leather":650,
          "green dragon leather":100,
          "green dragon scale":100,
          "green piece of cloth":200,
          "hair of a banshee":350,
          "half-digested piece of meat":55,
          "half-eaten brain":85,
          "hardened bone":70,
          "hatched rorc egg":30,
          "haunted piece of wood":115,
          "heaven blossom":50,
          "hellhound slobber":500,
          "hellspawn tail":475,
          "hemp rope":350,
          "hideous chunk":510,
          "high guard flag":550,
          "high guard shoulderplates":130,
          "holy ash":160,
          "holy orchid":90,
          "honeycomb":40,
          "horoscope":40,
          "humongous chunk":540,
          "hunter's quiver":80,
          "hydra head":600,
          "incantation notes":90,
          "instable proto matter":300,
          "iron ore":500,
          "jewelled belt":180,
          "key to the drowned library":330,
          "kollos shell":420,
          "kongra's shoulderpad":100,
          "lancer beetle shell":80,
          "lancet":90,
          "legionnaire flags":500,
          "lion's mane":60,
          "lizard essence":300,
          "lizard leather":150,
          "lizard scale":120,
          "lost basher's spike":280,
          "lost bracers":140,
          "lost husher's staff":250,
          "luminous orb":1000,
          "lump of dirt":10,
          "lump of earth":130,
          "mad froth":80,
          "magic sulphur":8000,
          "mammoth tusk":100,
          "mantassin tail":280,
          "marsh stalker beak":65,
          "marsh stalker feather":50,
          "minotaur horn":75,
          "minotaur leather":80,
          "miraculum":60,
          "mr. punish's handcuffs":50000,
          "mutated bat ear":420,
          "mutated flesh":50,
          "mutated rat tail":150,
          "mystical hourglass":700,
          "necromantic robe":250,
          "nettle blossom":75,
          "nettle spit":25,
          "noble turban":430,
          "nose ring":2000,
          "odd organ":410,
          "ogre ear stud":180,
          "ogre nose ring":210,
          "orc leather":30,
          "orc tooth":150,
          "orcish gear":85,
          "pair of hellflayer horns":1300,
          "peacock feather fan":350,
          "pelvis bone":30,
          "perfect behemoth fang":250,
          "petrified scream":250,
          "piece of archer armor":20,
          "piece of crocodile leather":15,
          "piece of dead brain":420,
          "piece of massacre's shell":50000,
          "piece of scarab shell":45,
          "piece of swampling wood":30,
          "piece of warrior armor":50,
          "pieces of magic chalk":210,
          "pig foot":10,
          "pile of grave earth":25,
          "plasma pearls":250,
          "plasmatic lightning":270,
          "poison spider shell":10,
          "poisonous slime":50,
          "polar bear paw":30,
          "pool of chitinous glue":480,
          "protective charm":60,
          "purple robe":110,
          "quara bone":500,
          "quara eye":350,
          "quara pincers":410,
          "quara tentacle":140,
          "red dragon leather":200,
          "red dragon scale":200,
          "red hair dye":40,
          "red piece of cloth":300,
          "rope belt":66,
          "rorc egg":120,
          "rorc feather":70,
          "rotten piece of cloth":30,
          "sabretooth":400,
          "safety pin":120,
          "sandcrawler shell":20,
          "scale of corruption":680,
          "scarab pincers":280,
          "scorpion tail":25,
          "scroll of heroic deeds":230,
          "scythe leg":450,
          "sea serpent scale":520,
          "seeds":150,
          "shaggy tail":25,
          "shamanic hood":45,
          "shamanic talisman":200,
          "sight of surrender's eye":3000,
          "silencer claws":390,
          "silencer resonating chamber":600,
          "silky fur":35,
          "skeleton decoration":3000,
          "skull belt":80,
          "skull fetish":250,
          "skull shatterer":170,
          "skunk tail":50,
          "small energy ball":250,
          "small flask of eyedrops":95,
          "small notebook":480,
          "small oil lamp":150,
          "small pitchfork":70,
          "snake skin":400,
          "sniper gloves":2000,
          "solid rage":310,
          "some grimeleech wings":1200,
          "soul stone":6000,
          "spark sphere":350,
          "sparkion claw":290,
          "sparkion legs":310,
          "sparkion stings":280,
          "sparkion tail":300,
          "spellsinger's seal":280,
          "spider fangs":10,
          "spider silk":100,
          "spidris mandible":450,
          "spiked iron ball":100,
          "spirit container":40000,
          "spitter nose":340,
          "spooky blue eye":95,
          "star herb":15,
          "stone herb":20,
          "stone wing":120,
          "strand of medusa hair":600,
          "strange proto matter":300,
          "strange symbol":200,
          "striped fur":50,
          "swamp grass":20,
          "swampling moss":20,
          "swarmer antenna":130,
          "tail of corruption":240,
          "tarantula egg":80,
          "tattered piece of robe":120,
          "tentacle piece":5000,
          "terramite eggs":50,
          "terramite legs":60,
          "terramite shell":170,
          "terrorbird beak":95,
          "the handmaiden's protector":50000,
          "the imperor's trident":50000,
          "the plasmother's remains":50000,
          "thick fur":150,
          "thorn":100,
          "tooth file":60,
          "trapped bad dream monster":900,
          "troll green":25,
          "trollroot":50,
          "turtle shell":90,
          "tusk":100,
          "undead heart":200,
          "unholy bone":480,
          "vampire dust":100,
          "vampire teeth":275,
          "vampire's cape chain":150,
          "venison":55,
          "vexclaw talon":1100,
          "volatile proto matter":300,
          "warmaster's wristguards":200,
          "warwolf fur":30,
          "waspoid claw":320,
          "waspoid wing":190,
          "weaver's wandtip":250,
          "werewolf fur":380,
          "white piece of cloth":100,
          "widow's mandibles":110,
          "wimp tooth chain":120,
          "winged tail":800,
          "winter wolf fur":20,
          "witch broom":60,
          "wolf paw":70,
          "wood":5,
          "wool":15,
          "wyrm scale":400,
          "wyvern talisman":265,
          "yellow piece of cloth":150,
          "yielowax":60,
          "zaogun flag":600,
          "zaogun shoulderplates":150}

lailene = {"batwing hat":8000,
          "ethno coat":200,
          "focus cape":6000,
          "jade hat":9000,
          "spellweaver's robe":12000,
          "spirit cloak":350,
          "zaoan robe":12000}

telas = {"ancient stone":200,
          "battle stone":290,
          "broken gladiator shield":190,
          "coal":20,
          "crystal of balance":1000,
          "crystal of focus":2000,
          "crystal of power":3000,
          "crystalline spikes":440,
          "flintstone":800,
          "gear crystal":200,
          "gear wheel":500,
          "huge chunk of crude iron":15000,
          "magma clump":570,
          "metal spike":320,
          "piece of draconian steel":3000,
          "piece of hell steel":500,
          "piece of hellfire armor":550,
          "piece of royal steel":10000,
          "pulverized ore":400,
          "shiny stone":500,
          "stone nose":590,
          "sulphurous stone":100,
          "vein of ore":330,
          "war crystal":460,
          "crystal pedestal":500}

tesha = {"black pearl":280,
          "blue crystal shard":1500,
          "blue crystal splinter":400,
          "brown crystal splinter":400,
          "cyan crystal fragment":800,
          "giant shimmering pearl":3000,
          "giant shimmering pearl":3000,
          "gold ingot":5000,
          "golden figurine":3000,
          "green crystal fragment":800,
          "green crystal shard":1500,
          "green crystal splinter":400,
          "opal":500,
          "onyx chip":500,
          "red crystal fragment":800,
          "scarab coin":100,
          "small amethyst":200,
          "small diamond":300,
          "small emerald":250,
          "small rubies":250,
          "small sapphire":250,
          "small topaz":200,
          "violet crystal shard":1500,
          "wedding ring":100,
          "white pearl":160}

tamoril = {"blue gem":5000,
            "golden mug":250,
            "green gem":5000,
            "red gem":1000,
            "violet gem":10000,
            "yellow gem":1000}

bone_master = {"demonic essence":1000,
               "soul orb":25}

gold = {"gold coins":1,
        "platinum coins":100,
        "crystal coins":10000}

alexander = {"crystal ball":190,
            "life crystal":85,
            "mind stone":170,
            "spellbook of enlightenment":4000,
            "spellbook of lost souls":19000,
            "spellbook of mind control":13000,
            "spellbook of warding":8000}

esrik = {"drachaku":10000,
          "draken boots":40000,
          "drakinata":10000,
          "elite draken mail":50000,
          "guardian boots":35000,
          "sai":16500,
          "twiceslicer":28000,
          "twin hooks":500,
          "wailing widow's necklace":3000,
          "zaoan armor":14000,
          "zaoan halberd":500,
          "zaoan helmet":45000,
          "zaoan legs":14000,
          "zaoan shoes":5000,
          "zaoan sword":30000}

player_items = {"ultimate health potion":250,
                "great mana potion":80}


npc_list = [rashid, nahbob, haroun, alesar, yaman, yasir, lailene, telas, tesha, tamoril, alexander, esrik, bone_master, gold, player_items]
database_list = [Rashid, Nahbob, Haroun, Alesar, Yaman, Yasir, Lailene, Telas, Tesha, Tamoril, Alexander, Esrik, Bone_master, Gold, Player_items]

for i in range(len(npc_list)):
	for item, value in npc_list[i].items():
		database_list[i].create(item_name=item, price=value)

