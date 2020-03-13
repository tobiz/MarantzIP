import Marantz5
#import nclib
import socket
import time



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

print "Test1"
avr.write_command("SI?")

print "Test2"
avr.write_command("SIDVD")
avr.write_command("SI?")

print "Test3"
avr.write_command("SIAUX2")
avr.write_command("SI?")
avr.write_command("SIAUX1")
avr.write_command("SI?")

print "Test4"
avr.write_command("MS?")

print "Test5"
avr.write_command("MNZST?")

print "Test 6"
avr.write_command("PW?")

print "Test 7"
avr.write_command("PWSTANDBY")

print "Test 8"
avr.write_command("MS?")

print "\rTest 9"
avr.write_command("PWON")
avr.write_command("PW?")
avr.write_command("PVMOV")
avr.write_command("PV?")
avr.write_command("PVSTD")
avr.write_command("PV?")
avr.write_command("VSSCH ?")
avr.write_command("PVCN UP")
avr.write_command("PVCN ?")


print "\rTest 10"
avr.write_command("PSSP?")

print "Test 11"
avr.write_command("MNMEN?")

print "Test 12"
avr.write_command("PWSTANDBY")


exit()






#avr.get_status()