


from Duplicated import DupDetector




#####
# 1 #
#####
def test1_0():
	t = DupDetector()
	d1 = {'name':"bar a treta", 'address':'r. da boavista n 50, porto, portugal'}
	d2 = {'name':"bar da treta", 'address':'av. da boavista n 50, porto, portugal'}
	if t.isDup_0(d1,d2,min_ratio=85) and not t.isDup_0(d1,d2,min_ratio=90):
		return True
	else:
		return False

def test1_1():
	t = DupDetector()
	d1 = {'name':"bar a treta", 'address':'r. da boavista n 50, porto, portugal'}
	d2 = {'name':"bar da treta", 'address':'av. sá da bandeira n 50, porto, portugal'}

	if not t.isDup_0(d1,d2,min_ratio=80) and t.isDup_0(d1,d2,min_ratio=50):
		return True
	else:
		return False

def test1_2():
	t = DupDetector()
	d1 = {'name':"bar a treta", 'address':'r. da boavista n 50, porto, portugal', "nif":123456}
	d2 = {'name':"bar da treta", 'address':'av. da boavista n 50, porto, portugal'}
	if not t.isDup_0(d1,d2,min_ratio=80):
		return True
	else:
		return False

def test1_3():
	t = DupDetector()
	d1 = {'name':"bar a treta", 'address':'r. da boavista n 50, porto, portugal', "nif":123456}
	d2 = {'name':"bar da treta", 'address':'av. da boavista n 50, porto, portugal', "nif":123456}

	if t.isDup_0(d1,d2,min_ratio=85):
		return True
	else:
		return False
		
def test1_4():
	t = DupDetector()
	d1 = {'name':"bar a treta", 'address':'r. da boavista n 50, porto, portugal', "nif":123456}
	d2 = {'name':"bar da treta", 'address':'av. da boavista n 50, porto, portugal', "nif":6543321}

	if not t.isDup_0(d1,d2,min_ratio=85):
		return True
	else:
		return False

def test1_5():
	t = DupDetector()
	d1 = {'name':"o bar 1 a treta", 'address':'r. da boavista n 50, porto, portugal', "nif":123456}
	d2 = {'name':"o bar 2 da treta", 'address':'av. da boavista n 50, porto, portugal', "nif":123456}

	if not t.isDup_0(d1,d2,min_ratio=85):
		return True
	else:
		return False

def test1_6():
	t = DupDetector()
	d1 = {'name':"a loja 1 a treta", 'address':'r. da boavista n 50, porto, portugal', "nif":123456}
	d2 = {'name':"a loja 1 da treta", 'address':'av. da boavista n 50, porto, portugal', "nif":123456}

	if t.isDup_0(d1,d2,min_ratio=85):
		return True
	else:
		return False
		
def test1_7():
	t = DupDetector()
	d1 = {'name':"a loja 1 a treta", 'address':'r. da boavista n 50, porto, portugal', "nif":123456, "is_parent":1}
	d2 = {'name':"a loja 1 da treta", 'address':'av. da boavista n 50, porto, portugal', "nif":123456}

	if not t.isDup_0(d1,d2,min_ratio=85):
		return True
	else:
		return False
		
def test1_8():
	t = DupDetector()
	d1 = {'name':"a loja 1 a treta", 'address':'r. da boavista n 50, porto, portugal', "nif":123456, "is_parent":1}
	d2 = {'name':"a loja 1 da treta", 'address':'av. da boavista n 50, porto, portugal', "nif":123456, "is_parent":0}

	if not t.isDup_0(d1,d2,min_ratio=85):
		return True
	else:
		return False
		





#####
# 2 #
#####
def test2_0():
	t = DupDetector()
	d1 = {'nif':123456,'lon':8.0,'lat':40.0}
	d2 = {'nif':123456,'lon':8.0,'lat':40.0}

	if t.isDup_1(d1,d2) == True:
		return True
	else:
		return False


def test2_1():
	t = DupDetector()
	d1 = {'nif':123456,'lon':8.0,'lat':40.0}
	d2 = {'nif':654321,'lon':8.0,'lat':40.0}

	if t.isDup_1(d1,d2) == False:
		return True
	else:
		return False

def test2_2():
	t = DupDetector()
	d1 = {'nif':123456,'lon':8.0,'lat':80.0}
	d2 = {'nif':123456,'lon':8.0,'lat':40.0}

	if t.isDup_1(d1,d2) == False:
		return True
	else:
		return False

def test2_3():
	t = DupDetector()
	d1 = {'nif':123456,'lon':8.0,'lat':40.0}
	d2 = {'nif':123456,'lon':8.0,'lat':40.00005}

	if t.isDup_1(d1,d2) == True:
		return True
	else:
		return False

def test2_4():
	t = DupDetector()
	d1 = {'nif':123456,'lon':8.0,'lat':40.0}
	d2 = {'nif':123456,'lon':8.0,'lat':45.0}

	if t.isDup_1(d1,d2,max_radius=1000000) == True:	# 1000 km
		return True
	else:
		return False

def test2_5():
	t = DupDetector()
	d1 = {'nif':123456,'lon':8.0,'lat':40.0,'is_parent':1}
	d2 = {'nif':123456,'lon':8.0,'lat':40.0}

	if t.isDup_1(d1,d2) == False:
		return True
	else:
		return False

def test2_6():
	t = DupDetector()
	d1 = {'nif':123456,'lon':8.0,'lat':40.0,'is_parent':1}
	d2 = {'nif':123456,'lon':8.0,'lat':40.0,'is_parent':0}

	if t.isDup_1(d1,d2) == False:
		return True
	else:
		return False

def test2_7():
	t = DupDetector()
	d1 = {'nif':123456,'lon':8.0,'lat':40.0,'ent_type':None}
	d2 = {'nif':123456,'lon':8.0,'lat':40.0,'is_parent':1}

	if t.isDup_1(d1,d2) == False:
		return True
	else:
		return False

def test2_8():
	t = DupDetector()
	d1 = {'nif':123456,'lon':8.0,'lat':40.0,'ent_type':1, 'is_parent':1}
	d2 = {'nif':123456,'lon':8.0,'lat':40.0,'ent_type':1, 'is_parent':1}

	if t.isDup_1(d1,d2) == True:
		return True
	else:
		return False
		

def test2_9():
	t = DupDetector()
	d1 = {'nif':123456,'lon':8.0,'lat':40.0,'ent_type':None, 'is_parent':1}
	d2 = {'nif':123456,'lon':8.0,'lat':40.0,'ent_type':None, 'is_parent':1}

	if t.isDup_1(d1,d2) == True:
		return True
	else:
		return False


#####
# 3 #
#####
def test3_0():
	t = DupDetector()
	d1 = {'name':"bar a treta", 'address':'r. da boavista n 50, porto, portugal'}
	d2 = {'name':"bar da treta", 'address':'av. da boavista n 50, porto, portugal'}

	if t.isDup_2(d1,d2,min_ratio=85) and not t.isDup_2(d1,d2,min_ratio=90):
		return True
	else:
		return False

def test3_1():
	t = DupDetector()
	d1 = {'name':"bar a treta", 'address':'r. da boavista n 50, porto, portugal'}
	d2 = {'name':"bar da treta", 'address':'av. sá da bandeira n 50, porto, portugal'}

	if not t.isDup_2(d1,d2,min_ratio=80) and t.isDup_2(d1,d2,min_ratio=40):
		return True
	else:
		return False

def test3_2():
	t = DupDetector()
	d1 = {'name':"bar a treta", 'address':'r. da boavista n 50, porto, portugal', "nif":123456}
	d2 = {'name':"bar da treta", 'address':'av. da boavista n 50, porto, portugal'}

	if not t.isDup_2(d1,d2,min_ratio=80):
		return True
	else:
		return False

def test3_3():
	t = DupDetector()
	d1 = {'name':"bar a treta", 'address':'r. da boavista n 50, porto, portugal', "nif":123456}
	d2 = {'name':"bar da treta", 'address':'av. da boavista n 50, porto, portugal', "nif":123456}

	if t.isDup_2(d1,d2,min_ratio=85):
		return True
	else:
		return False
		
def test3_4():
	t = DupDetector()
	d1 = {'name':"bar a treta", 'address':'r. da boavista n 50, porto, portugal', "nif":123456}
	d2 = {'name':"bar da treta", 'address':'av. da boavista n 50, porto, portugal', "nif":6543321}

	if not t.isDup_2(d1,d2,min_ratio=85):
		return True
	else:
		return False

def test3_5():
	t = DupDetector()
	d1 = {'name':"o bar 1 a treta", 'address':'r. da boavista n 50, porto, portugal', "nif":123456}
	d2 = {'name':"o bar 2 da treta", 'address':'av. da boavista n 50, porto, portugal', "nif":123456}

	if not t.isDup_2(d1,d2,min_ratio=85):
		return True
	else:
		return False

def test3_6():
	t = DupDetector()
	d1 = {'name':"a loja 1 a treta", 'address':'r. da boavista n 50, porto, portugal', "nif":123456}
	d2 = {'name':"a loja 1 da treta", 'address':'av. da boavista n 50, porto, portugal', "nif":123456}

	if t.isDup_2(d1,d2,min_ratio=85):
		return True
	else:
		return False
		
def test3_7():
	t = DupDetector()
	d1 = {'name':"a loja 1 a treta", 'address':'r. da boavista n 50, porto, portugal', "nif":123456, "is_parent":1}
	d2 = {'name':"a loja 1 da treta", 'address':'av. da boavista n 50, porto, portugal', "nif":123456}

	if not t.isDup_2(d1,d2,min_ratio=85):
		return True
	else:
		return False
		
def test3_8():
	t = DupDetector()
	d1 = {'name':"a loja 1 a treta", 'address':'r. da boavista n 50, porto, portugal', "nif":123456, "is_parent":1}
	d2 = {'name':"a loja 1 da treta", 'address':'av. da boavista n 50, porto, portugal', "nif":123456, "is_parent":0}

	if not t.isDup_2(d1,d2,min_ratio=85):
		return True
	else:
		return False
		




#####
# 4 #
#####
def test4_0():
	t = DupDetector()
	d1 = {'name':"bar a treta", 'address':'r. da boavista n 50, porto, portugal'}
	d2 = {'name':"bar da treta", 'address':'av. da boavista n 50, porto, portugal'}

	if t.isDup_3(d1,d2,min_size=4):
		return True
	else:
		return False

def test4_1():
	t = DupDetector()
	d1 = {'name':"bar a treta", 'address':'praceta da boavista n 50, porto, portugal'}
	d2 = {'name':"bar da treta", 'address':'av. da boavista n 50, porto, portugal'}

	if not t.isDup_3(d1,d2,min_size=4):
		return True
	else:
		return False


def test4_2():
	t = DupDetector()
	d1 = {'name':"bar a treta", 'address':'rua da boavista n 50, porto, portugal', "nif":123456}
	d2 = {'name':"bar da treta", 'address':'av. da boavista n 50, porto, portugal', "nif":654321,"is_parent":1}

	if not t.isDup_3(d1,d2,min_size=4):
		return True
	else:
		return False

def test4_3():
	t = DupDetector()
	d1 = {'name':"bar a treta", 'address':'rua da boavista n 50, porto, portugal', "nif":123456, "is_parent":1}
	d2 = {'name':"bar da treta", 'address':'av. da boavista n 50, porto, portugal', "nif":123456, "is_parent":1}

	if t.isDup_3(d1,d2,min_size=4):
		return True
	else:
		return False



def runTests():
	if test1_0() and test1_1() and test1_2() and test1_3() and test1_4() and test1_5() and test1_6() and test1_7() and test1_8():
		print ("TEST 1 [OK]")
	else:
		print ("TEST 1 [NOT OK]")


	if test2_0() and test2_1() and test2_2() and test2_3() and test2_4() and test2_5() and test2_6() and test2_7() and test2_8() and test2_9():
		print ("TEST 2 [OK]")
	else:
		print ("TEST 2 [NOT OK]")

	if test3_0() and test3_1() and test3_2() and test3_3():# and test3_4() and test3_5() and test3_6() and test3_7() and test3_8():
		print ("TEST 3 [OK]")
	else:
		print ("TEST 3 [NOT OK]")

	if test4_0() and test4_1() and test4_2() and test4_3():
		print ("TEST 4 [OK]")
	else:
		print ("TEST 4 [NOT OK]")



if __name__ == '__main__':
	runTests()
