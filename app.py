from flask import Flask, jsonify
from models import books
from flask import abort
from flask import make_response
from flask import request


app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('marta_config.cfg', silent=True)


@app.route("/api/v1/books/", methods=["GET"])
def books_list_api_v1():
    return jsonify(books.all())


@app.route("/api/v1/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = books.get(book_id)
    if book is None:
        abort(404)
    return jsonify({"book": book})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)


@app.route("/api/v1/books/", methods=["POST"])
def create_book():
    if not request.json or not 'title' in request.json:
        abort(400)
    book = {
        'id': books.all()[-1]['id'] + 1,
        'title': request.json['title'],
        'author': request.json.get('author'),
        'description': request.json.get('description', ""),
        'number_of_pages': request.json.get('numebr_of_pages'),
        'done': False
    }
    books.create(book)
    return jsonify({'book': book}), 201

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)

@app.route("/api/v1/books/<int:book_id>", methods=['DELETE'])
def delete_book(book_id):
    result = books.delete(book_id)
    if not result:
        abort(404)
    return jsonify({'result': result})

@app.route("/api/v1/books/<int:book_id>", methods=["PUT"])
def update_books(book_id):
    book = books.get(book_id)
    if book is None:
        abort(404)
    if request.json is None:
        abort(400)
    data = request.json
    if any([
        'title' in data and not isinstance(data.get('title'), str),
        'author' in data and not isinstance(data.get('author'), str),
        'description' in data and not isinstance(data.get('description'), str),
        'done' in data and not isinstance(data.get('done'), bool),
        'number_of_pages' in data and not isinstance(data.get('number_of_pages'), int),

    ]):
        abort(400)
    
    books.update(book_id, book)
    return jsonify({'book': book})


if __name__ == "__main__":
    app.run(debug=True)