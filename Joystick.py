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

while 1:
  print(str(self.xlocation)+" , ")
  print(str(self.ylocation))