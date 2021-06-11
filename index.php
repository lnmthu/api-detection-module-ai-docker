<?php
require_once "./vendor/autoload.php";
use quynhthu\DetectAttacker\DetectAttacker;
$detect = $_GET["detect"] ?? "";
echo (new DetectAttacker($detect))->handle();
