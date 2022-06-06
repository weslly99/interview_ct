
### Antes de tudo tenha instalado no sistema
* Docker 
* docker-compose

## Rodando o app
De dentro da pasta raiz rode o comando:
```sh
  docker-compose up -d
```

## Utilização
você pode acessar o app pelo endereço: http://127.0.0.1:5000/api/v1/artists/{artist_name}

```sh
curl http://127.0.0.1:5000/api/v1/artists/drake
```
para apagar o cache basta enviar uma querystring com cache=false

```
curl http://127.0.0.1:5000/api/v1/artists/drake/?cache=false
```
