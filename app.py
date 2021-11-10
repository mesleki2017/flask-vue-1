from flask import Flask, jsonify, render_template,request
from flask_socketio import SocketIO
import pyisleri.sql_isleri1 as aa

aa.sql_tablo_olustur("kendim")


app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)
   


@app.route('/',methods=['GET', 'POST'])#decorator
def sessions():
    return render_template('index5.html')



@socketio.on('addDataToBackendSql')
def tabloyaEkleBackend(FrontenddenGelenData, methods=['GET', 'POST']):
    g_title = FrontenddenGelenData["title"]
    g_done=FrontenddenGelenData["done"]
    aa.addToSqlTable("kendim",g_title,g_done)

@socketio.on('deleteRowsBackendSql')
def tablodanSilBackend(FrontenddenGelenData, methods=['GET', 'POST']):
    print("delete this row with id : ",FrontenddenGelenData)
    aa.tablodan_sil("kendim",FrontenddenGelenData)
    socketio.emit('backend_sends_all_list', aa.sql_to_list("kendim"))

@socketio.on('taskDoneChange')
def tabloDuzenleBackend(FrontenddenGelenData, methods=['GET', 'POST']):
    print(FrontenddenGelenData)
    aa.tabloda_duzenle("kendim",str(FrontenddenGelenData["id"]),"done",FrontenddenGelenData["done"])


@socketio.on('connect_to_server')
def tumSqlDatasiniGonder(FrontenddenGelenData, methods=['GET', 'POST']):
    socketio.emit('backend_sends_all_list', aa.sql_to_list("kendim"))


if __name__ == '__main__':
    socketio.run(app,host='127.0.0.1',debug=True,port=5000)
