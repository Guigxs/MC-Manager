from bottle import route, run, template, get, post, request, redirect, static_file, SimpleTemplate
import os
import subprocess

host = '0.0.0.0'
port = 8091

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@get("/")
def mcServ():
    return template('templates/main', Status=getServiceStatus(), State="coucou")

@route("/", method='POST')
def controller():
    cmd = request.forms.get('commandSend')
    btnStart = request.forms.get('startServer')
    btnStop = request.forms.get('stopServer')
    btnLogs = request.forms.get('showLogs')
    
    if (btnStart):
        print("Starting server...")
        print(sendCommand("sudo systemctl start MCServ.service"))

    if (btnStop):
        print("Stopping server...")
        print(sendCommand("sudo systemctl stop MCServ.service"))
    
    if (btnLogs):
        print("Show logs...")
        redirect("/logs")

    if (cmd):
        print(sendServerCommand(cmd))

    return mcServ()

@route("/logs", method="GET")
def logs():
    out = sendCommand("cat /home/gui/Lilou/logs/latest.log | aha").decode()
    return '''
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
                    integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    {}

    <form method='GET' action='/'>
        <input class='btn btn-secondary btn-sm' value='Back to server page' type="submit"></input>
    </form>
    
    '''.format(out)

@route("/static/<filename>")
def server_static(filename):
    return static_file(filename, root="./static")


def getServiceStatus():
    process = subprocess.Popen("sudo systemctl status MCServ.service", shell = True, stdout=subprocess.PIPE).stdout.read()

    if ("Active: active" in process.decode()):
        return "<b style='color : green;'>Connected</b>"

    elif ("Active: inactive" in process.decode()):
        return "<b style='color : red;'>Not connected</b>"
    
    else :
        return "<b style='color : red;'>Error</b>"

def getStatesInfo():
    process = subprocess.Popen("sudo systemctl status MCServ.service | grep Active", shell = True, stdout=subprocess.PIPE).stdout.read()

    print(process.decode().split("\n"))


def sendServerCommand(command):
    process = subprocess.Popen("screen -S MCServ -X stuff '{}\n'".format(command), shell = True, stdout=subprocess.PIPE).stdout.read()
    return process

def sendCommand(command):
    process = subprocess.Popen(command, shell = True, stdout=subprocess.PIPE).stdout.read()
    return process


if __name__ == "__main__":
    run(host=host, port=port, reloader=True, debug=True)
