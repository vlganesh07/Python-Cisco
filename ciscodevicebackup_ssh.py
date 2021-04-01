from netmiko import ConnectHandler
import getpass
import sys
import time

##getting system date 
day=time.strftime('%d')
month=time.strftime('%m')
year=time.strftime('%Y')
today=month+"-"+day+"-"+year

##initialising device
device = {
    'device_type': 'cisco_ios',
    'username': 'username',
    'password': 'password',
    'secret':'password'
    }

##opening IP file
ipfile=open("iplist.txt")
print ("Script to take backup of devices, Please enter your credential")
device['username']=input("User name ")
device['password']=getpass.getpass()


##taking backup
for line in ipfile:
 try:
     device['ip']=line.strip("\n")
     print("\n\nConnecting Device ",line)
     net_connect = ConnectHandler(**device)
     net_connect.enable()
     time.sleep(1)
     print ("Reading the running config ")
     output = net_connect.send_command('show run')
     time.sleep(3)
     filename=device['ip']+'-'+today+".txt"
     saveconfig=open(filename,'w+')
     print("Writing Configuration to file")
     saveconfig.write(output)
     saveconfig.close()
     time.sleep(2)
     net_connect.disconnect()
     print ("Configuration saved to file",filename)
 except:
           print ("Access to "+device['ip']+" failed,backup did not taken")

ipfile.close()
print ("\nAll device backup completed")
