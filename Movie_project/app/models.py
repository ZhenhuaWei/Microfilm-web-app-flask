# coding:utf8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:passowrd@127.0.0.1:3306/movie"
app.config["SQLALCHEMY_TRACK_MODIFCATIONS"] = True

db = SQLAlchemy(app)


# 会员数据模型
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 昵称
    pwd = db.Column(db.String(100))  # 密码
    email = db.Column(db.String(100), unique=True)  # 邮箱
    phone = db.Column(db.String(11), unique=True)  # 手机号码
    info = db.Column(db.Text)  # 个性简介
    face = db.Column(db.String(255), unique=True)  # 头像
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 注册时间
    uuid = db.Column(db.String(255), unique=True)  # 唯一标识符
    userlogs = db.relationship("Userlog", backref='user')  # 会员日志外健关联
    comments = db.relationship("Comment", backref='user')  # 评论外健关联
    moviecols = db.relationship("Moviecol", backref='user')  # 收藏电影外健关联

    def __repr_(self):
        return "<User %r>" % self.name


# 会员登录日志
class Userlog(db.Model):
    __tablename__ = "Userlog"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属会员
    ip = db.Column(db.String(100))  # 登录
    addtime = db.Column(db.DateTime, index=True, default=datetime.uctnow)  # 登录时间

    def __repr__(self):
        return "<Userlog %r>" % self.id


# 标签
class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 标题
    addtime = db.Column(db.DateTime, index=True, default=datetime.uctnow)  # 添加时间
    movies = db.relationship("Movie", backref='tag')  # 电影外健关系关联

    def __repr__(self):
        return "<Tag %r>" % self.name


# 电影
class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    title = db.Column(db.String(255), unique=True)  # 标题
    url = db.Column(db.String(255), unique=True)  # 地址
    info = db.Column(db.Text)  # 简介
    logo = db.Column(db.String(255), unique=True)  # 封面
    star = db.Column(db.SmallInteger)  # 星际
    playnum = db.Column(db.BigInteger)  # 播放量
    commentnum = db.Column(db.BigInteger)  # 评论数
    tag_id = db.Colum(db.Integer, db.ForeignKey("tag.id"))  # 所属标签
    area = db.Column(db.String(255))  # 上映地区
    release_time = db.Column(db.Date)  # 上映时间
    length = db.Column(db.String(100))  # 播放时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.uctnow)  # 添加时间
    comments = db.relationship("Comment", backref='movie')  # 评论外健关联
    moviecols = db.relationship("Moviecol", backref='movie')  # 评论外健关联

    def __repr__(self):
        return "<Movie %r>" % self.title


# 上映预告
class Preview(db.Model):
    __tablename__ = "preview"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    title = db.Column(db.String(255), unique=True)  # 标题
    logo = db.Column(db.String(255), unique=True)  # 封面
    addtime = db.Column(db.DateTime, index=True, default=datetime.uctnow)  # 添加时间

    def __repr__(self):
        return "<Preview %r>" % self.title

class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True) #编号
    content = db.Column(db.Text)   #内容
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))#所属电影
    user_id = db.Column(db.Integer, db,ForeignKey("user.id"))#所属用户
    addtime = db.Column(db.DateTime, index=True, default=datetime.uctnow)  # 添加时间

    def __repr__(self):
        return "<Comment %r>" % self.id

#电影收藏
class Moviecol(db.Model):
    __tablename__ = "moiecol"
    id = db.Column(db.Integer, primary_key=True) #编号
    content = db.Column(db.Text)   #内容
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))#所属电影
    user_id = db.Column(db.Integer, db,ForeignKey("user.id"))#所属用户
    addtime = db.Column(db.DateTime, index=True, default=datetime.uctnow)  # 添加时间

    def __repr__(self):
        return "<Moviecol %r>" % self.id
