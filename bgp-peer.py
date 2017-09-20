#
#Script to login to routers and return BGP neighbours. Return if UP/DOWN and description if down.
#Currently setup for Junos devices only.
#
#Madoc Batters 20/09/2017
#

import re, getpass, netmiko
from netmiko import ConnectHandler

ssh_exceptions = (netmiko.ssh_exception.NetMikoAuthenticationException,
                  netmiko.ssh_exception.NetMikoTimeoutException, netmiko.NetMikoTimeoutException,
                  netmiko.NetMikoAuthenticationException, netmiko.NetmikoTimeoutError, netmiko.NetmikoAuthError,
                  netmiko.ssh_exception.SSHException, netmiko.ssh_exception.AuthenticationException)

un = input('Username: ')
pw = getpass.getpass()
device_type="juniper"


#Insert Device hostnames between treble quotes below, will modify to call hosts from a file:
j_routers = '''

'''.strip().splitlines()

totalpeer=0
alldownpeer2=""
bgpsum = "show bgp summary"

def devicetype():
    madshow = ssh_conn.send_command_expect("show version")
    if "cisco" in madshow.lower():
        return "CISCO"
    elif "junos" in madshow.lower():
        return "JUNIPER"
    else:
        return None

def bgpdesc(peerip):
    command2 = "show configuration | match bgp | match description | display set | match "+peerip
    madshow = ssh_conn.send_command_expect(command2)
    try:
        madshow = madshow.replace('\n','')
        madshow = madshow.replace('{master}','')
        print (madshow.split("description")[1])
    except:
        print ("No Description for this Peer configured on Router sorry!")

print ("All Juniper Routers:")

for j_rtr in j_routers:
    try:
        print ("#"*79)
        print ("Connecting to:",j_rtr)
        ssh_conn = ConnectHandler(ip=j_rtr, device_type=device_type, username=un, password=pw)
        output = ssh_conn.send_command_expect(bgpsum)
        print (devicetype())
        lineoutput = output.splitlines()

        print ("Connected to:",j_rtr)
        print (lineoutput[1])

        print ("Peers UP")
        for line in lineoutput:
            if "Establ" in line:
                totalpeer += 1
                print (line)

#Below could do with less repo            

        print ("Peers DOWN")
        for line in lineoutput:
            if " Acti" in line:
                totalpeer += 1
                print (line)
                peeripdown = line.split("   ")[0]
                alldownpeer2 += peeripdown + (" -*- ")
                bgpdesc(peeripdown)
            elif "Idle" in line:
                totalpeer += 1
                print (line)
                peeripdown = line.split("   ")[0]
                alldownpeer2 += peeripdown + (" -*- ")
                bgpdesc(peeripdown)
            elif "Connect" in line:
                totalpeer += 1
                print (line)
                peeripdown = line.split("   ")[0]
                alldownpeer2 += peeripdown + (" -*- ")
                bgpdesc(peeripdown)
                
        ssh_conn.disconnect()
    except ssh_exceptions:
        print ("Could not connect to device:",j_rtr)

print ("\n")
print ("#"*79)    
print ("Total number of BGP Peerings checked:",totalpeer)
print ("All Peers that are down:")
print (alldownpeer2)

