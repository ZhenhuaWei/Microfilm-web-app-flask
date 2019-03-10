# coding:utf8

from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")#访问后台的时候需要加上/admin


@app.errorhandler(404)
def pge_not_find(error):
    return render_template("home/404.html"), 404
