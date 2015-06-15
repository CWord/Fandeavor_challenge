import urllib
import urllib2
import xmltodict
import parse_xml

appid = 'L5W6HA-8PPL28JEAR'
base_url = 'http://api.wolframalpha.com/v2/query?'
headers = {'User-Agent':None}

def get_xml(ip):
	url_params = {'input':ip, 'appid':appid}
	data = urllib.urlencode(url_params)
	req = urllib2.Request(base_url, data, headers)
	xml = urllib2.urlopen(req).read()
	return xml

def get_data_dict(query):

	xml = get_xml(query)

	data_dict = parse_xml.get_data_dict(xml)
	if data_dict['Success'] == 'false' and data_dict['Did you mean'] != 'No matches':
		xml = get_xml(data_dict['Did you mean'])
		data_dict = parse_xml.get_data_dict(xml)
	return data_dict