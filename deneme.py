from flask import Flask, jsonify, render_template,request
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)
   


@app.route('/',methods=['GET', 'POST'])#decorator
def sessions():
    return render_template('index5.html')



@socketio.on('addDataToBackendSql')
def tabloyaEkleBackend(FrontenddenGelenData, methods=['GET', 'POST']):
    ipadr=request.remote_addr



@socketio.on('connect_to_server')
def tumSqlDatasiniGonder(FrontenddenGelenData, methods=['GET', 'POST']):
    print(FrontenddenGelenData)
    socketio.emit('backend_sends_all_list',"tasks22")


if __name__ == '__main__':
    socketio.run(app,host='127.0.0.1',debug=True,port=5000)
