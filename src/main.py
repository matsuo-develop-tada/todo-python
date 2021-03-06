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


@app.route('/todos', methods=['POST'])
def regist_todo():
     # vueから渡ってきたデータを取得する
    content = request.json["content"]
    deadline = request.json["dt_do"]
    color_code = request.json["color_code"]

    # それぞれのパラメータを渡してtodoをインスタンス化する
    todo = Todo(content, color_code, False, deadline)

    db.session.add(todo)
    db.session.commit()

    return jsonify(todo.to_dict())

@app.route('/delTodos', methods=['POST'])
def del_todos():
    # vue側からもらった削除するtodoのidを取得する
    delTodoIds = request.json
    # 画面からもらったtodo_idを参考にしてDBのデータを削除する
    for delTodoId in delTodoIds:
        delTodo = db.session.query(Todo).filter(Todo.id_todo == delTodoId).one()
        db.session.delete(delTodo)
    db.session.commit()

    return {}

@app.route('/getSingleTodo', methods=['GET'])
def get_single_todo():
    updateTodoId = request.args.get('id_todo')
    upDateTodo = db.session.query(Todo).filter(Todo.id_todo == updateTodoId).one()

    return jsonify(upDateTodo.to_dict())

@app.route('/updateTodo', methods=['POST'])
def update_todo():
    # フロント側から送られてきたオブジェクトからidを取得する
    updateTodoId = request.json['id_todo']
    updateTodo = db.session.query(Todo).filter(Todo.id_todo == updateTodoId).one()

    # 更新処理を行う内容を取得、代入
    updateTodo.content = request.json['content']
    updateTodo.color_code = request.json['color_code']
    updateTodo.dt_do = request.json['dt_do']

    db.session.commit()

    return {}

@app.route('/updateCheckFlg', methods=['POST'])
def update_checkFlg():
    # フロントのチェックボックスにチェックがつけられたタスクのidを取得する
    updateCheckFlgId = request.args.get('id_todo')
    updateTodo = db.session.query(Todo).filter(Todo.id_todo == updateCheckFlgId).one()

    # チェックフラグを反転させる
    updateTodo.checked = not updateTodo.checked
    db.session.commit()

    return {}


# Flask起動
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
