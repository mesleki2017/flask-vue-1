from flask import Flask, jsonify, render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///list1.db"
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)    


@app.route('/',methods=['GET', 'POST'])#decorator
def sessions():
    return render_template('index5.html')

##CREATE TABLE
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(250),nullable=False)
    done = db.Column(db.Boolean)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Todo {self.task}>'


def create_db():
    db.create_all()

    # CREATE RECORD
    new_book = Todo(task="fff", done=False)
    db.session.add(new_book)
    db.session.commit()

task = Todo.query.filter_by(task="fff").first()
print(task.id)

@socketio.on('addDataToBackendSql')
def tabloyaEkleBackend(FrontenddenGelenData, methods=['GET', 'POST']):
    ipadr=request.remote_addr
    new_task = Todo(task=FrontenddenGelenData["title"], done=FrontenddenGelenData["done"])
    db.session.add(new_task)
    db.session.commit()

@socketio.on('connect_to_server')
def tumSqlDatasiniGonder(FrontenddenGelenData, methods=['GET', 'POST']):
    print(FrontenddenGelenData)
    tasks22 = Todo.query.all()
    print(type(tasks22))
    socketio.emit('backend_sends_all_list',"tasks22")


if __name__ == '__main__':
    socketio.run(app,host='127.0.0.1',debug=True,port=5000)
