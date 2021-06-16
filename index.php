<?php
require_once "./vendor/autoload.php";
use quynhthu\DetectAttacker\DetectAttacker;
$text = $_GET["text"] ?? "";
$result = ( new DetectAttacker($text))->handle();
$dataObj = new \stdClass();
$dataObj->text = $text;
$dataObj->result = $result;

$dataJSON = json_encode($dataObj);

echo $dataJSON;