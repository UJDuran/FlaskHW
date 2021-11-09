from myapp import myapp_obj
from flask import render_template, redirect, flash
from myapp.forms import TopCities

from myapp import db
from myapp.models import User

@myapp_obj.route("/",   methods = ['GET', 'POST'])
def home():
    form = TopCities()
    name = 'Ulises'
    title = 'Welcome ' + name
    return render_template("base.html",form = form, title = title)

@myapp_obj.route("/")
def list():
    theList = db.create_all()
    theCity = User(city_name=form.city_name.data)
    theRank = User(city_rank=form.city_rank.data)
    db.session.add(theCity, theRank)
    db.session.commit()
    theList = db.query_all()
    return render_template("home.html", theList = theList)
