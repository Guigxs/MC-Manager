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

        <?php 
            include "getStatus.php";
            
            if (array_key_exists('stopServer', $_POST)){
                echo 'stopping';
                echo shell_exec("service MCServ stop");
            }
            else if (array_key_exists('showConsole', $_POST)){
                echo 'console';
            }

            else if (array_key_exists('startServer', $_POST)){
                echo 'starting';
                echo shell_exec("service MCServ start");
            }

            else if (array_key_exists('showLogs', $_POST)){
                echo 'logs';
                echo shell_exec("service MCServ status");
            }

            if (array_key_exists('sendCommand', $_POST)){
                $cmd = $_POST["commandSend"];
                //$out = shell_exec("screen -S MCServ -X stuff '$cmd\n'");
                $out = exec($cmd);
            }
        ?>

        <div class="terminal">
            <div class="console">
                <?php echo $out?>
            </div>

            <div class="command">
                <form method="post">
                    <div class="form-group row pl-4 pr-4 pt-2">
                        
                        <input type="text" name="commandSend" id="commandSend", class="form-control col-sm-10"></input>
                        <input type="submit" class='btn btn-secondary btn-sm col-sm-2' value='Send' name='sendCommand'></input>
                    
                    </div>
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