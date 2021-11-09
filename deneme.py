
from flask_socketio import SocketIO
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = "random string"

socketio = SocketIO(app)



@app.route('/',methods=['GET', 'POST'])#decorator
def sessions():
    return render_template('index5.html')

if __name__ == '__main__':
    socketio.run(app,host='127.0.0.1',debug=True,port=5000)

