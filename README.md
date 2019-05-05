

Version: 0.0.1

# Input data (all fields opctional):

* Main function:

       isDup(data1, data2, min_ratio = 90, max_radius = 50, min_size = 4, ignore = [], order = [0,1,2,3])

* Where:
	*  *data1* and *data2* are dictionaries:
			 {name, address, nif, is_parent, ent_type, lat, lon}
			 {name, address, nif, is_parent, ent_type, lat, lon}
	*	*min_ratio*: minimum Levenshtein ratio (100 => equal) (algo 0 and 2)
	*	*max_radius*: maximum geodesic distance, in meters, between two sets of coordinates (algo 1)
	*	*min_size*: all words size less min_size are eliminated (algo 3)
	*	*ignore*: list of algorithms to ignore
	*	*order*: algorithm's application order


# Returns:

* If an algorithm determinate that data1 and data2 are the same, then returns the struct *{"DUPLICATED":1,"ALGO":X}*
	where X is the algorithm number.
	
* Else, returns: *{"DUPLICATED":0}*


# Algorithms:

* Algo 1: Levenshtein over *names* and *addresses*
* Algo 2: Distance between two coordinates sets with the same *NIF*
* Algo 3: Levenshtein over the phonetic string of the *names* and *addresses*
* Algo 4: *name* and*address* of entity X is contained or contains the *name* and *address* of entity Y.


# Requirements
* Python 3.7.x
* fuzzywuzzy
* geopy
* phonetics


# Example usage


    import duplicated as duplicated
    	
    t = duplicated.DupDetector()
    d1 = {'name':"a loja 1 a treta", 'address':'r. da boavista n 50, porto, portugal', "nif":123456, "is_parent":1}
    d2 = {'name':"a loja 1 da treta", 'address':'av. da boavista n 50, porto, portugal', "nif":123456, "is_parent":1}
    
    print (t.isDup(d1,d2))	# returns {'DUPLICATED': 1, 'ALGO': 3}

