import getpass
import telnetlib
import datetime
import time
#Getting Variables required for Switch Access
USER = raw_input("Enter your remote account: ")
PASSWORD = getpass.getpass()
EN_PASS = getpass.getpass()
IP_LIST = open("SWITCH_IP") #Opening File SWITCH_IP
NOW = datetime.datetime.now()
#Loop for using IP mentioned in SWITCH_IP File
for line in IP_LIST:
	print "Getting Running Configuration " + (line)
	HOST = line.strip()
	tn = telnetlib.Telnet(HOST)
#Keying in Username
	tn.read_until("Username: ")
	tn.write(USER + "\n")
#Keying in Password
	if PASSWORD:
		tn.read_until("Password: ")
		tn.write(PASSWORD + "\n")
#Enable Password
		tn.write("\n")
		tn.write("enable\n")

	if EN_PASS:
		tn.read_until("Password: ")
		tn.write(EN_PASS + "\n")
		tn.write("terminal length 0\n")
		tn.write("show run\n")
		tn.write("show tech-support\n")
		time.sleep(10)
		#Saving Switch Config
		tn.write("exit\n")
#Print Outputs
		print tn.read_all()
		readoutput = tn.read_all()
		saveoutput = open("switch " + HOST + " " + str(NOW), "w")
		saveoutput.write(readoutput)
		saveoutput.close
		