# Script for recconet loss connection to VPN, ppoe etc.
# Author Denis Krupenov
# v 1.0
import time, subprocess

def ping(host):
    """
    Returns True if host responds to a ping request
    """
    import platform

    # Ping parameters as function of OS
    ping_str = "-n 4" if  platform.system().lower()=="windows" else "-c 4"
    args = "ping " + " " + ping_str + " " + host

    # Ping
    return subprocess.call(args, shell=False) == 0

while 0 == 0:
    if ping("10.0.10.1") == False:
        subprocess.call('rasphone -h VPN', shell=False)
	itime.sleep(5)
        subprocess.call('rasphone -d VPN', shell=False)
    time.sleep(10)

