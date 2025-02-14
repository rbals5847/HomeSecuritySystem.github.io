#system LIB
import time as tm
import threading
import serial

#Python GPIO LIB
from RPi import GPIO

#My Lib
from My_Lib import My_RPi_GPIO_Lib_V1_2 as my_gpio

import pir_sensor

io = my_gpio.Gpio_Lib_Pin_Out()

my_port =None
my_port1 =None

rx_flag = False
run_flag = True
rx_buf = 0

#FULL Color LED
__R_pin__ = 26 
__G_pin__ = 19
__B_pin__ = 13


full_led = (__R_pin__,__G_pin__,__B_pin__)

def fc_led_bit(data):
    
    match data:
       case 0:
            io.d_out(__R_pin__, 1)
            io.d_out(__G_pin__, 0)
            io.d_out(__B_pin__, 0)
                     
       case 1:
            io.d_out(__R_pin__, 1)
            io.d_out(__G_pin__, 0)
            io.d_out(__B_pin__, 0)
         
       case 2:
            io.d_out(__R_pin__, 0)
            io.d_out(__G_pin__, 1)
            io.d_out(__B_pin__, 0)
            
       case 3:
            io.d_out(__R_pin__, 1)
            io.d_out(__G_pin__, 1)
            io.d_out(__B_pin__, 0)
            
       case 4:
            io.d_out(__R_pin__, 0)
            io.d_out(__G_pin__, 0)
            io.d_out(__B_pin__, 1)
                   
       case 5:
            io.d_out(__R_pin__, 1)
            io.d_out(__G_pin__, 0)
            io.d_out(__B_pin__, 1)
            
       case 6:
            io.d_out(__R_pin__, 0)
            io.d_out(__G_pin__, 1)
            io.d_out(__B_pin__, 1)
            
       case 7:
            io.d_out(__R_pin__, 1)
            io.d_out(__G_pin__, 1)
            io.d_out(__B_pin__, 1)

    
def rx_func(port):
    global rx_flag, rx_buf
    while run_flag:
        if port.readable():
            rx_buf = port.readline().decode("utf-8").strip()
            rx_flag = True
            print(f"Received: {rx_buf}")


def setup():
    global my_port
    
    #dev gpio mode set
    GPIO.setmode(GPIO.BCM) 
    
    my_port = serial.Serial("/dev/ttyAMA4", 115200)
    #my_port1 = serial.Serial("/dev/ttyAMA3", 115200) 
    
   
    
    GPIO.setup(pir_sensor.__PIR__, GPIO.IN)
    GPIO.setup(pir_sensor.__MQ_Sensor__,  GPIO.IN)
    
    GPIO.setup(__R_pin__,GPIO.OUT,initial = GPIO.LOW)
    GPIO.setup(__G_pin__,GPIO.OUT,initial = GPIO.LOW)
    GPIO.setup(__B_pin__,GPIO.OUT,initial = GPIO.LOW)

def main():
    setup()
    
    try:        
        while True:
           
           if io.d_in(pir_sensor.__PIR__) == 1:                                
                print("Motion Detected!")
                my_port.write(b'Motion Detected!\n')
                fc_led_bit(1)
                
                
                
           else:
                print("NO Motion")                                                                          
                my_port.write(b'no Motion\n')
                fc_led_bit(2)
                
          
           
           if io.d_in(pir_sensor.__MQ_Sensor__ )== 0:
                print("gas detected...\n")
                my_port.write(b'gas detected\n')    
                fc_led_bit(4)
                    

           else:
                print("not gas\n");
                my_port.write(b'not gas\n')
                
                         
 
           tm.sleep(0.7)
        
    except KeyboardInterrupt:
        print("Ctrl + C KeyboardInterrupt")        
    finally:  
        GPIO.cleanup()
        my_port.close()
        #my_port1.close()
        #my_port.is_close()
        print("GPIO Close")     

#=================================================================

# Program Start main
if __name__ == "__main__":
    main()



                                                                                                                                                                             