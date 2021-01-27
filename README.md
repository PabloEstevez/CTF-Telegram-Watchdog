# CTF-Telegram-Watchdog

Bot de telegram que va comprobando que los retos estén en buen estado. Si alguno tiene algún problema, envía un mensaje de error a un grupo de telegram donde deben estar los administradores.

La idea es que el script principal ("watchdog.py") se ejecute en un cronjob cada cierto tiempo.

Ahora mismo hay implementadas funciones de check para retos Web y de netcat (conectarse a un puerto remoto donde se ejecuta un programa). En un futuro habría que ir implementando funciones de check para otros tipos de retos e ir mejorando las existentes.

## Archivo de configuración

El archivo de configuración es *config.json*. En el primer nivel de jerarquía se ponen los nombres de los retos como clave y como valor se anida otra lista de parámetros. El script principal va a mirar solamente el primer nivel de jerarquía, así que lo que hay dentro de cada reto se puede personalizar todo lo que se quiera. La función de check implementada para los nuevos retos tiene que encargarse de leer los niveles jerárquicos inferiores al primer nivel.

## check_url

Esta función hace un GET a la URL donde está la web del reto. Si le devuelve un 200, supone que está todo OK.

## check_port

Esta función intenta conectarse al puerto especificado en la configuración. Si lo consigue, supone que está todo OK.

## Ejecución

```
bot_TOKEN="123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11" group_id="196925415" python3 watchdog.py

```
