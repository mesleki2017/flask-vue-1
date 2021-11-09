from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///list1.db"
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


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



