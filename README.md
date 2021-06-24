<h1 align="center">Detection Module</h1>
<p align="center">
    <a href="https://hub.docker.com/repository/docker/thuicetea/module_detection"><img src="https://badgen.net/docker/size/library/ubuntu" /></a>
     <a href="https://hub.docker.com/repository/docker/thuicetea/module_detection"><img src="https://badgen.net/docker/pulls/library/ubuntu" /></a>
      <a href="https://lumen.laravel.com/"><img src="https://badgen.net/badge/lumen/orange/8.0" /></a>
    <a href="https://en.wikipedia.org/wiki/MIT_License"><img src="https://badgen.net/github/license/micromatch/micromatch" /></a>
    <a href="https://www.facebook.com/lnmthu1"><img src="https://badgen.net/badge/facebook/thule/3b5998"/></a>
    <a href="https://www.facebook.com/nhuquynh9985"><img src="https://badgen.net/badge/facebook/nhuquynh/3b5998"/></a>
</p>
<p align="center">Use AI (CNN) to detect attacker is XSS or SQL</p>
<img src="https://i.imgur.com/7ppBhpL.png">

## Install
```bash
docker run --privileged -d -p 8080:80 thuicetea/module_detection:version-model-final-one-UI
```

## Test with
# UI
```bash
# Access URL
http://localhost:8080/
```

# Curl
```bash
# Call API (return JSON)
curl -d "search=' or 1=1 #" http://localhost:8080/api
```
