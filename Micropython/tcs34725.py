# Demo sensor de color TCS34725.
# Detecta el color que capta el sensor, lo imprime cada segundo y lo representa en el Led RGB.

import time 
import board
import busio 
import adafruit_tcs34725
from machine import Pin, PWM
 
 # Pines en esp-8266

D5 = 14 # rojo
D6 = 12 # verde
D7 = 13 # azul

rojo = PWM(Pin(D5), freq=500)
verde = PWM(Pin(D6), freq=500)
azul = PWM(Pin(D7), freq=500)

# Descomentar las siguientes lineas para probar el Led RGB

# rojo = Pin(D5, Pin.OUT)
# verde = Pin(D6, Pin.OUT)
# azul = Pin(D7, Pin.OUT)

# rojo.on()
# verde.on()
# azul.on()

# Inicializa bus de comunicacion I2C y sensor de color
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tcs34725.TCS34725(i2c)
sensor.integration_time = 200
sensor.gain = 60

# Bucle principal
while True:
	# Lee color, temperatura y lux del sensor, y la imprime.    
    temp = sensor.color_temperature
    lux = sensor.lux
    print('Temperature: {0}K Lux: {1}'.format(temp, lux))
    print('Color: ({0}, {1}, {2})'.format(*sensor.color_rgb_bytes))
    c = sensor.color_rgb_bytes
    print(c)

# Comentar las siguientes 3 lineas para probar el Led RGB con salidas digitales en modo Pin.
    rojo.duty(c[0] * 10)
    verde.duty(c[1] * 10)
    azul.duty(c[2] * 10)

    # Retardo de un segundo.
    time.sleep(1.0)
