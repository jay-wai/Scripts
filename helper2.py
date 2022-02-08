loc_json = {	
	"no_of_dropdown": 4,
	"dropdown_list": [
		{
		  "label": {
			"en": "Select State",
			# "hi": "",
			# "gu": ""
			},
		  "dropdown_list": [
			
			{
			  "label": {
				"en": "Select Cluster",
				# "hi": "",
				# "gu": ""
			  },
			  "dropdown_list": [
				{
					"label": {
						"en": "Select Village",
						# "hi": "",
						# "gu": ""
					},
					"dropdown_list": [
						{	
							"label": {
								"en": "Select Site Type",
								# "hi": "",
								# "gu": ""
							},
							"dropdown_list": [
							]
						}
					]
				}
			  ]	
			}
			
			#Addtion of more dropdowns starts from here in this drop down list second element----------------------
		]
	}
	],
	"dropdown_info_list": [
		{
		  "tag": "state",
		  "label": {
			"en": "State",
			# "hi": "",
			# "gu": ""
		  }
		},
		{
		  "tag": "cluster",
		  "label": {
			"en": "Cluster",
			# "hi": "",
			# "gu": ""
		  }
		},

		{
		  "tag": "site_name",
		  "label": {
			"en": "Village Name",
			# "hi": "",
			# "gu": ""
		  }
		},

		{
		  "tag": "site_type",
		  "label": {
			"en": "Site Type",
			# "hi": "",
			# "gu": ""
		  }
		}
	]
}

state_list = [
							   {
								  "label": {
									"en": "Select Cluster",
									# "hi": "",
									# "gu": ""
								  },
								  "dropdown_list": [
									  {
									  "label": {
										"en": "Select Village",
										# "hi": "",
										# "gu": ""
									  },
									  "dropdown_list": [
									  	{
										  "label": {
											"en": "Select Site Type",
											# "hi": "",
											# "gu": ""
										  },
										  "dropdown_list": []
										}
									  ]
									}
								  ]
								}
							   ]
							   
cluster_list = [
									  {
									  "label": {
										"en": "Select Village",
										# "hi": "",
										# "gu": ""
									  },
									  "dropdown_list": [
									  	{
										  "label": {
											"en": "Select Site Type",
											# "hi": "",
											# "gu": ""
										  },
										  "dropdown_list": []
										}
									  ]
									}
								  ]