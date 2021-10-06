import smbus

class Joystick:

  def __init__(self,address):
    self.ADC = PCF8591(bus,address)
    
  def getX():
    ADC.read(1)
    print(str(ADC.write(1))+" , ")
  
  def getY():
    ADC.read(2)
    print(str(ADC.write(2)))