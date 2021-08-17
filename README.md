# bak

Intead of typing :

```shell
cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.bak
```

you just need to type :

```shell
bak /etc/nginx/nginx.conf
```

## Setup

1. Clone the repository

```shell
git clone https://github.com/xanhacks/bak.git
cd bak
```

2. Add execute permission and move the script to your PATH.

```shell
chmod +x bak.py
mv bak.py /usr/local/bin/bak
```
