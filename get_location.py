# get location(lat, long) using public ip 

import requests

# gives public ip  ,  also use : https://api.ipify.org
ipadd = requests.get('https://get.geojs.io/v1/ip.json')  # gets ip in json , 
ipadd = ipadd.json()['ip']
print('Public Ip: ', ipadd)

url = 'https://get.geojs.io/v1/ip/geo/'+ipadd+'.json'      # get location
geo_request = requests.get(url)
geo_data = geo_request.json()
# print(geo_data)

print('lat : ', geo_data['latitude'])
print('lon : ', geo_data['longitude'])
print('city:', geo_data['city'])
