<h1 align="center">Detection Module</h1>
<p align="center">
    <a href="https://hub.docker.com/repository/docker/thuicetea/module_detection"><img src="https://badgen.net/docker/size/library/ubuntu" /></a>
     <a href="https://hub.docker.com/repository/docker/thuicetea/module_detection"><img src="https://badgen.net/docker/pulls/library/ubuntu" /></a>
      <a href="http://php.net"><img src="https://badgen.net/packagist/php/monolog/monolog" /></a>
    <a href="https://en.wikipedia.org/wiki/MIT_License"><img src="https://badgen.net/github/license/micromatch/micromatch" /></a>
    <a href="https://www.facebook.com/lnmthu1"><img src="https://badgen.net/badge/facebook/thule/3b5998"/></a>
    <a href="https://www.facebook.com/nhuquynh9985"><img src="https://badgen.net/badge/facebook/nhuquynh/3b5998"/></a>
</p>
<p align="center">Use AI (CNN) to detect attacker is XSS or SQL</p>



## Install
```bash
git clone https://github.com/lnmthu/module_detection.git
```

## Use 
```bash
cd module_detection && docker-compose up -d --build
```
## Access
```bash
localhost:8080/?text=' or 1=1 #
```
