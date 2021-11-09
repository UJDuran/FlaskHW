from myapp import db

class User(db.Model):
    name = db.Column(db.String(64), index = True, unique = True)
    rank = db.Column(db.Integer, primary_key = True)
