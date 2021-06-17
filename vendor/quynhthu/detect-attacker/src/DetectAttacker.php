<?php

namespace quynhthu\DetectAttacker;

class DetectAttacker 
{
    const NORMAL = 0;
    const XSS = 1;
    const SQL = 2;

    protected $search = "";
    
    public function __construct($search)
    {
        $this->search = $search;
    }

    public function handle()
    { 
        $command = escapeshellcmd("python3 vendor/quynhthu/detect-attacker/check.py ".$this->search);
        $result = shell_exec($command);
        return $result;
    }
}
