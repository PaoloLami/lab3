import smbus
import time

class PCF8591:

  def __init__(self,address):
    self.bus = smbus.SMBus(1)
    self.address = address

  def read(self,chn): #channel
      try:
          self.bus.write_byte(self.address, 0x40 | chn)  # 01000000
          self.bus.read_byte(self.address) # dummy read to start conversion
      except Exception as e:
          print ("Address: %s \n%s" % (self.address,e))
      return self.bus.read_byte(self.address)

  def write(self,val):
      try:
          self.bus.write_byte_data(self.address, 0x40, int(val))
      except Exception as e:
          print ("Error: Device address: 0x%2X \n%s" % (self.address,e))

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