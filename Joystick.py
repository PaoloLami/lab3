import smbus
import PCF8591

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
  while 1:
    x = Joystick.getX("127")
    y = Joystick.getY("127")
    print(str(x)+" , ")
    print(str(y) + "\n")
except KeyboardInterrupt:
  print("Exiting...")