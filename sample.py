#Flaskの雛形
#必要なモジュールをインポート
from flask import Flask

#Flaskをインスタンス化
app = Flask(__name__)

#ルートディレクトリにアクセスがあった時の処理
@app.route('/')
def hello():
    return 'Hello World!'

#エントリーポイント
if __name__ == '__main__':
    app.run()