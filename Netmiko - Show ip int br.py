from netmiko import ConnectHandler
import getpass
#Getting Username and password
USER = raw_input("Username: ")
PASSWORD = getpass.getpass()
EN_PASS = getpass.getpass()

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '10.16.212.148',
    'username': USER,
    'password': PASSWORD,
	'secret' : EN_PASS
}


net_connect = ConnectHandler(**iosv_l2)
#net_connect.find_prompt()
output = net_connect.send_command('show ip int brief')
print output