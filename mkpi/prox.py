"""
Prox (/prox) API:

### action = pass (default)

requires: "url"

    - /prox?url=https%3A//google.com/

returns: requested resource
"""

import requests, urllib
from datetime import datetime, timedelta
from cantools.web import respond, succeed, cgi_get
from cantools.util import log
from cantools import config

CACHE = {}
STAMP = {}
limit = timedelta(seconds=int(config.prox.timeout))

def check(url):
	if url not in CACHE:
		return False
	elapsed = datetime.now() - STAMP[url]
	log("elapsed: %s"%(elapsed,), 1)
	return elapsed < limit

def cache(url):
	log("checking cache for: %s"%(url,))
	if not check(url):
		log("acquiring", 1)
		CACHE[url] = requests.get(url).content
		STAMP[url] = datetime.now()
	return CACHE[url]

def response():
	succeed(cache(urllib.unquote(cgi_get("url"))))

respond(response)