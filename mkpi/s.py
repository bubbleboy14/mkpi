"""
Short (/s) API:

### requires: "u"

    - /u=https://www.google.com

which returns: shortened version of url

### or: "k"

    - /k=aXzHO

which returns: 302 redirect
"""

from cantools.web import respond, succeed, cgi_get, local
from cantools.util import log, token
from model import Short

def response():
	u = cgi_get("u", required=False, decode=True)
	k = cgi_get("k", required=False)
	if u:
		s = Short.query(Short.url == u).get()
		if not s:
			s = Short()
			s.url = u
			s.code = token(5)
			s.put()
		succeed(s.code)
	elif k:
		s = Short.query(Short.code == k[:5]).get()
		s and local("redir")(s.url)

respond(response)