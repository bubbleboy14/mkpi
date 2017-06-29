"""
The Geo (/geo) APIs are as follows:

### action = zip

requires: "code"

    - /geo?action=zip&code=94624

returns: [city, state, county]

    - ["Oakland", "CA", "Alameda"]

### action = ip

requires: "ip"

    - /geo?action=ip&ip=74.125.45.100

returns: location data

    - {"latitude": "36.153999", "location": "US, OK, Oklahoma, Tulsa, 74102", "longitude": "-95.992798"}

#### setup

The IP API uses the geoiplookup tool, which can be acquired
on Debian-based systems with the following command:

	sudo apt install geoip-bin

That's it!
"""

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