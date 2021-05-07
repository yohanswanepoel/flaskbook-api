from flask import Flask, jsonify, request
from flask_cors import CORS

# Configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable flask_cors
CORS(app)

@app.route('/')
def homepage():
    return """<h1>Books API Landing page try <a href="/books">/books</a></h1>"""

# Health check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong')

BOOKS = [
    {
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    },
    {
        'title': 'Never say Die',
        'author': 'Ian Flemming',
        'read': True
    },
    {
        'title': 'Jock of the Bushveld',
        'author': 'James Percy FitzPatrick',
        'author': 'Author Unknown',
        'read': True
    }
]



@app.route('/books', methods=['GET','POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)

if __name__ == '__main__':
    print("INFO: Starting the app")
    app.run(host='0.0.0.0',port=8080)
