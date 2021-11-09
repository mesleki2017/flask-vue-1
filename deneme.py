
from flask_socketio import SocketIO
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aaa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)
socketio = SocketIO(app)

 # Define ORM
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(120), unique=True)
    done = db.Column(db.Boolean)

    def __init__(self, title, description, done):
        self.title = title
        self.description = description
        self.done = done

    def __repr__(self):
        return '<Todo %r>' % self.title
        
def create_db():
    # Recreate database each time for demo
    #db.drop_all()
    db.create_all()


create_db()


tasks = [Todo('Buy groceries', 'Milk, Cheese, Pizza, Fruit, Tylenol', False),
             Todo('Learn Python', 'Need to find a good Python tutorial on the web', False),
             Todo('Mow the lawn', 'Find out some tools', False)]
db.session.add_all(tasks)
db.session.commit()


@app.route('/',methods=['GET', 'POST'])#decorator
def sessions():
    return render_template('index5.html')

if __name__ == '__main__':
    socketio.run(app,host='127.0.0.1',debug=True,port=5000)

