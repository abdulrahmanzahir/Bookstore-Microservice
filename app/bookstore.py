from flask import Flask, jsonify, render_template
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import os


app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://mongodb:27017/Bookstore")
mongo = PyMongo(app)


@app.route('/')
def home():
    return "Hey, This is my Bookstore!!!"


@app.route('/Books', methods=['GET'])
def get_library():
    all_books = list(database.books.find())
    return jsonify({'library': all_books})


@app.route('/Books', methods=['GET'])
def get_book_details(book_id):
    book = database.books.find_one({'_id': ObjectId(book_id)})
    return jsonify({'book_details': book})


@app.route('/Books', methods=['POST'])
def add_book_to_library():
    new_book_data = request.get_json()
    database.books.insert_one(new_book_data)
    return jsonify({'message': 'Book was added to the bookstore successfully'})


@app.route('/Books', methods=['PUT'])
def update_book_in_library(book_id):
    updated_book_data = request.get_json()
    database.books.update_one({'_id': ObjectId(book_id)}, {'$set': updated_book_data})
    return jsonify({'message': 'Book details was updated successfully'})


@app.route('/Books', methods=['DELETE'])
def remove_book_from_library(book_id):
    database.books.delete_one({'_id': ObjectId(book_id)})
    return jsonify({'message': 'Book was removed from the bookstore successfully'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
