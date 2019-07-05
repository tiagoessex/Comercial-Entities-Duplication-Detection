"""

Input data (all fields optional):
	data1: {name, address, nif, is_parent, ent_type, lat, lon}
	data2: {name, address, nif, is_parent, ent_type, lat, lon}


Returns:

	If an algorithm determinate that data1 and data2 are the same, then	returns the struct 
		{"DUPLICATED":1,"ALGO":X}
	where X is the algorithm number.
	
	Else, returns:
		{"DUPLICATED":0}


Usage example:

	t = DupDetector()
	d1 = {'name':"a loja 1 a treta", 'address':'r. da boavista n 50, porto, portugal', "nif":123456, "is_parent":1}
	d2 = {'name':"a loja 1 da treta", 'address':'av. da boavista n 50, porto, portugal', "nif":123456, "is_parent":1}

	print (t.isDup(d1,d2))	# returns {'DUPLICATED': 1, 'ALGO': 3}

	

requirements:
	Python 3.7.x
	fuzzywuzzy
	geopy
	phonetics

"""

from .Duplicated import DupDetector

__version__ = "0.0.2"




