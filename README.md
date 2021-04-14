# FlaskSQLAlchemy ドキュメント

## ホーム

`https://flask-sqlalchemy.palletsprojects.com/en/2.x/`

## CRUD 操作（create, read, update, delete等の基本操作方法が載ってます）

`https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/`



# 「.docker」フォルダ以下に変更があった場合
```$ git pull origin master```

を実行後に「.docker」フォルダ以下に変更があった場合は

```$ docker-compose up -d --build```

実行してください

コンテナ内の環境が更新されます

# Flaskサーバー起動方法
```$ python3 /var/www/html/src/main.py```

実行してください（python3コマンドでmain.pyを実行してるだけ）

そうするとFlaskサーバーが起動するので、vue側からリクエストが受けられるようになります
