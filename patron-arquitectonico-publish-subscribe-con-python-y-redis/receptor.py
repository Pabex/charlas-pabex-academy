import redis

r = redis.Redis(host="localhost", port=6379, db=0)
s = r.pubsub()

s.subscribe("pabex_academy")

print("Suscripto correctamente al canal pabex_academy")

try:
    for message in s.listen():
        data = message["data"]
        if isinstance(data, bytes):
            data = data.decode("utf-8")
            print("Se recibió: %s" % data)
except KeyboardInterrupt:
    print("Saliendo")
