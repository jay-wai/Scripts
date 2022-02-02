import json
import copy
import pandas as pd
from helper import loc_json,state_list,district_list,block_list,phc_list,subc_list

sheetnames = ["Jhagadiya","Valiya","Netrang"]

anthro_map = {}

for s in sheetnames:
	df = pd.read_excel('sewa.xlsx',sheet_name=s)
	print(df)
	
	for index, row in df.iterrows():
		state = row['STATE']
		district = row['DISTRICT']
		block = row['BLOCK']
		phc = row['PHC']
		subc = row['SUB CENTAR']
		village = row['VILLAGE']

		if state not in anthro_map:
			anthro_map[state] = {}

		if district not in anthro_map[state]:
			anthro_map[state][district] = {}

		if block not in anthro_map[state][district]:
			anthro_map[state][district][block] = {}
		
		if phc not in anthro_map[state][district][block]:
			anthro_map[state][district][block][phc] = {}
		
		if subc not in anthro_map[state][district][block][phc]:
			anthro_map[state][district][block][phc][subc] = []

		anthro_map[state][district][block][phc][subc].append(village)

print(anthro_map.keys())

for state in anthro_map:
	state_dl = copy.deepcopy(state_list)
	for district in anthro_map[state]:
		district_dl = copy.deepcopy(district_list)
		for block in anthro_map[state][district]:
			block_dl = copy.deepcopy(block_list)
			for phc in anthro_map[state][district][block]:
				phc_dl = copy.deepcopy(phc_list)
				for subc in anthro_map[state][district][block][phc]:
					subc_dl = copy.deepcopy(subc_list)
					for village in anthro_map[state][district][block][phc][subc]:
						subc_dl.append({
							"label": {
								"en": village,
								"hi": village
							},
							"dropdown_list":[]
						})
					
					phc_dl.append({
						"label": {
								"en": subc,
								"hi": subc
						},
						"dropdown_list": subc_dl
					})

				block_dl.append({
					"label": {
							"en": phc,
							"hi": phc
					},
					"dropdown_list": phc_dl
				})
			district_dl.append({
				"label": {
						"en": block,
						"hi": block
				},
				"dropdown_list": block_dl
			})
		
		state_dl.append({
			"label": {
					"en": district,
					"hi": district
			},
			"dropdown_list": district_dl
		})
	
	loc_json["dropdown_list"].append({
		"label": {
				"en": state,
				"hi": state
		},
		"dropdown_list": state_dl
	})

# print(loc_json)

with open("locdata.json", "w") as loc_data_file:
    json.dump(loc_json, loc_data_file, indent=4)