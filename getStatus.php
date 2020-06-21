<?php
    $output = shell_exec('service MCServ status');
    
    if (preg_match('/\bActive: active\b/', $output)){
        $val = "Running";
        echo "<b style='color: green;'>$val</b>";
    }
    else if (preg_match('/\bActive: inactive\b/', $output)){
        $val = "Not running";
        echo "<b style='color: red;'>$val</b>";
    }
    else{
        $val = "Error";
        echo "<b style='color: red;'>$val</b>";
    }

    #echo "<p>$output</p>"
?>