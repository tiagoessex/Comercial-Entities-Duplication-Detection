# pip install fuzzywuzzy
# pip install python-Levenshtein
# pip install geopy
# pip install phonetics


import unicodedata
import re
import sys

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import geopy.distance
import phonetics




class DupDetector():

	abreviaturas = {
		"al":"alameda", "av":"avenida", "az":"azinhaga", "br":"bairro",
		"bc":"beco", "cc":"calcada", "ccnh":"calcadinha", "cam":"caminho",
		"csl":"casal", "esc":"escadas", "escnh":"escadinhas", "estr":"estrada",
		"est":"estrada", "en":"estrada nacional", "jrd":"jardim", "lg":"largo",
		"loteam":"loteamento", "pq":"parque", "pto":"patio", "pc":"praca",
		"pct":"praceta", "prolng":"prolongamento", "qta":"quinta", "rot":"rotunda",
		"r":"rua", "transv":"transversal", "tv":"travessa", "trav":"travessa",
		"urb":"urbanizacao", "vl":"vila", "zn":"zona", "cv":"cave", "dto":"direito",
		"esq":"esquerdo", "ft":"frente", "hab":"habitacao", "lj":"loja",
		"rc":"res do chao", "slj":"sobre loja", "scv ":"sub cave ", "bl ":"bloco ",
		"edf ":"edificio ", "lt ":"lote ", "tr ":"torre ", "vv ":"vivenda ",
		"alf":"alferes", "alm":"almirante", "arq":"arquiteto", "brig":"brigadeiro",
		"cap":"capitao", "cmdt":"comandante", "comend":"comendador", "cons":"conselheiro",
		"cor":"coronel", "d":"dom", "d":"dona", "dr":"doutor", "dr":"doutora",
		"dq":"duque", "bem":"embaixador", "eng":"engenheira", "eng":"engenheiro",
		"fr":"frei", "gen":"general", "inf":"infante", "mq":"marques",
		"presid":"presidente", "prof":"professor", "prof":"professora",
		"s":"sao", "sarg":"sargento", "ten":"tenente", "visc":"visconde",
		"ass":"associacao", "inst":"instituto", "lug":"lugar", "min":"ministerio",
		"proj":"projetada", "numero":"sem", "soc":"sociedade", "univ":"universidade",
		"b":"bloco", "e":"edificio", "l":"lote", "t":"torre", "n":"numero"
	}


	#SIM_RATIO_MIN = 90

	def __init__(self):
		pass

	############################
	#	SETUP AND CLEANING OPS #
	############################

	# replace all special chars for non special
	# ex: áâãàç -> aaac
	def replacePTChars(self, s):
		return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))


	# if not number or letter then be replaced by by_what
	def replaceAllNonAlfaNum(self, s, by_what=" "):
		return re.sub('[^A-Za-z0-9]+', by_what, s)
		
	# including trailing spaces
	def removeAllExtraSpaces(self, s):
		#return re.sub(' +', ' ',s)
		return " ".join(s.split())
	
	# basically, it joins all words into one
	def removeAllSpaces(self, s):		
		return s.replace(' ','')


	# replaces all tokens that have a correspondence in the abreviaturas list
	# ex: s = "EN 5 lt 10 porto" -> "ESTRADA NACIONAL 5 LOTE 10 PORTO"  
	def replaceAbrevs(self, addr):
		tokens = addr.split(' ')
		for i in range(len(tokens)):
			if tokens[i] in self.abreviaturas:
				tokens[i] = self.abreviaturas[tokens[i]]
		return ' '.join(tokens)


	# in some algorithms small words can be considered noise and as such
	# irrelevant
	def removeSmallWords(self, s):
		remove_list = ['DE','DO','DA','DOS','DAS']
		word_list = s.split()	
		ss = ' '.join([i for i in word_list if i not in remove_list])
		#ss = re.sub(r'\b\w{1,3}\b', '', s)
		return ss

	# prepare/clean the address
	def sanitizeMorada(self, addr, remove_all_spaces = False):
		temp = addr.lower()	
		temp = self.replacePTChars(temp)
		temp = self.replaceAllNonAlfaNum(temp)
		temp = self.replaceAbrevs(temp)
		temp = self.removeSmallWords(temp)
		temp = self.removeAllExtraSpaces(temp)
		if not remove_all_spaces:
			temp = self.removeAllExtraSpaces(temp)
		else:
			temp = self.removeAllSpaces(temp)
		return temp
		
	# prepare/clean the name
	def sanitizeNome(self, nome, remove_all_spaces = False):
		temp = nome.lower()	
		temp = self.replacePTChars(temp)
		temp = self.replaceAllNonAlfaNum(temp)
		temp = self.removeSmallWords(temp)
		temp = self.removeAllExtraSpaces(temp)
		if not remove_all_spaces:
			temp = self.removeAllExtraSpaces(temp)
		else:
			temp = self.removeAllSpaces(temp)
		return temp

	def keepOnlyWords(self, s):
		return [s1 for s1 in s if s1.isalpha()]

	def keepIfMinSize(self, s,n):
		return [s1 for s1 in s if (len(s1) >= n or not s1.isalpha()) ]




	##############
	# OPERATIONS #
	##############

	def getRatioNome(self, str1, str2):
		return fuzz.ratio(str1,str2)
		
	def getRatioMorada(self, str1, str2):
		return fuzz.ratio(str1,str2)

	def getPhoneticsRatioNome(self, str1, str2):
		return fuzz.ratio(phonetics.metaphone(str1),phonetics.metaphone(str2))
		
	def getPhoneticsRatioMorada(self, str1, str2):
		return fuzz.ratio(phonetics.metaphone(str1),phonetics.metaphone(str2))

	def isSameNumbers(self, s1, s2, keyword):
		match1 = re.search(keyword + '\s*(\d+)', s1)
		match2 = re.search(keyword + '\s*(\d+)', s2)
		if match1 and match2:
			if match1.group(1) == match2.group(1):
				return True
		return False


	def isNameIn(self, s1, s2 ,n):
		temp1 = self.keepIfMinSize(self.removeAllExtraSpaces(s1).split(" "),n)
		temp2 = self.keepIfMinSize(self.removeAllExtraSpaces(s2).split(" "),n)
		return set(temp1).issubset(temp2) or set(temp2).issubset(temp1)

	def isAddressIn(self, s1, s2 ,n):
		temp1 = self.keepIfMinSize(self.removeAllExtraSpaces(s1).split(" "),n)
		temp2 = self.keepIfMinSize(self.removeAllExtraSpaces(s2).split(" "),n)
		return set(temp1).issubset(temp2) or set(temp2).issubset(temp1)



	##############
	# ALGO IMPL  #
	##############

	# returns true if similar
	# data: {name=not null, address=not null, nif=null, is_parent=null, ent_type=null}
	# if any of nif or is_parent or ent_type are mising from 1 ent, then different
	def isDup_0(self, data1, data2, min_ratio = 90):
		if 'name' not in data1 or 'name' not in data2:
			raise RuntimeError('Error: missing name(s)!')
		if 'address' not in data1 or 'address' not in data2:
			raise RuntimeError('Error: missing address(s)!')
	
	
	
		if 'nif' in data1 and 'nif' not in data2:
			return False
		if 'nif' not in data1 and 'nif' in data2:
			return False		
			
		if 'is_parent' in data1 and 'is_parent' not in data2:
			return False
		if 'is_parent' not in data1 and 'is_parent' in data2:
			return False
			
		if 'ent_type' in data1 and 'ent_type' not in data2:
			return False
		if 'ent_type' not in data1 and 'ent_type' in data2:
			return False					

		# if nifs <> and not false => False
		if 'nif' in data1 and 'nif' in data2:
			if data1['nif'] != data2['nif']:
				return False
		
		
		
		isBar = False
		isLoja = False
		n1 = self.sanitizeNome(data1['name'])
		n2 = self.sanitizeNome(data2['name'])
		m1 = self.sanitizeMorada(data1['address'])
		m2 = self.sanitizeMorada(data2['address'])
		
		if ' bar ' in n1:
			isBar = True
		if ' loja ' in n1:
			isLoja = True
		
		
		if self.getRatioNome(n1,n2) > min_ratio and self.getRatioMorada(m1,m2) > min_ratio:
			if isBar:
				if not self.isSameNumbers(n1,n2,'bar'):
					return False
			if isLoja:
				if not self.isSameNumbers(n1,n2,'loja'):
					return False
		
		
			if 'is_parent' in data1 and 'is_parent' in data2:
				if data1['is_parent'] != data2['is_parent']:
					return False
			
			if 'ent_type' in data1 and 'ent_type' in data2:
				if data1['ent_type'] != data2['ent_type']:
					return False
			return True
		
		return False




	# returns true if similar
	# data: {nif=not null, lat=not null, lon=not null, is_parent=null, ent_type=null}
	# if any of is_parent or ent_type are  mising from 1 ent, then different
	def isDup_1(self, data1, data2, max_radius = 50):
		if 'nif' not in data1 or 'nif' not in data2:
			raise RuntimeError('Error: missing nif(s)!')
		#if 'is_parent' not in data1 or 'is_parent' not in data2:
		#	raise RuntimeError('Error: missing is_parent(s)!')
		if 'lat' not in data1 or 'lat' not in data2:
			raise RuntimeError('Error: missing latitude(s)!')
		if 'lon' not in data1 or 'lon' not in data2:
			raise RuntimeError('Error: missing longitude(s)!')
		
		
		
		if 'nif' in data1 and 'nif' not in data2:
			return False
		if 'nif' not in data1 and 'nif' in data2:
			return False	
		
		if 'is_parent' in data1 and 'is_parent' not in data2:
			return False
		if 'is_parent' not in data1 and 'is_parent' in data2:
			return False
			
		if 'ent_type' in data1 and 'ent_type' not in data2:
			return False
		if 'ent_type' not in data1 and 'ent_type' in data2:
			return False	
				
		
		# if nifs <> and not false => False
		if 'nif' in data1 and 'nif' in data2:
			if data1['nif'] != data2['nif']:
				return False
		
		
		
		coords_1 = (data1['lat'],data1['lon'])
		coords_2 = (data2['lat'],data2['lon'])
		if geopy.distance.distance(coords_1, coords_2).meters < max_radius:
			if 'is_parent' in data1 and 'is_parent' in data2:
				if data1['is_parent'] != data2['is_parent']:
					return False
			if 'ent_type' in data1 and 'ent_type' in data2:
				if data1['ent_type'] != data2['ent_type']:
					return False
						
			return True
			
		return False


	# returns true if similar
	# data: {name=not null, address=not null, nif=null, is_parent=null, ent_type=null}
	# if any of nif or is_parent or ent_type are mising from 1 ent, then different
	def isDup_2(self, data1, data2, min_ratio = 90):
		if 'name' not in data1 or 'name' not in data2:
			raise RuntimeError('Error: missing name(s)!')
		if 'address' not in data1 or 'address' not in data2:
			raise RuntimeError('Error: missing address(s)!')
				
		
		
		if 'nif' in data1 and 'nif' not in data2:
			return False
		if 'nif' not in data1 and 'nif' in data2:
			return False	
			
		if 'is_parent' in data1 and 'is_parent' not in data2:
			return False
		if 'is_parent' not in data1 and 'is_parent' in data2:
			return False
			
		if 'ent_type' in data1 and 'ent_type' not in data2:
			return False
		if 'ent_type' not in data1 and 'ent_type' in data2:
			return False					

		# if nifs <> and not false => False
		if 'nif' in data1 and 'nif' in data2:
			if data1['nif'] != data2['nif']:
				return False
		
		
		
		isBar = False
		isLoja = False
		n1 = self.sanitizeNome(data1['name'], True)
		n2 = self.sanitizeNome(data2['name'], True)
		m1 = self.sanitizeMorada(data1['address'], True)
		m2 = self.sanitizeMorada(data2['address'], True)
		
		if ' bar ' in self.sanitizeNome(data1['name']):
			isBar = True
		if ' loja ' in self.sanitizeNome(data2['name']):
			isLoja = True
		
		
		if self.getPhoneticsRatioNome(n1,n2) > min_ratio and self.getPhoneticsRatioNome(m1,m2) > min_ratio:
			if isBar:
				if not self.isSameNumbers(n1,n2,'bar'):
					return False
			if isLoja:
				if not self.isSameNumbers(n1,n2,'loja'):
					return False
		
		
			if 'is_parent' in data1 and 'is_parent' in data2:
				if data1['is_parent'] != data2['is_parent']:
					return False
			
			if 'ent_type' in data1 and 'ent_type' in data2:
				if data1['ent_type'] != data2['ent_type']:
					return False
			
			return True
			
		return False


	# returns true if similar
	# data: {name=not null, address=not null, nif=null, is_parent=null, ent_type=null}
	# if any of nif or is_parent or ent_type are mising from 1 ent, then different
	def isDup_3(self, data1, data2, min_size = 4):
		if 'name' not in data1 or 'name' not in data2:
			raise RuntimeError('Error: missing name(s)!')
		if 'address' not in data1 or 'address' not in data2:
			raise RuntimeError('Error: missing address(s)!')
		
		
		if 'nif' in data1 and 'nif' not in data2:
			return False
		if 'nif' not in data1 and 'nif' in data2:
			return False	
			
		if 'is_parent' in data1 and 'is_parent' not in data2:
			return False
		if 'is_parent' not in data1 and 'is_parent' in data2:
			return False
			
		if 'ent_type' in data1 and 'ent_type' not in data2:
			return False
		if 'ent_type' not in data1 and 'ent_type' in data2:
			return False					

		# if nifs <> and not false => False
		if 'nif' in data1 and 'nif' in data2:
			if data1['nif'] != data2['nif']:
				return False
				
		n1 = self.sanitizeNome(data1['name'])
		n2 = self.sanitizeNome(data2['name'])
		m1 = self.sanitizeMorada(data1['address'])
		m2 = self.sanitizeMorada(data2['address'])
		
		#print (n1," # ", n2)
		#print (m1," # ", m2)

		if self.isNameIn(n1,n2,4) and self.isAddressIn(m1,m2,4):
		
			if 'is_parent' in data1 and 'is_parent' in data2:
				if data1['is_parent'] != data2['is_parent']:
					return False
			
			if 'ent_type' in data1 and 'ent_type' in data2:
				if data1['ent_type'] != data2['ent_type']:
					return False
			
			
			return True
			
		return False



	##################
	# MAIN DUP FUNC  #
	##################
	
		
	def isDup(self, data1, data2, min_ratio = 90, max_radius = 50, min_size = 4, ignore=[], order = [0,1,2,3]):
		
		for algo in order:
		
			if algo == 0 and 0 not in ignore:
				try:
					if self.isDup_0(data1, data2, min_ratio):
						return {"DUPLICATED":1,"ALGO":0}
				except Exception as e:
					pass
			if algo == 1 and 1 not in ignore:
				try:
					if self.isDup_1(data1, data2, max_radius):
						return {"DUPLICATED":1,"ALGO":1}
				except Exception as e:
					pass
			
			if algo == 2 and 2 not in ignore:
				try:
					if self.isDup_2(data1, data2, min_ratio):
						return {"DUPLICATED":1,"ALGO":2}
				except Exception as e:
					pass
			
			if algo == 3 and 3 not in ignore:
				try:
					if self.isDup_3(data1, data2, min_size):
						return {"DUPLICATED":1,"ALGO":3}			
				except Exception as e:
					pass
				
				return {"DUPLICATED":0}





