import paramiko
import time
import datetime
import getpass
import os
#Getting IP and U/N
USER = raw_input("Username: ")
PASSWORD = getpass.getpass()
IP_LIST = open("SWITCH_IP")
NOW = datetime.date.today()
#Get Show-Tech
for line in IP_LIST:
	print "Getting Show-Tech from " + (line)
	HOST = line.strip()
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=HOST,username=USER,password=PASSWORD)
	print "Successful connection", HOST
	remote_connection = ssh_client.invoke_shell()
	remote_connection.send("terminal length 0\n")
	remote_connection.send("show mac address-table\n")
	remote_connection.send("show users\n")
	remote_connection.send("show ip protocols\n")
	remote_connection.send("show tech\n")
	time.sleep(10)
	remote_connection.send("exit\n")
	output = remote_connection.recv(-1)
	saveoutput = open("DEVICE_" + HOST + "_" + str(NOW), "w")
	saveoutput.write(str(output))
	saveoutput.close
	ssh_client.close