import subprocess
import shlex
from subprocess import Popen
from subprocess import Popen,PIPE
import time
import string
import socket


class IP():    
    def __init__(self, script, ip, port, timer):
        print "Marantz5"
        #self.script = "./MarantzIP/"
        self.script = script
        self.ip = ip
        self.port = port
        self.timer = timer  # threading.Timer(10, self.disconnect)
        
    #
    # Start
    # It might be possible to use the following rather than netcat - for later!
    #
        
    def netcat(hostname, port, content):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((hostname, port))
        s.sendall(content)
        s.shutdown(socket.SHUT_WR)
        while 1:
            data = s.recv(1024)
            if data == "":
                break
            print "Received:", repr(data)
        print "Connection closed."
        s.close()
        
    #
    # End
    #
     
    def write(self, command): 
        self.parms_str = "%s \"%s\" %s %s %s" % (str(self.script), str(command), str(self.ip), str(self.port), str(self.timer))
        #print "Command str is: ", self.parms_str 
        print "Command is: ", command, " self.parms_str is: ", self.parms_str 
        #print "Command is: ", command
        
        #self.parms_lst = [str(self.script), str(command), str(self.ip), str(self.port), str(self.timer)]
        #print "Command lst is: ", self.parms_lst
        #output = subprocess.check_output(self.parms_lst)
        #print "Test: ", output.decode("utf-8")
        
        proc = Popen(self.parms_str, shell=True, stdin=PIPE, stderr=PIPE, stdout=PIPE)
        res = proc.communicate()[0]
        #res, err = proc.communicate()
        #print "STDOUT: ", repr(res), " STDERR: ", repr(err)
        #print "Communicate returns: ", repr(res)
        #string.replace(res, "\n", "\r")
        lst = string.split(res, "\r")               #Result ["Start\nano_string1", "ano_string2, ... , "End\n" ]
        #print "Output list1: ", lst
        lst.remove("")
        #print "Final Output list: ", lst
        print "Returned:   ", lst
        
        time.sleep(self.timer)
        #print "Output strt: ", proc.communicate(), "\nOutput end"
        #return res
        return lst
        
    def write_command(self, command):
        return self.write(command)


       