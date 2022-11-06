from machine import I2C
from machine import Pin
from machine import sleep
import mpu6050
import sys
#Initialisering af I2C objekt
i2c = I2C(scl=Pin(22), sda=Pin(21))     
#Initialisering af mpu6050 objekt
mpu = mpu6050.accel(i2c)
while True:
 try:
  print(mpu.get_values())
  sleep(500)
 except KeyboardInterrupt:
  print("Ctrl+C pressed - exiting program.")
  sys.exit()



