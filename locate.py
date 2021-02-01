# get location(lat, long) using public ip  and open google maps search using cordinates.


import pygeoip          # pip install pygeoip

gip = pygeoip.GeoIP("GeoLiteCity.dat")
res = gip.record_by_addr('127.0.0.1')   # pass here private / public ip - get lat,long.
print(res)
for key, val in res.items():
    print('%s : %s' % (key, val))
