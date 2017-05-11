# tor-privoxy-alpine with compose and autochanging exit node

The smallest (**15 MB**) docker image with Tor and Privoxy on Alpine Linux and compose-file to run ten instances of this container. 
Exit node on each container change every 30 sec. 
```
sudo docker-compose -f tor_compose.yml up
curl --proxy localhost:8118 https://www.google.com
...
curl --proxy localhost:8127 https://www.google.com
```

## Source of this fork
* [tor-privoxy-alpine](https://github.com/rdsubhas/docker-tor-privoxy-alpine)
