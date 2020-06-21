<?php
    $output = shell_exec('service MCServ status');
    
    if (preg_match('/\bActive\b/', $output)){
        $val = "Connected";
    }
    else{
        $val = "Error";
    }
    echo "$val";
?>