from django.shortcuts import render

def lookup(request):
	import json
	import requests

	if request.method == "POST":

		zipcode = request.POST['zipcode']

		try:
			api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=1&API_KEY=18DD9D0B-3362-4B81-9A6B-A9480A04875D")
			api = json.loads(api_request.content)
			return render(request, 'lookup.html', {'api': api})

		except Exception as e:
			api = "Error"
			return render(request, 'lookup.html', {})
	else:

		try:
			api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=1&API_KEY=18DD9D0B-3362-4B81-9A6B-A9480A04875D")
			api = json.loads(api_request.content)
			return render(request, 'lookup.html', {'api': api})

		except Exception as e:
			api = "Error"
			return render(request, 'lookup.html', {})
