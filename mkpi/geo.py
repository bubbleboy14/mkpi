from cantools.web import respond, succeed, fail, cgi_get
from cantools.util import output

def response():
	action = cgi_get("action", choices=["zip", "ip"])
	if action == "zip":
		import zipcodes
		succeed(zipcodes.codes.get(cgi_get("code"), ["unknown", "unknown", "unknown"]))
	elif action == "ip":
		parts = output("geoiplookup %s -f GeoLiteCity.dat"%(cgi_get("ip"),)).split(": ")[1].split(", ")
		succeed({
			"location": ", ".join(parts[0:5]),
			"latitude": parts[5],
			"longitude": parts[6]
		})
	else:
		fail("no such action: %s"%(action,))

respond(response)