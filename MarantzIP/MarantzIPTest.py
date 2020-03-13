import Marantz5
#import nclib
import socket
import time

"""
TCP_IP = '192.168.1.47'
TCP_PORT = 23
BUFFER_SIZE = 1024
MESSAGE = "SIAUX1\\r"
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.close()
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()
 
print "received data:", data

#nc = nclib.Netcat(('192.168.1.47', 23), verbose=True, retry=10)
#nc.settimeout(3)
#nc.send("SIAUX2")
"""

from Marantz import IP
# setup the AVR object using your AVR IP
print "Start"
avr = Marantz5.IP("./nc.sh", "192.168.1.47", 23, 1) 

#avr = Marantz5.IP("nc", "192.168.1.47", 23, 3) 

print "Power On"
#avr.write_command("PWSTANDBY")
avr.write_command("PWON")
#avr.write_command("PW?")

res = avr.write_command("TR?")
#print "Returned: ", res
#avr.write_command("TR1 ON")
avr.write_command("TR1 ON")
avr.write_command("TR?")
avr.write_command("TR1 OFF")
avr.write_command("TR?")
avr.write_command("PVSTD")
avr.write_command("PV?")
avr.write_command("PSFRONT SPA")
avr.write_command("PSFRONT?")
avr.write_command("PSFRONT SPB")
avr.write_command("PSFRONT?")
avr.write_command("PSFRONT A+B")
avr.write_command("PSFRONT?")
avr.write_command("MSDTS SURROUND")
avr.write_command("MS?")
avr.write_command("VSSCH ?")
avr.write_command("VSSCH10P")
avr.write_command("VSSCH ?")
avr.write_command("SDAUTO")
avr.write_command("SD?")
avr.write_command("Z2?")
avr.write_command("PWSTANDBY")



#exit()

print "Again1"
avr.write_command("SI?")

print "Again2"
avr.write_command("SIDVD")
avr.write_command("SI?")

print "Again3"
avr.write_command("SIAUX2")
avr.write_command("SI?")
avr.write_command("SIAUX1")
avr.write_command("SI?")

print "Again4"
avr.write_command("MS?")

print "Again5"
avr.write_command("MNZST?")

print "Again 6"
avr.write_command("PW?")

print "Again 7"
avr.write_command("PWSTANDBY")

print "Again 8"
avr.write_command("MS?")

print "\rAgain 9"
avr.write_command("PWON")
avr.write_command("PW?")
avr.write_command("PVMOV")
avr.write_command("PV?")
avr.write_command("PVSTD")
avr.write_command("PV?")
avr.write_command("VSSCH ?")
avr.write_command("PVCN UP")
avr.write_command("PVCN ?")


print "\rAgain 10"
avr.write_command("PSSP?")

print "Again 11"
avr.write_command("MNMEN?")

print "Again 12"
avr.write_command("PWSTANDBY")


exit()



#avr.write_command("AUX1")
#avr = IP("192.168.1.47") # replace with your AVR IP
# test connectivity
#avr.connect() # if you get an error, double check the IP
# send a command
#avr.get_source()
#avr.set_power("OFF")
#avr.set_power("ON")
#print avr.get_power()
#avr.test()
#exit()
#avr.get_mute()
#print "Set source DVD"
#avr.set_source("DVD")
#print "Result"
#avr.get_source()
#avr.set_source("BD")
#avr.get_source()
#avr.set_source("AUX1")
#avr.set_source("AUX2")
#avr.get_source()
#i = 0
#for j in [1, 2, 3, 4] :
#    print "Test: ", j, " Source is: ", avr.get_source()
#    if i == 0:
#        avr.set_source("AUX1")
#        #print "source was AUX2, now AUX1; ", i
#        i = 1
#    else:
#        avr.set_source("AUX2")
#        #print "source was AUX1, now AUX2: ", i
#        i = 0
#avr.get_source()
#avr.test()
#avr.write_command("SIAUX2")
#avr.write_command("SI?")
#avr.write_command("SI?")



#avr.get_status()