# Instruction:
# Also download 0-10-7_rebal_mult_model for guessing the multiplier value
# Put a data folder with ship in the same directory as this file
# Output will be in "output" folder with "000 BAL-10-7" prefix

# What it does:
# Adjust mass, heat dissipation, and drag the same way it was done in 0.10.7 (https://docs.google.com/spreadsheets/d/1F-dPCeTjWYQfA64flG2qzKdfec9z0_YrIqBGbSOxmwI/edit?gid=1373529923#gid=1373529923)
# Also add scrambling protection and resistance to ship with ion protection/resistance



import os
no_sk = False
try:
	from sklearn.ensemble import RandomForestRegressor
except ModuleNotFoundError:
	from balance_table0107 import mult_table
	no_sk = True
import pickle

if not no_sk:
	mult_predictor: RandomForestRegressor = pickle.load(open("0-10-7_rebal_mult_model", 'rb'))

e = 2.71828

def get_multiplier(x):
	if (no_sk):
		try:
			return mult_table[x[0][0]]
		except KeyError:
			return mult_table[len(mult_table) - 1]
	return mult_predictor.predict(x)[0]

outfitlist = []
outfitout = []

engine_attrs = [
	"thrust",
	"turn",
	"reverse thrust",
	"afterburner thrust"
]

def parse_folder_outfit(f):
	for datafile in f[2]:
		if datafile.endswith(".txt"):
			dataread = open(f[0]+"/"+datafile, 'r')
			alllines = dataread.readlines()
			outfitfound = False
			outfitexist = False
			outfitout = []
			for line in alllines:
				if line.startswith("outfit "):
					outfitout.append("\n")
					outfitfound = True 
					outfitexist = True
					outfitout.append(line)
				elif line.startswith("\t") and outfitfound:
					attrs = line.split()
					if (len(attrs) == 0):
						outfitout.append(line)
						continue
					attr = attrs[0]
					for i in range(len(attrs) - 2 - 1):
						attr += " " + attrs[i + 1]
					attr = attr.strip().removeprefix('"').removesuffix('"')
					if line.startswith('\t\t'):
						pass
					elif attr in engine_attrs:
						val = line.split()[-1]
						new_val = float(val) * 2
						#print(f'{line} :: flotsam={droprate}\n')
						outfitout.append(f'\t"{attr}" {new_val:.3f}\n')
					else:
						outfitout.append(line)
				elif not line.startswith("outfit "):
					outfitfound = False
			if outfitexist:
				fileout = open(f'output/000 OBAL-10-7 {datafile}', 'w')
				fileout.writelines(outfitout)
				fileout.close()

def compute_ship(ship_data: dict, ship_dat_tmp: list):
	multiplier = 0
	if 'mass' in ship_data.keys():
		ship_mass  = float(ship_data['mass'])
		ship_ospace = float(ship_data['outfit space'])
		multiplier = get_multiplier([[ship_mass + ship_ospace]])
		ship_data['mass'] = multiplier * (ship_mass + ship_ospace) - ship_ospace
		if 'drag' in ship_data.keys():
			ship_mass  = float(ship_data['mass'])
			ship_ospace = float(ship_data['outfit space'])
			ship_drag = float(ship_data['drag'])
			if multiplier == 0:
				multiplier = get_multiplier([[ship_mass + ship_ospace]])
			ship_data['drag'] = multiplier * ship_drag
		if 'heat dissipation' in ship_data.keys():
			ship_mass  = float(ship_data['mass'])
			ship_ospace = float(ship_data['outfit space'])
			ship_diss = float(ship_data['heat dissipation'])
			if multiplier == 0:
				multiplier = get_multiplier([[ship_mass + ship_ospace]])
			ship_data['heat dissipation'] = ship_diss / multiplier
	shipout = []
	for line in ship_dat_tmp:
		if line.startswith('\t\t"mass"') or line.startswith('\t\tmass') and 'mass' in ship_data.keys():
			smass = ship_data['mass']
			line = f'\t\t"mass" {smass:.3f}\n'
		elif line.startswith('\t\t"drag"') or line.startswith('\t\tdrag') and 'drag' in ship_data.keys():
			smass = ship_data['drag']
			line = f'\t\t"drag" {smass:.3f}\n'
		elif line.startswith('\t\t"heat dissipation"') or line.startswith('\t\theat dissipation') and 'heat dissipation' in ship_data.keys():
			smass = ship_data['heat dissipation']
			line = f'\t\t"heat dissipation" {smass:.3f}\n'
		shipout.append(line)
	# for key in ship_data.keys():
	# 	# line = '"' + key + '" ' + ship_data[key]
	# 	if type(ship_data[key]) is str and " " in ship_data[key]:
	# 		line = f'"{key}" "{ship_data[key]}"'
	# 	else:
	# 		line = f'"{key}" {ship_data[key]}'
	# 	shipout.append(line)
	return shipout

def parse_folder_ship(f):
	for datafile in f[2]:
		if datafile.endswith(".txt"):
			dataread = open(f[0]+"/"+datafile, 'r')
			alllines = dataread.readlines()
			shipfound = False
			shipexist = False
			ship_data = {}
			ship_dict = {}
			ship_list = []
			ship_dat_tmp = []
			shipout = []
			for line in alllines:
				stripped_line = line.strip()
				# if stripped_line.startswith('#'):
				# 	pass
				if line.startswith("ship ") and not line.startswith('ship "Timer') :
					shipfound = True 
					shipexist = True
					ship_id = line.split()
					ship_id: str = ship_id[1].removeprefix('"').removesuffix('"')
					if (len(ship_data.keys()) > 0):
						# multiplier = mult_predictor.predict([ship_data['mass'] + ship_data['outfit space']])[0]
						# ship_data['mass'] = multiplier * (ship_data['mass'] + ship_data['outfit space']) - ship_data['outfit space']
						if ('mass' not in ship_data.keys()):
							# print("db")
							pass
						shipout.extend(compute_ship(ship_data, ship_dat_tmp))
					del ship_data
					ship_dat_tmp.clear()
					ship_data = {}
					ship_data["ship"] = f'{ship_id}'
					ship_dict[f'{ship_id}'] = ship_data
					ship_dat_tmp.append(line)
					# ship_list.append(ship_dict)
					# shipout.append("\n")
					# shipout.append(line)
				elif line.startswith('\t\tcategory'):
					shipcat = line.split()
					shipcat = shipcat[1].removeprefix('"').removesuffix('"')
					ship_data['category'] = shipcat
					ship_dat_tmp.append(line)
				elif line.startswith('\t\t"outfit space"'):
					outfit_space = line.split()
					outfit_space = float(outfit_space[2])
					ship_data['outfit space'] = outfit_space
					ship_dat_tmp.append(line)
				elif line.startswith('\t\t"mass"') or line.startswith('\t\tmass') and shipfound:
					massdata = line.split()
					shipmass = float(massdata[1])
					ship_data['mass'] = shipmass
					# eq = int(max(1,.05/(.01+(pow(e,-0.01*shipmass)/1))))
					# finmass = (shipmass * eq)
					# shipout.append(f'\t\t"mass" {finmass:.2f}\n')
					ship_dat_tmp.append(line)
				elif line.startswith('\t\t"drag"') or line.startswith('\t\tdrag') and shipfound:
					massdata = line.split()
					shipdrag = float(massdata[1])
					ship_data['drag'] = shipdrag
					ship_dat_tmp.append(line)
				elif line.startswith('\t\t"heat dissipation"') and shipfound:
					massdata = line.split()
					shipdiss = float(massdata[2])
					ship_data['heat dissipation'] = shipdiss
					ship_dat_tmp.append(line)
				elif line.startswith('\t\t"ion protection"') and shipfound:
					massdata = line.split()
					ship_ion = float(massdata[2])
					ship_data['ion protection'] = ship_ion
					ship_dat_tmp.append(line)
					ship_data['scrambling protection'] = ship_ion
					add_line = f'\t\t"scrambling protection" {ship_ion}\n'
					ship_dat_tmp.append(add_line)
				elif line.startswith('\t\t"ion resistance"') and shipfound:
					massdata = line.split()
					ship_ion = float(massdata[2])
					ship_data['ion resistance'] = ship_ion
					ship_dat_tmp.append(line)
					ship_data['scrambling resistance'] = ship_ion
					add_line = f'\t\t"scrambling resistance" {ship_ion}\n'
					ship_dat_tmp.append(add_line)
				elif line.startswith('\t') and shipfound:
					#BROKEN, DOESNT WORK
					tab_lv = line.removesuffix('\t').removesuffix('\t').removesuffix('\t').count('\t')
					attr = line.strip()
					# while attr.startswith('\t') :
					# 	attr = attr.removeprefix('\t')
					idx =  attr.find('"', 1)
					attr_val = attr[idx + 1:].removesuffix('"')
					attr_name = attr[:idx]
					attr_val = attr_val.strip()
					attr_name = attr_name.strip().removeprefix('"').removesuffix('"').strip()
					ship_data[attr_name] = attr_val
					ship_dat_tmp.append(line)
					# shipout.append(line)
				elif line.startswith('\t') and len(line.split()) > 1:
					#still in ship.
					pass
				else :
					ship_dat_tmp.append(line)
				# elif not line.startswith("ship "):
				# 	shipfound = False
			if shipfound:
				shipout.extend(compute_ship(ship_data, ship_dat_tmp))
			if shipexist:
				fileout = open(f'output/000 BAL-10-7 {datafile}', 'w')
				fileout.writelines(shipout)
				fileout.close()

if True:
	filelist = os.walk("./")
	for f in filelist:
		#print("File list: ",f)
		#print("things",f[1])
		if f[0].startswith('./data'):
			print("Found data folder: ", f)
			parse_folder_ship(f)
			parse_folder_outfit(f)

