import smbus

class Joystick:
  
  def __init__(self,address):
    self.ADC = PCF8591(bus,address)
    
  def getX(self):
    self.xlocation=ADC.read(1)
    return(self.xlocation)
  
  def getY(self):
    self.ylocation=ADC.read(2)
    return(self.ylocation)

try:
  while 1:
    x = Joystick.getX()
    y = Joystick.getY() 
    print(str(x)+" , ")
    print(str(y) + "\n")
except KeyboardInterrupt:
  print("Exiting...")