<?php
require_once "./vendor/autoload.php";
use quynhthu\DetectAttacker\DetectAttacker;
$text = $_POST["text"] ?? "";
$result = ( new DetectAttacker($text))->handle();
echo $result;