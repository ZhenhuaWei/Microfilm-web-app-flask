# coding:utf8
from app import app
from flask_script import Manager #命令行的一个模块

manager = Manager(app)
if __name__ == "__main__":
    app.run()
