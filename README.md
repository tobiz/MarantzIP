# MarantzIP
Python module to perform IP control of Marantv AV systems

This is a Python module which enables control of Marantz AV sytems via the IP interface.
The module includes a test script and been tested using a Marantz NR1604.
The repository includes the specification of the Marantz RS232C/IP protocol which includes the command set.  This information was obtained from the Internet as it proved impossible to obtain it from Marantz own website.  If Marantz does not want me to include this information then if the provide a working URL to said information then I will remove the document from this repository and replace it with a link to the Marantz document.

It has taken a considerable time to 'understand' how the Marantz protocol works as there appears to be information missing in its specification.  Most noticeable is the definition of what is returned after a command is sent to a Marantz device.

My conclusion is that in some cases if the device is in the state in which the command being set is trying to set it then an empty response is returned, eg if the device is "powered on" and a PWON command is sent then it returns nothing (represented by \r).  If the device is not in the command state then then it returns the command which it has been sent, eg if the device is in "standby" (represented by PWSTANDBY) and is sent "PWON" then it returns "PWON".  However in many cases not only does it send back the anticipated response but it also sends back other information some of which looks like the RS232C version of the command or system state. Example.  If my NR1604 is in PWSTANDBY and is send PWON the following is returned: 
['PWON', '@PWR:2', 'Z2ON', '@MPW:2', 'ZMON', '@PWR:2']
The @PWR:2 data looking very much like the RS232C format of the system state (after considerable research). It rather looks like Marantz has upgrade its software which originally only supported an RS232C interface to support IP by adding in the IP code and not removing the RS232C code; this is not an issue but it would be helpful if the Marantz documentation explained this as would be expected from a well defined interface specification.

One minor issue is that the general design principle of the interface is that the command structure is a 2 character command code followed by addition parameter characters.  A subset of this syntax is that if the 2 character command code is followed by a question mark character (eg TR?) the command sematics means: return the system state of the system component.  This in general is correct except for the VSSCH command. Under the general rule the 'interogate command would be VSSCH? but it isn't, it's "VSSCH ?", a space between the VSSCH and the ?.  This might be a bug. To be fair the documentation states the syntax is "VSSH ?", but it's potentially a bug by going against the general protocol principle.  If Marantz want to correct me on this I'm more than prepared to remove this statement.

Finally, for now, after much effort using the "correct" Python functions to perform calls to the Marantz device, I've ended up using the "netcat" command (which can also be executed as "nc") and Popen.  I'm not happy about this as it means the interface is not written in "pure" Python, if anyone an correct this to remove "nc and Popen" by pure Python I'd welcome the change.

I'd like to thank Dan Nagle for the PacketSender s/w (https://packetsender.com/) which I used in debugging my code.