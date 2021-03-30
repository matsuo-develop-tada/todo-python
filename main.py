from flask import Flask, jsonify

app = Flask(__name__)

todos = [
    {'id': 1, 'content': 'todo1'},
    {'id': 2, 'content': 'todo2'},
    {'id': 3, 'content': 'todo3'},
]

@app.route('/todos')
def get_todos():
    return jsonify(todos)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
