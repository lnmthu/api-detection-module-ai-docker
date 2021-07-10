<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class DetectionController extends Controller
{
    public function index(){
        return view("home");
    }
    public function store(Request $request)
    {
        $search = $request->input("search");
        $command = escapeshellcmd("python3 check.py ".$search);
        $result = shell_exec($command);
        $resultAfterDecode = json_decode($result);
        return view("home")->with("data",$resultAfterDecode);
    }
    public function api(Request $request)
    {
        $search = $request->input("search") ?? "";
        $search = urlencode($search);
        $command = escapeshellcmd("python3 check.py ".$search);
        $result = shell_exec($command);
        return $result;
    }
}
