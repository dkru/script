# -*- coding: cp866 -*-

# Program for close opened sessions on Terminal Server.
#
# work with Python 2.xx
# Author Denis Krupenov dkru84@gmail.com
#
# run programm logoutter [group name] with paprams, for close session for user
# presented in group. If group name with spaces includin in quotes ""

import subprocess
import re
import sys

#Set default group name Remote desktop users (on Russian language) if input args is null
print str(len(sys.argv))
if len(sys.argv) < 2:
        groupname = '"╧юы№чютрЄхыш єфрыхээюую Ёрсюўхую ёЄюыр"'
else:
        groupname = str(sys.argv[1])
consoleout = subprocess.Popen('net localgroup '+groupname, stdout = subprocess.PIPE)
nameslist = consoleout.stdout.read().split('\r\n')[6:]
for username in nameslist:
        # Skip NT-AUTHORIY, NT_SYSTEM users and empty strings in end of console out, and username not include spaces
	if ('NT' in username) or (' ' in username) or (len(username) == 0): continue
        consoleline = [r'%SYSTEMROOT%\\Sysnative\\query.exe', 'SESSION', username]
        usersessionattribute = subprocess.Popen(consoleline, stdout = subprocess.PIPE, shell = True)
        consoleout = usersessionattribute.stdout.read()
        sessionattributearray = re.split(r'\s{2,}', consoleout)
        # Check for stirngs is present
        if len(sessionattributearray) > 1:
                try:
                        sessionid = int(sessionattributearray[7])
                except:
                        sessionid = int(sessionattributearray[8])
                # Close the session
                if sessionid > 0:
                        #print str(sessionid) #Turn on for debug
                        subprocess.call('%SYSTEMROOT%/Sysnative//logoff.exe '+str(sessionid), shell=True)
