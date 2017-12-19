import paramiko 

host = '10.16.212.178'
user = 'admin'
secret = 'force10'
port = 22

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #Set policy to use when connecting to servers without a known host key
ssh.connect(hostname=host, username=user, password=secret, port=port)
stdin, stdout, stderr = ssh.exec_command('sh ver')
output = stdout.readlines()
#print (''.join(output))
file = open('sh_ver.txt', 'w')
file.write(''.join(output))
file.close() 