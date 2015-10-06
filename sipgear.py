##########################
# sipgear module 0.1     #
# Marek (n1x0n) Kroemeke #
# License: LGPLv3        #
##########################

#########################################
# 1  imei
# 2  telephone
# 3  ? (bool 1/0)
# 4  ? 0000
# 5  ? AUT
# 6  ? 01
# 7  ? 23403002970038 (time?!)
# 8  long/lat,speed in knots, direction
# 9  gps date DDMMYY
# 10 gps time HHMMSS.????
#########################################

class message:
  def __init__(self,message):
    self.message = message
    self.imei = self.message.split('#')[1]
    self.tel = self.message.split('#')[2]
    self.longtitude = self.message.split('#')[8].split(',')[0][:-2] \
                    + self.message.split('#')[8].split(',')[1]
    self.latitude = self.message.split('#')[8].split(',')[2][:-2] \
                  + self.message.split('#')[8].split(',')[3]
    self.speed  = self.message.split('#')[8].split(',')[4]
    self.direction  = self.message.split('#')[8].split(',')[5]
    self.gpsdate    = self.message.split('#')[9]
    self.gpstime    = self.message.split('#')[10]
  def imei(self):
    return self.imei
  def tel(self):
    return  self.tel
  def longtitude(self):
    return self.longtitude
  def latitude(self):
    return self.latitude
  def speed(self):
    return self.speed
  def direction(self):
    return self.direction
  def gps_date(self):
    return self.gpsdate
  def gps_time(self):
    return self.gpstime
