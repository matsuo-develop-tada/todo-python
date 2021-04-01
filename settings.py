from sqlalchemy import create_engine
from os import getenv
from os.path import join, dirname
from dotenv import load_dotenv

# 環境変数をどのファイルから読み込むかを設定
load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# 環境変数の取得
dialect = getenv('DIALECT')
driver = getenv('DRIVER')
db_user = getenv('DB_USER')
db_pass = getenv('DB_PASS')
db_host = getenv('DB_HOST')
db_port = getenv('DB_PORT')
db_name = getenv('DB_NAME')
charset = getenv('CHARSET')

# DB接続用url生成
url = f'{dialect}+{driver}://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
print(url)

# DB接続
engine = create_engine(url, echo=True)
print(engine)

engine.execute('DROP TABLE IF EXISTS todo')
engine.execute('CREATE TABLE todo (id INT PRIMARY KEY AUTO_INCREMENT, content VARCHAR(500))')
engine.execute("INSERT INTO todo (content) VALUES ('todo1')")
engine.execute("INSERT INTO todo (content) VALUES ('todo2')")
engine.execute("INSERT INTO todo (content) VALUES ('todo3')")
todos = engine.execute('SELECT * FROM todo')

for todo in todos:
    print(todo)

