

Version: 0.0.1

# Input data (all fields opctional):

* Main function:

       isDup(data1, data2, min_ratio = 90, max_radius = 50, min_size = 4, ignore = [], order = [0,1,2,3], sanitize = True, checkname = False,
			check_addresses = True)

* Where:
	*  *data1* and *data2* are dictionaries:
			 {name, address, nif, is_parent, ent_type, lat, lon}
			 {name, address, nif, is_parent, ent_type, lat, lon}
	*	*min_ratio*: minimum Levenshtein ratio (100 => equal) (algo 0 and 2)
	*	*max_radius*: maximum geodesic distance, in meters, between two sets of coordinates (algo 1)
	*	*min_size*: all words size less min_size are eliminated (algo 3)
	*	*ignore*: list of algorithms to ignore
	*	*order*: algorithm's application order
	*   *sanitize*: is input is not sanitized, that is, if both the addresses and names are already processed or not (lowercase, extra-spaces removed, ...). 
	*	*checkname*: should algorithm 1 check not only the distance but also the name? (algo 1)
	*	*check_addresses*: check names and addresses or only the names? (algo 0,2,3)

# Returns:

* If an algorithm determinate that data1 and data2 are the same, then returns the struct *{"DUPLICATED":1,"ALGO":X}*
	where X is the algorithm number.
	
* Else, returns: *{"DUPLICATED":0}*

# Notes:
* Albeit all input fields are optional, algorithm selection depends on them. For example, if no name is given, then only algorithm 1 will be applied.
* *IF A FIELD HAS NO VALUE, THEN DO NOT SET IT TO NONE, JUST DO NOT INSERTED IT IN THE DATA STRUCTURE* - use the createData() function to prevent any problem.

# Algorithms:

* Algo 1: Levenshtein over *names* and, optionally also *addresses*
* Algo 2: Distance between two set of coordinates is less than X meters
* Algo 3: Levenshtein over the phonetic string of the *names* and, optionally also *addresses*
* Algo 4: *name* and, optionally also *address* of entity X is contained or contains the *name* and, optionally also  *address* of entity Y.


# Requirements
* Python 3.7.x
* fuzzywuzzy
* geopy
* phonetics


# Example 1 - using the main function *isDup* to get first algorithm to flag possible duplication:


    import duplicated as duplicated
    	
	d1 = createData(name = 'a loja 1 a treta', address = 'r. da boavista n 50, porto, portugal', nif = '123456', is_parent = 1)
	d2 = createData(name = 'a loja 1 da treta', address = 'av. da boavista n 50, porto, portugal', nif = '123456', is_parent = 1)
    
    print (duplicated.isDup(d1,d2))	# returns {'DUPLICATED': 1, 'ALGO': 3}


# Example 2 - using a particular algorithm:


    from Duplicated import *
    
    # create the data structures
	d1 = createData(name = 'a loja 1 a treta', address = 'r. da boavista n 50, porto, portugal')
	d2 = createData(name = 'a loja 1 da treta', address = 'av. da boavista n 50, porto, portugal')
	
	# sanitize ... only if needed
	# note that if isDup_2 => also set remove_all_spaces = False
	d1['name'] = sanitizeStr(d1['name'])
	d2['name'] = sanitizeStr(d2['name'])
	d1['address'] = sanitizeStr(d1['address'])
	d2['address'] = sanitizeStr(d2['address'])
	
	if isDup_0(d1,d2,min_ratio=85) and not isDup_0(d1,d2,min_ratio=90):
		return True
	else:
		return False
