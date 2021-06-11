<h1 align="center">Detect Attacker</h1>
<p align="center">
    <a href="https://packagist.org/packages/haruncpi/laravel-log-reader"><img src="https://badgen.net/packagist/v/haruncpi/laravel-log-reader" /></a>
    <a href="https://en.wikipedia.org/wiki/MIT_License"><img src="https://badgen.net/github/license/micromatch/micromatch" /></a>
     <a href=""><img src="https://badgen.net/packagist/dt/quynhthu/detect-attacker"/></a>
    <a href="https://www.facebook.com/lnmthu1"><img src="https://badgen.net/badge/facebook/thule/3b5998"/></a>
    <a href="https://www.facebook.com/nhuquynh9985"><img src="https://badgen.net/badge/facebook/nhuquynh/3b5998"/></a>
</p>
<p align="center">Using AI to detect attacker is XSS or SQL)</p>



## Install
```bash
composer require quynhthu/detect-attacker
```

## Use 
```bash
# return string
use quynhthu\DetectAttacker\DetectAttacker;
return (new DetectAttacker("' or 1=1 # "))->handle();
```
## Change Log
v2.1