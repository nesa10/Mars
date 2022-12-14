
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
client = MongoClient('mongodb+srv://nesa:nesasaputri@cluster0.7le98k4.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/mars", methods=["POST"])
def web_mars_post():
    name_receive = request.form['name_give']
    addres_receive = request.form['addres_give']
    size_addres_receive = request.form['size_give']
    doc = {
       'nama'  :name_receive,
       'addres' : addres_receive,
       'size'  : size_addres_receive }
        
     

    db.orders.insert_one(doc)
    return jsonify({'msg': 'lengkap!'})

@app.route("/mars", methods=["GET"])
def web_mars_get():
    orders_list = list(db.orders.find ({}, {'_id': False}))
    return jsonify({'orders': orders_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)