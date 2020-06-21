<?php
    $output = shell_exec('service MCServ status');
    
    if (preg_match('/\bActive: active\b/', $output)){
        $val = "Running";
        echo "<p style='color: green;'>$val</p>";
    }
    else if (preg_match('/\bActive: inactive\b/', $output)){
        $val = "Not running";
        echo "<p style='color: red;'>$val</p>";
    }
    else{
        $val = "Error";
        echo "<p style='color: red;'>$val</p>";
    }

    echo "<p>$output</p>"
?>