<?php
    $output = shell_exec('service MCServ status');
    
    if (preg_match('/\bActive: active\b/', $output)){
        $val = "Running";
        echo "<div class='status'>Status: <b style='color: green;'>$val</b></div>";
        echo "<div class='start'><form method='post'><input type='submit' class='btn btn-info' value='Show console' name='showConsole'></input> <input type='submit' class='btn btn-danger' value='Stop serve' name='stopServer'></input></form></div>";
    }
    else if (preg_match('/\bActive: inactive\b/', $output)){
        $val = "Not running";
        echo "<div class='status'>Status: <b style='color: red;'>$val</b></div>";
        echo "<div class='start'><form method='post'><input type='submi' class='btn btn-primary' value='Start server' name='startServer'></input></form></div>";
    }
    else{
        $val = "Error";
        echo "<div class='status'>Status: <b style='color: red;'>$val</b></div>";
        echo "<div class='start'><form method='post'><input type='submit' class='btn btn-primary' value='Show logs' name='showLogs'></input></form></div>";
    }

    echo "<p>$output</p>"
?>