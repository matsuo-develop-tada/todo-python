from flask import jsonify
from settings import app, Todo, Color


@app.route('/todos', methods=['GET'])
def get_todos():
    # Todo一覧を取得
    todos = Todo.query.all()

    # Todo一覧を取得した後に、class→dict→jsonの順に変換して返す
    dict_todos = []
    for todo in todos:
        dict_todos.append(todo.to_dict())

    return jsonify(dict_todos)


@app.route('/colors', methods=['GET'])
def get_colors():
    colors = Color.query.all()

    dict_colors = []
    for color in colors:
        dict_colors.append(color.to_dict())

    return jsonify(dict_colors)


# Flask起動
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
