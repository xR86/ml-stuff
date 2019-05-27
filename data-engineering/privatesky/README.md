# privatesky


## Run privatesky in a docker

Not recommended, since all examples require the file to be accessed by `file:///` link, maybe a `python3 -m http.server` can help with this):
+ `docker run -i -v /home:/home --name node-privatesky2 node:10.15.3-jessie-slim`
+ `docker exec -it node-privatesky2 /bin/bash`
  + `apt-get update`
  + `apt-get install git -y`
  + `git clone https://github.com/PrivateSky/privatesky`
  + `npm run install`
  + `npm run start`
  + in a separate terminal with docker exec, modify files as indicated in [~adria/teach/courses/pcd/resources/PrivateSky.pdf](https://profs.info.uaic.ro/~adria/teach/courses/pcd/resources/PrivateSky.pdf)

Obs: Slimmer - node:10.15.3-alpine  
Obs: Account for port fwd...

---

## PrivateSky CSBUI (Cloud Safe Boxes User Interface)

Drop the `--restart always` in the `docker/start.sh` file.  
In case configuration of the CSBUI is abandoned or exited, regardless of the how, future deployments of CSBUI docker and/or privatesky standalone will require a PIN that can't be set because of an invalid seed => configuration is invalid, as such the user must purge the browser cache for that page (eg: Chrome - F12 -> Application Tab -> Clear storage page -> Clear site data), and/or use incongnito sessions for further testing.

