from cantools import db

class Short(db.TimeStampedBase):
	url = db.String()
	code = db.String()