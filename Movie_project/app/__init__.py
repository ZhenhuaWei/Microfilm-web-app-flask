# coding:utf8
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
import pymysql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:password@127.0.0.1:3306/movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = 'a99df3b52dca4f3e85f90da2ae86b446'
app.debug = True
db = SQLAlchemy(app)

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")#访问后台的时候需要加上/admin


@app.errorhandler(404)
def pge_not_find(error):
    return render_template("home/404.html"), 404
