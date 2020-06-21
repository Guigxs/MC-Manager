from bottle import route, run, template, get, post, request
import os
import subprocess

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


@get("/")
def mcServ():

    return '''
        <!doctype html>
        <html lang="en">

            <head>
                <title>Minecraft manager</title>
                <!-- Required meta tags -->
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

                <!-- Bootstrap CSS -->
                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
                    integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
                <link rel="stylesheet" href="style.css">
            </head>

            <body>
                <div class="navbar navbar-expand-lg navbar-dark bg-dark">
                    <a class="navbar-brand" href="#">Minecraft Manager</a>
                </div>

                <div class='status' style='font-size: 50px; text-align : center;'>Status: {}</div>

                <div class="terminal">
                    <div class="console">
                    </div>

                    <div class="command">
                        <form method="post">
                            <div class="form-group row pl-4 pr-4 pt-2">
                                
                                <input type="text" name="commandSend" id="commandSend", class="form-control col-sm-10"></input>
                                <input type="submit" class='btn btn-secondary btn-sm col-sm-2' value='Send' name='sendCommand'></input>
                            
                            </div>
                            <input type="submit" class='btn btn-primary btn-sm col-sm-2' value='Start server' name='startServer'></input>
                            <input type="submit" class='btn btn-danger btn-sm col-sm-2' value='Stop server' name='stopServer'></input>
                            <input type="submit" class='btn btn-info btn-sm col-sm-2' value='Show logs' name='showLogs'></input>
                        </form>
                    </div>
                </div>
            

                <!-- Optional JavaScript -->
                <!-- jQuery first, then Popper.js, then Bootstrap JS -->
                <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
                    integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
                    crossorigin="anonymous"></script>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
                    integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1"
                    crossorigin="anonymous"></script>
                <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
                    integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM"
                    crossorigin="anonymous"></script>
            </body>

        </html>

    '''.format(getServiceStatus())

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

    if (cmd):
        print(sendServerCommand(cmd))

    return mcServ()

def getServiceStatus():
    process = subprocess.Popen("systemctl status MCServ.service", shell = True, stdout=subprocess.PIPE).stdout.read()
    print(process.decode())

    if ("Active: active" in process.decode()):
        return "<b style='color : green;'>Connected</b>"

    elif ("Active: inactive" in process.decode()):
        return "<b style='color : red;'>Not connected</b>"
    
    else :
        return "<b style='color : red;'>Error</b>"

def sendServerCommand(command):
    process = subprocess.Popen("screen -S MCServ -X stuff '{}\n'".format(command), shell = True, stdout=subprocess.PIPE).stdout.read()
    return process

def sendCommand(command):
    process = subprocess.Popen(command, shell = True, stdout=subprocess.PIPE).stdout.read()
    return process

run(host='0.0.0.0', port=8091)