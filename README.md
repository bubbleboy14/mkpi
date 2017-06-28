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