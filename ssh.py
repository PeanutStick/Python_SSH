import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('ip', port=22, username='user',password='pass')
ssh.exec_command('ls')
stdin, stdout, stderr = ssh.exec_command("ls -l")
for line in stdout.read().splitlines():
     print (line)

stdin, stdout, stderr = ssh.exec_command ('cd Desktop; pwd; ls -l')
for line in stdout.read().splitlines():
     print (line)

#stdin, stdout, stderr = ssh.exec_command("who")
#for line in stdout.read().splitlines():
#    print (line)

#stdin, stdout, stderr = ssh.exec_command("ls -l")
#for line in stdout.read().splitlines():
#     print (line)
