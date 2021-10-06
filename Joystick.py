import smbus

class Joystick:
  
  def __init__(self,address,xlocation,ylocation):
    self.ADC = PCF8591(address)
    self.xlocation=xlocation
    self.ylocation=ylocation
    
  def getX(self):
    self.xlocation=self.ADC.read(1)
    return(self.xlocation)

  def getY(self):
    self.ylocation=self.ADC.read(2)
    return(self.ylocation)

try:
  while 1:
    coordinates= Joystick("test","127","127")
    print(str(coordinates.xlocation)+" , ")
    print(str(coordinates.ylocation) + "\n")
except KeyboardInterrupt:
  print("Exiting...")