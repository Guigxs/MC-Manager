<?php
    $output = shell_exec('service MCServ status');
    
    echo "$output";
?>