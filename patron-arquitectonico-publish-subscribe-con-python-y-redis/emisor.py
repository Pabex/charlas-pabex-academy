import redis

r = redis.Redis()

print("Ingrese lo que se quiere enviar por el canal pabex_academy")

input_str = input()

r.publish("pabex_academy", input_str)
