# mkpi

A set of web APIs.

## geo.py

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

### action = ips

requires: "ips"

    - use a post request, providing a list of ip addresses for processing

returns: location data array

    - [{"latitude": "36.153999", "location": "US, OK, Oklahoma, Tulsa, 74102", "longitude": "-95.992798"},
       {"latitude": "37.236198", "location": "US, CA, California, San Jose, 95123", "longitude": "-121.828903"}]

### setup

The IP APIs use the geoiplookup tool, which can be acquired
on Debian-based systems with the following command:

	sudo apt install geoip-bin

That's it!