import json
import copy
import pandas as pd
from helper2 import loc_json,state_list,cluster_list


anthro_map = {}

df = pd.read_excel('sewa2.xlsx')
print(df)

for index, row in df.iterrows():
	state = row['State']
	cluster = row['Cluster Name']
	site = row['Site Name']

	if state not in anthro_map:
		anthro_map[state] = {}

	if cluster not in anthro_map[state]:
		anthro_map[state][cluster] = []

	anthro_map[state][cluster].append(site)

print(anthro_map.keys())

for state in anthro_map:
	state_dl = copy.deepcopy(state_list)
	for cluster in anthro_map[state]:
		cluster_dl = copy.deepcopy(cluster_list)
		for site in anthro_map[state][cluster]:
			cluster_dl.append({
				"label": {
					"en": site
				},
				"dropdown_list":[
					{
					  "label": {
						"en": "Select Site Type"
					  },
					  "dropdown_list": []
					},
					{
					  "label": {
						"en": "Home"
					  },
					  "dropdown_list": []
					}
				]
			})
		state_dl.append({
			"label": {
					"en": cluster			
			},
			"dropdown_list": cluster_dl
		})
	
	loc_json["dropdown_list"].append({
		"label": {
				"en": state
		},
		"dropdown_list": state_dl
	})

# print(loc_json)

with open("locdata2.json", "w") as loc_data_file:
    json.dump(loc_json, loc_data_file, indent=4)