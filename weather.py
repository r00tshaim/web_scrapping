import json,requests,sys

if(len(sys.argv)<3):
	print("Usage: weather.py city country")
	sys.exit()

print(sys.argv)
city=''.join(sys.argv[1:2])
country=''.join(sys.argv[2:])

APPID="43637071dd1704cd97bdda7d62fc17ed"
url ='https://api.openweathermap.org/data/2.5/forecast?q=%s,%s&appid=%s' %(city,country,APPID)
response=requests.get(url)

try:
	response.raise_for_status()
except requests.exceptions.HTTPError:
	print("City or Country not found please try again")
	sys.exit(0)
else:
	#print(response.text)

	weatherData=json.loads(response.text)
	#print(weatherData)

	w = weatherData['list']
	print('Current weather in %s:' % (city))
	
	print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description']) 
	print('Tomorrow:') 
	print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description']) 
	print('Day after tomorrow:') 
	print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
