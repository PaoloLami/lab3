import smbus
import PCF8591
import time

class Joystick:
  
  def __init__(self,address):
    self.ADC = PCF8591(address)
    
  def getX(self):
    self.xlocation=self.ADC.read(1)
    return(self.xlocation)

  def getY(self):
    self.ylocation=self.ADC.read(2)
    return(self.ylocation)

try:
  location = Joystick(0x48)
  while 1:
    x = location.getX()
    y = location.getY()
    print(str(x)+" , ")
    print(str(y) + "\n")
    time.sleep(100)
except KeyboardInterrupt:
  print("Exiting...")