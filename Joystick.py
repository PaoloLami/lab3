import smbus

class Joystick:
  
  def __init__(self,address):
    self.ADC = PCF8591(bus,address)
    
  def getX(self):
    self.xlocation=ADC.write(ADC.read(1))
    return(self.xlocation)
  
  def getY(self):
    self.ylocation=ADC.write(ADC.read(2))
    return(self.ylocation)

try:
  while 1:
    x = Joystick.getX(x)
    y = Joystick.getY(y) 
    print(str(x)+" , ")
    print(str(y) + "\n")
except KeyboardInterrupt:
  print("Exiting...")