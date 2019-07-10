
import duplicated as duplicated


print (duplicated.__version__)


# SANITIZED

d1 = {'name':"a loja 1 a treta", 'address':'r. da boavista n 50, porto, portugal', "nif":123456, "is_parent":1}
d2 = {'name':"a loja 1 da treta", 'address':'av. da boavista n 50, porto, portugal', "nif":123456, "is_parent":1}

print (duplicated.isDup(d1,d2))	# returns {'DUPLICATED': 0}

d1 = {'name':"a loja 1 a treta", 'address':'r. da cdsxczxcds n 50, porto, portugal', "nif":123456, "is_parent":1, "lon":10,"lat":20}
d2 = {'name':"a loja 1 da treta", 'address':'av. da boavista n 50, porto, portugal', "nif":123456, "is_parent":1, "lon":10.005,"lat":20}

print (duplicated.isDup(d1,d2))	# returns {'DUPLICATED': 0}


d1 = {'name':"a loja 1 a treta", 'address':'r. da cdsxczxcds n 50, porto, portugal', "nif":123456, "is_parent":1, "lon":10,"lat":20}
d2 = {'name':"a loja 1 da treta", 'address':'av. da boavista n 50, porto, portugal', "nif":123456, "is_parent":1, "lon":10.00005,"lat":20}

print (duplicated.isDup(d1,d2))	# returns {'DUPLICATED': 1, 'ALGO': 1}


d1 = {'name':"a loja 1 a treta", 'address':'r. da cdsxczxcds n 50, porto, portugal', "nif":123456, "is_parent":1, "lon":10,"lat":20}
d2 = {'name':"a loja 1 da treta", 'address':'av. da boavista n 50, porto, portugal', "nif":123456, "is_parent":1, "lon":10.00005,"lat":20}

print (duplicated.isDup(d1,d2, ignore=[1]))	# returns {'DUPLICATED': 0}

d1 = {'name':"a loja 1 a treta", 'address':'avenida da boavista n 50, porto, portugal', "nif":123456, "is_parent":1}
d2 = {'name':"a loja 1 da treta", 'address':'av. da boavista n 50, porto, portugal', "nif":123456, "is_parent":1}

print (duplicated.isDup(d1,d2,min_ratio = 85))	# returns {'DUPLICATED': 1, 'ALGO': 0}

d1 = {'name':"a loja 1 a treta", 'address':'avenida da boavista n 50, porto, portugal', "nif":123456, "is_parent":1}
d2 = {'name':"a loja 1 da treta", 'address':'av. da boavista n 50, porto, portugal', "nif":123456, "is_parent":1}

print (duplicated.isDup(d1,d2,min_ratio = 85, order=[3,2,1,0]))	# returns {'DUPLICATED': 1, 'ALGO': 3}



print ('\n\n')

# increase match


d1 = {'name':"a loja 1 a treta", 'address':'r. da boavista n 50, porto, portugal', "nif":123456, "is_parent":1}
d2 = {'name':"a loja 1 da treta", 'address':'av. da boavista n 50, porto, portugal', "nif":123456, "is_parent":1}

print (duplicated.isDup(d1,d2,min_ratio = 85))	# returns {'DUPLICATED': 1, 'ALGO': 0}

d1 = {'name':"a loja 1 a treta", 'address':'r. da cdsxczxcds n 50, porto, portugal', "nif":123456, "is_parent":1, "lon":10,"lat":20}
d2 = {'name':"a loja 1 da treta", 'address':'av. da boavista n 50, porto, portugal', "nif":123456, "is_parent":1, "lon":10.005,"lat":20}

print (duplicated.isDup(d1,d2, max_radius = 1000))	# returns {'DUPLICATED': 1, 'ALGO': 1}


d1 = {'name':"a loja 1 a treta", 'address':'r. da cdsxczxcds n 50, porto, portugal', "nif":123456, "is_parent":1, "lon":10,"lat":20}
d2 = {'name':"a loja 1 da treta", 'address':'av. da boavista n 50, porto, portugal', "nif":123456, "is_parent":1, "lon":10.00005,"lat":20}

print (duplicated.isDup(d1,d2))	# returns {'DUPLICATED': 1, 'ALGO': 1}


d1 = {'name':"a loja 1 a treta", 'address':'r. da cdsxczxcds n 50, porto, portugal', "nif":123456, "is_parent":1, "lon":10,"lat":20}
d2 = {'name':"a loja 1 da treta", 'address':'av. da boavista n 50, porto, portugal', "nif":123456, "is_parent":1, "lon":10.00005,"lat":20}
# too low ...
print (duplicated.isDup(d1,d2, ignore=[1], min_ratio = 50))	# returns {'DUPLICATED': 1, 'ALGO': 0}

d1 = {'name':"a loja 1 a treta", 'address':'avenida da boavista n 50, porto, portugal', "nif":123456, "is_parent":1}
d2 = {'name':"a loja 1 da treta", 'address':'av. da boavista n 50, porto, portugal', "nif":123456, "is_parent":1}

print (duplicated.isDup(d1,d2,min_ratio = 85))	# returns {'DUPLICATED': 1, 'ALGO': 0}

d1 = {'name':"a loja 1 a treta", 'address':'avenida da boavista n 50, porto, portugal', "nif":123456, "is_parent":1}
d2 = {'name':"a loja 1 da treta", 'address':'av. da boavista n 50, porto, portugal', "nif":123456, "is_parent":1}

print (duplicated.isDup(d1,d2,min_ratio = 85, order=[3,2,1,0]))	# returns {'DUPLICATED': 1, 'ALGO': 3}
