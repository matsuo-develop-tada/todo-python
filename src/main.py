from flask import jsonify, request
from settings import app, db, Todo, Color


@app.route('/todos', methods=['GET'])
def get_todos():
    color_code = request.args.get('color_code')
    dt_do = request.args.get('dt_do')

    query = Todo.query
    if color_code:
        query = query.filter(Todo.color_code == color_code)
    if dt_do:
        query = query.filter(Todo.dt_do == dt_do)
    todos = query.all()

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


@app.route('/regist', methods=['POST'])
def regist_todo():
     # vueから渡ってきたデータを取得する
    content = request.json["content"]
    deadline = request.json["dt_do"]
    color_code = request.json["color_code"]

    # それぞれのパラメータを渡してtodoをインスタンス化する
    todo = Todo(content, color_code, False, deadline)

    db.session.add(todo)
    db.session.commit()

    return "hello"


# Flask起動
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
