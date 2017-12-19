import getpass
import sys
import telnetlib
#Getting Variables required for Switch Access
user = raw_input("Enter your remote account: ")
password = getpass.getpass()
enable_password = getpass.getpass()
IP_LIST = open("SWITCH_IP")
#Loop for using IP mentioned in SWITCH_IP File
for line in IP_LIST:
	print "Configuring Switch with IP " + (line)
	HOST = line
	tn = telnetlib.Telnet(HOST)
#Keying in Username
	tn.read_until("Username: ")
	tn.write(user + "\n")
#Keying in Password
	if password:
		tn.read_until("Password: ")
		tn.write(password + "\n")
#Enable Password
		tn.write("\n")
		tn.write("enable\n")

	if password:
		tn.read_until("Password: ")
		tn.write(enable_password + "\n")
#Configure Terminal
		tn.write("conf t\n")
#Loop for creating VLAN's
	for n in range(2,21):
		tn.write("vlan " + str(n) + "\n")
		tn.write("name Python_VLAN_" + str(n) +"\n")
#Saving Switch Config
	tn.write("end\n")
	tn.write("wr\n")
	tn.write("exit\n")
#Print Outputs
	print tn.read_all()