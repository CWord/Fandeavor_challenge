import xmltodict

# with open('xml_data.xml') as fd:
#     doc = xmltodict.parse(fd)
#   - Display the image of the person
# 	- Some notable facts(2-3)
# 	- Full name
# 	- Date of birth
# 	- Place of birth
# 	- Date of death
# 	- Place of death

#LOOK AT DATATYPE TO ONLY SHOW PERSON RESULTS

#def get_data_dict(doc):
def get_data_dict(xml):
	doc = xmltodict.parse(xml)
	success = doc['queryresult']['@success']
	if success == 'true':
		pods = doc['queryresult']['pod']
		pod_map = {}
		for index in range(len(pods)):
			title = pods[index]['@title']
			pod_map[str(title)] = index
		#print pod_map.keys()
		notable_facts = pods[pod_map['Notable facts']]['subpod']['plaintext']
		basic_information = pods[pod_map['Basic information']]['subpod']['plaintext']
		image_src = str(pods[pod_map['Image']]['subpod']['img']['@src'])
		#input_interpretation = str(pods[pod_map['Input interpretation']]['subpod']['plaintext'])
		#print input_interpretation

		temp = ""
		notable_facts_list = []
		for char in str(notable_facts):
			if char == '\n':
				notable_facts_list.append(temp)
				temp = ""
			else:
				temp += char

		notable_facts_list = notable_facts_list[:3]

		if temp != '...':
			notable_facts_list.append(temp)
		temp_list = []
		for item in notable_facts_list:
			if len(temp_list) <= 3:
				temp_list.append(item)
		notable_facts_list = temp_list
		basic_info_dict = {}
		index = 0
		temp = ""
		temp_key = ""
		temp_value = ""
		#print basic_information
		for char in basic_information:
			if char == '|':
				temp_key = temp[:-1]
				temp = ""
			if char == '\n' and basic_information[index + 1] != ' ':
				temp_value = temp[2:]
				temp = ""
				basic_info_dict[str(temp_key)] = str(temp_value)
				temp_key = ""
				temp_value = ""
			else:
				temp += char
			index += 1
		basic_info_dict[str(temp_key)] = str(temp[2:])
		#print basic_info_dict

		data_dict = {'Success': success, 'Notable facts': notable_facts_list, 'Image source': image_src}
		for key, value in basic_info_dict.items():
			data_dict[key] = value
		# for key, value in data_dict.items():
		# 	print key +':', value
	elif success == 'false' and 'didyoumeans' in doc['queryresult'].keys():
		did_you_mean = doc['queryresult']['didyoumeans']['didyoumean']['#text']
		data_dict = {'Success': success, 'Did you mean': did_you_mean}
	else:
		data_dict = {'Success': success, 'Did you mean': 'No matches'}
	return data_dict
#get_data_dict(doc)