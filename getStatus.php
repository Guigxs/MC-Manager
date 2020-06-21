<?php
    $output = shell_exec('service MCServ status');
    
    if (preg_match('/\bActive: active\b/', $output)){
        $val = "Running";
        echo "<div style='color: green;'>$val</div>";
    }
    else if (preg_match('/\bActive: inactive\b/', $output)){
        $val = "Not running";
        echo "<div style='color: red;'>$val</div>";
    }
    else{
        $val = "Error";
        echo "<div style='color: red;'>$val</div>";
    }

    echo "<p>$output</p>"
?>