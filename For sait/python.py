from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import test

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vk_bot-master/Goods.db'
db = SQLAlchemy(app)


class GG(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(200))
    Address = db.Column(db.String())
    Address_log = db.Column(db.String())
    Goods = db.Column(db.String())
    Period = db.Column(db.String())
    Coment = db.Column(db.String())
    Photo = db.Column(db.String())
