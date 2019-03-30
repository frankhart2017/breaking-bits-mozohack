<?php 


$db['db_host'] = "localhost";
$db['db_user'] = "D0L1njfQuf";
$db['db_pass'] = "qd1YrRTmsl";
$db['db_name'] = "D0L1njfQuf";

foreach ($db as $key => $value ) {

    define(strtoupper($key), $value);

}

$connection = mysqli_connect(DB_HOST,DB_USER,DB_PASS,DB_NAME);

if(!$connection) {

    die('connection failed');

}


?>