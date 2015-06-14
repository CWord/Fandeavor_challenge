from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

import get_wolfram_data
import json

# Create your views here.
def tell_me_page(request):
	return render(request, 'tell_me/fandeavor_front_end.html', {})
	# data_dict = get_wolfram_data.get_data_dict("Stephen Hawking")
	#template = loader.get_template('tell_me/fandeavor_front_end.html')
	# full_name = data_dict['full name']
	# date_of_birth = data_dict['date of birth']
	# context = RequestContext(request, {'full_name': full_name, 'date_of_birth': date_of_birth})
	# return HttpResponse(template.render(context))
	#return HttpResponse("Button Clicked")
	#return HttpResponse(template.render({}))
def run_search(request):
	search_name = request.POST.get('search_value')
	response_data = get_wolfram_data.get_data_dict(search_name)

	# if data_dict['Success'] = 'true':
	# 	key_list = ['full name', 'Notable facts', 'Image source', 'date of death', 'date of birth', 'place of birth', 'place of death']
	# 	for key, value in data_dict.items():
	# 		if key in key_list:
	# 			response_data['key'] = data_dict['key']

	if response_data['Success'] == 'true':
		return HttpResponse(
			json.dumps(response_data),
			content_type="application/json")
	else: 
		return HttpResponse(
		json.dumps({'search not found': 'Search value not found'}),
		content_type="application/json"
	)


