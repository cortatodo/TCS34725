# TCS34725
Código para probar el sensor de colores TCS34725 con Micro Python
<img src='media/tcs34725-rgb-color-sensor-with-ir-filter-and-white-led.jpg/' width=200 height=200 />
Este es el sensor de color TCS34725 el cual es probado con codigo Micropython y microcontrolador esp-8266.
<img src='media/NodeMCU-Microncontroller.ppm/' width=300 height=200 />

para poder hacer funcionar el esp-8266 con el TCS34725 tuve que hacer unos cambios en el firmware y usar el de Adafruit(&trade;)

que descargue aqui https://github.com/adafruit/circuitpython/releases/download/3.1.2/adafruit-circuitpython-feather_huzzah-3.1.2.bin 

Es una version en desuso pero para hacer la prueba funciono.

En este punto es importante indicar que para instalar el firmware use esptools, si no esta familiarizado hay otros tutoriales con la documentacion de uso y para instalarlo, borre la memoria flash del esp-8266 e instale el firmware.

Una vez instalado el firmware entonces se requiere de ampy (de Adafruit(&trade;) tambien) que es el interface para poner los archivos de python en el board esp-8266.
