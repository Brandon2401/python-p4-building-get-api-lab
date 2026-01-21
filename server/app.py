#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False




db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    all_bakeries = Bakery.query.all()
    return jsonify([b.to_dict() for b in all_bakeries]) , 200

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bakery = Bakery.query.filter(Bakery.id == id).first()
    return jsonify(bakery.to_dict()) , 200

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    baked_goods = (
        BakedGood.query
        .order_by(BakedGood.price.desc())
        .all()
    )
    baked_goods_list = [bg.to_dict() for bg in baked_goods]
    return jsonify ([bg.to_dict() for bg in baked_goods]) , 200
  

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    baked_good = (
        BakedGood.query
        .order_by(BakedGood.price.desc())
        .first()
    )
    return jsonify(baked_good.to_dict()) , 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)
