standard_values = [5,8.5,300,500,120,300,500,75,30,250,45,150,5]
weights = [0.3723,.2190,0.371,0.0037,.0155,0.0062,.0037,0.025,0.061,0.0074,.0412,0.01236,0.3723]

standards = {
		'ph_val':[8.5,0.2190],
		'dissolved_oxygen':[5,0.3723],		
		'biological_oxygen_demand':[5,0.3723],
		# 'colour':[5,]
		'electrical_conductivity':[300,0.371],
		'total_dissolved_solids':[500,0.0037],
		'total_alkalinity':[120,0.0155],
		'total_hardness':[300,0.0062],
		'total_suspended_solids':[500,0.0037],
		
        
        'magnesium':[30,0.061],
		'calcium':[75,0.025],
		'nitrate':[45,0.0412],
		'chlorides':[250,0.0074],
		'sulphate':[150,0.01236],

		
		

}


# def calcQn(vn,i):
# 	if i >1:
# 		q = (vn)/(standard_values[i])
# 		q = 100 * q
# 		print(q)
# 		return abs(q)

# 	elif i == 0:
# 		q = (vn - 14.6)/(standard_values[i] - 14.6)
# 		q = q * 100
# 		print(q)
# 		return abs(q)/1.4
# 	elif i == 1:
# 		q = (vn - 7)/(standard_values[i] - 7)
# 		q = 100 * q
# 		print(q)
# 		return abs(q)


# def calculateIndex(params):
# 	qn = []

# 	for i in range(0,13):
# 		qn.append(calcQn(params[i],i))
# 	print(qn)
# 	qn[12] = qn[12]/4.21052
# 	wn = 0
# 	for w in weights:
# 		wn = wn + w
# 	numerator = 0
# 	for i in range(0,13):
# 		numerator = numerator + (qn[i] * weights[i])
# 	print(numerator)
# 	index = numerator/wn
# 	print(index)
# 	return index

def calcQn(vn,key):
	if key == 'ph_val':
		q = (vn - 7)/(standards[key][0] - 7)
		q = 100 * q
		return abs(q)
	elif key == 'dissolved_oxygen':
		q = (vn - 14.6)/(standards[key][0] - 14.6)
		q = 100 * q
		return abs(q)
	elif key == 'biological_oxygen_demand':
		q = (vn)/(standards[key][0])
		q = (100 * q)/4.21052
		return abs(q)

	else :
		q = (vn)/(standards[key][0])
		q = 100 * q
		print(q)
		return abs(q)

def calculateIndex(dict_of_params):
	qn = {}
	for key in dict_of_params:
		qn[key] = calcQn(dict_of_params[key],key)
	print(qn)
	wn = 0
	numerator = 0
	for key in dict_of_params:
		wn = wn + standards[key][1]
		
		numerator =numerator +( standards[key][1] * qn[key] )
	
	index = numerator/wn
	print(index)
	return index

