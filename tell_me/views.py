from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

import get_wolfram_data
import json

# Create your views here.
def tell_me_page(request):
	return render(request, 'tell_me/fandeavor_front_end.html', {})

def run_search(request):
	search_name = request.POST.get('search_value')
	response_data = get_wolfram_data.get_data_dict(search_name)

	if response_data['Success'] == 'true':
		return HttpResponse(
			json.dumps(response_data),
			content_type="application/json")
	else: 
		return HttpResponse(
		json.dumps({'search not found': 'Search value not found'}),
		content_type="application/json"
	)


