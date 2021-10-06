import smbus

class Joystick:
  
  def __init__(self,bus,address,xlocation,ylocation):
    self.ADC = PCF8591(bus,address)
    self.xlocation=xlocation
    self.ylocation=ylocation
    
  def getX(self):
    self.xlocation=ADC.write(ADC.read(1))
    return(self.xlocation)
  
  def getY(self):
    self.ylocation=ADC.write(ADC.read(2))
    return(self.ylocation)

try:
  while 1:
    x = Joystick.getX()
    y = Joystick.getY() 
    print(str(x)+" , ")
    print(str(y) + "\n")
except KeyboardInterrupt:
  print("Exiting...")