#Name:Dylan Muriuki
#Date:26/02/2026
#Program to blink LEDs

from machine import Pin
import time
import machine

red_led = Pin(28, Pin.OUT)
yellow_led = Pin(27, Pin.OUT)
green_button = Pin(22, Pin.IN,Pin.PULL_UP)#Button input
while True:
  button_status = green_button.value()
  if (button_status == 1):
    red_led.off()
    print("Butto released")
  elif (button_status == 0):
    red_led.on()
    print("Button pressed")
  time.sleep(1)
  
