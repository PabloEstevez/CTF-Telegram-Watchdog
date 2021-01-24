#!/usr/bin/python3

import os
import requests
import socket
import json

## FUNCIONES ##
def check_url(reto):
    r = requests.get(reto["url"])
    if r.status_code != 200: check = False
    else: check = True
    return((check,r.status_code))

def check_port(reto):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    resultado = s.connect_ex((reto["ip"],reto["port"]))
    if resultado == 0: check = True
    else: check = False
    s.close()
    return((check, str(resultado)))

def notifica(texto):
    r = requests.get(bot_url + "sendMessage?chat_id=" + group_id + "&text=" + str(texto) + "&parse_mode=Markdown")
###

## DEFINICIONES ##
# A cada reto de tipo "clave" se le asigna una funcion de check: valor
function_dict = {"web":check_url, "netcat":check_port}
try:  
   bot_TOKEN = os.environ['bot_TOKEN']
   group_id = os.environ['group_id']
except KeyError: 
   print("Por favor, define las variables de entorno bot_TOKEN y group_id")
   sys.exit(1)
bot_url = "https://api.telegram.org/bot" + bot_TOKEN + "/"
###

# Lee la configuracion
config_file = open("config.json", "r")
config_str = config_file.read()
config = json.loads(config_str)
config_file.close()

# Comprueba uno a uno los retos
for reto in config:
    resultado = function_dict[config[reto]["type"]](config[reto])
    if resultado[0] != True: 
        notifica("El reto *" + reto + "* no esta disponible.\n\nMensaje de error: ```" + resultado[1] + "```")
