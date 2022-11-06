import gps_funktion
import umqtt_robust2 as mqtt
from machine import Pin, ADC, I2C
import time
import neopixel
import tm1637
from imu import MPU6050

# Her kan i placere globale varibaler, og instanser af klasser
# til gps
gps_data = gps_funktion.gps_to_adafruit
# til batteri
analog_pin = ADC(Pin(34))
analog_pin.atten(ADC.ATTN_11DB)
analog_pin.width(ADC.WIDTH_12BIT)
analog_val = analog_pin.read()
volts = (analog_val * 0.00084638*5)
# til batteri display:
tm = tm1637.TM1637(clk=Pin(5), dio=Pin(4))
tm1 = tm1637.TM1637(clk=Pin(19), dio=Pin(18))
tm.show('    ')
tm1.show('    ')
# IMU
i2c = I2C(0, sda=Pin(21), scl=Pin(22), freq=400000)
imu = MPU6050(i2c)
antaltaklinger = 0
# neopixel
def clear():
    for i in range(n):
        np[i] = (0,0,0)
        np.write()
while True:
    gps_data = gps_funktion.gps_to_adafruit
    acceleration = imu.accel
    gyroscope = imu.gyro
    analog_val = analog_pin.read()
    volts = (analog_val * 0.00084638*5)    
    try:
        # Jeres kode skal starte her
        if abs(acceleration.z) > 0.8:
            if (acceleration.z > 0):
                print("Faldet på ryggen")
                antaltaklinger = antaltaklinger + 1
                while (acceleration.z >= 0.7):
                    time.sleep(1)
                    print("Venter")
                    time.sleep(1)
           
            else:
                print("Faldet på maven")
                antaltaklinger = antaltaklinger + 1
                while (acceleration.z <= 0.5):
                    time.sleep(1)
                    print("Venter")
                    time.sleep(1)
                    
        if antaltaklinger > 0:
            ttt = str(antaltaklinger)
            tm1.show(ttt, False)
            mqtt.web_print(antaltaklinger, 'gruppe1a/feeds/tacklingfeed/csv')
            sleep(3)
            
        
        if gps_data != None:
            mqtt.web_print(gps_data, 'gruppe1a/feeds/gpsfeed/csv')        
            sleep(3)
        
        if analog_val >= 0:
            mqtt.web_print(volts, 'gruppe1a/feeds/batterifeed/csv')
            sleep(3)
        
        if volts > 8.1:
            tm.show(' 100', False)
            mqtt.web_print(100, 'gruppe1a/feeds/procentfeed/csv')
            sleep(3)

        elif volts <= 8.1 and volts >= 7.71:
            tm.show('  90', False)
            mqtt.web_print(90, 'gruppe1a/feeds/procentfeed/csv')
            sleep(3)
            
        elif volts <= 7.7 and volts >= 7.66:
            tm.show('  80', False)
            mqtt.web_print(80, 'gruppe1a/feeds/procentfeed/csv')
            sleep(3)
        
        elif volts <= 7.65 and volts >= 7.6:
            tm.show('  70', False)
            mqtt.web_print(70, 'gruppe1a/feeds/procentfeed/csv')
            sleep(3)
            
        elif volts <= 7.59 and volts >= 7.51:
             tm.show('  60', False)
             mqtt.web_print(60, 'gruppe1a/feeds/procentfeed/csv')
             sleep(3)
             
        elif volts <= 7.5 and volts >= 7.46:
             tm.show('  50', False)
             mqtt.web_print(50, 'gruppe1a/feeds/procentfeed/csv')
             sleep(3)
        elif volts <= 7.45 and volts >= 7.41:
            tm.show('  40', False)
            mqtt.web_print(40, 'gruppe1a/feeds/procentfeed/csv')
            sleep(3)
        elif volts <= 7.4 and volts >= 7.31:
            tm.show('  30', False)
            mqtt.web_print(30, 'gruppe1a/feeds/procentfeed/csv')
            sleep(3)
        elif volts <= 7.3 and volts >= 7:
            tm.show('  20', False)
            mqtt.web_print(20, 'gruppe1a/feeds/procentfeed/csv')
            sleep(3)
        elif volts < 7.0 and volts >=6.8:
            tm.show('  10', False)
            mqtt.web_print(10, 'gruppe1a/feeds/procentfeed/csv')
            sleep(3)
        elif volts < 6.7 and volts >=6.0:
            tm.show('   0', False)
            mqtt.web_print(0, 'gruppe1a/feeds/procentfeed/csv')
            sleep(3)
        elif volts <= 5.9:
            tm.scroll("no battery", 50)
            mqtt.web_print(0, 'gruppe1a/feeds/procentfeed/csv')
            sleep(3)
            
        if mqtt.besked == "svar_tilbage":
            mqtt.web_Print("ESP32 her!")
            sleep(3)
        
        # Jeres kode skal slutte her
        sleep(0.5)
        if len(mqtt.besked) != 0: # Her nulstilles indkommende beskeder
            mqtt.besked = ""            
        mqtt.sync_with_adafruitIO() # igangsæt at sende og modtage data med Adafruit IO             
        print(".", end = '') # printer et punktum til shell, uden et enter        
    # Stopper programmet når der trykkes Ctrl + c
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        clear()
        mqtt.c.disconnect()
        mqtt.sys.exit()