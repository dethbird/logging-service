<?php

require ("vendor/autoload.php");
require_once("LoggingServiceClient.php");

$logger = new LoggingServiceClient("http://11dd6794.ngrok.io");
$response = $logger->syslog("INFO", "Log message from PHP", array("foo"=>"bar"));
echo $response->body;

 ?>
