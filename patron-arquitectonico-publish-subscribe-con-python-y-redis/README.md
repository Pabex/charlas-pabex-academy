# Pasos para ejecutar #

## Paso 1 ##
Se requiere tener instalado el servidor de Redis:

https://redis.io/download

## Paso 2 ##
También se necesita conectar Python con el servidor de Redis, para ello se debe instalar la siguiente librería:

https://pypi.org/project/redis/

Este paquete ya está agregar en el archivo requirements.txt.

## Paso 3 ##
Se debe ejecutar: python3 receptor.py

## Paso 4 ##
En otra terminar, se debe ejecutar: python4 emisor.py

## Paso 5 ##
Comprobar cómo llegan los mensajes enviados por el emisor al receptor. Se puede jugar un poco más, ejecutando varios receptores.
