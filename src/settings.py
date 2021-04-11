from datetime import datetime
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from os.path import join, dirname
from dotenv import load_dotenv

# 環境変数の取得
load_dotenv(verbose=True)
dialect = getenv('DIALECT')
driver = getenv('DRIVER')
db_user = getenv('DB_USER')
db_pass = getenv('DB_PASS')
db_host = getenv('DB_HOST')
db_port = getenv('DB_PORT')
db_name = getenv('DB_NAME')
secret_key = getenv('SECRET_KEY')

# DB接続用URI生成
uri = f'{dialect}+{driver}://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'

# Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = uri
db = SQLAlchemy(app)


# Todoモデル
class Todo(db.Model):
    __tablename__ = 'todo'

    id_todo = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500))
    color_code = db.Column(db.String(10))
    checked = db.Column(db.Boolean)
    dt_do = db.Column(db.DateTime)
    dt_create = db.Column(db.DateTime, default=datetime.utcnow)
    dt_update = db.Column(db.DateTime, onupdate=datetime.utcnow)

    # dictに変換
    def to_dict(self):
        return {
            'id_todo': self.id_todo,
            'content': self.content,
            'color_code': self.color_code,
            'checked': self.checked,
            'dt_do': format_date(self.dt_do),
            'dt_create': format_date(self.dt_create),
            'dt_update': format_date(self.dt_update)
        }

    def __init__(self, content, color_code, checked, dt_do):
        self.content = content
        self.color_code = color_code
        self.checked = checked
        self.dt_do = dt_do


# datetimeを「%Y-%m-%d %H:%M:%S」形式に変換するメソッド
def format_date(datetime):
    if datetime is None:
        return None
    return datetime.strftime('%Y-%m-%d %H:%M:%S')


# 定義したモデルをDBに反映
# db.drop_all()
db.create_all()
