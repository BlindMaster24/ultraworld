import paramiko

def run_ssh_command(host, port, username, password, commands):
	try:
		# Create an SSH client
		ssh_client = paramiko.SSHClient()
		ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		
		# Connect to the SSH server
		ssh_client.connect(hostname=host, port=port, username=username, password=password)
		print("Connected to SSH server")

		# Combine commands into one
		command_string = " && ".join(commands)
		stdin, stdout, stderr = ssh_client.exec_command(command_string)

		# Capture output and error
		output = stdout.read().decode()
		error = stderr.read().decode()
		print(f"Output:\n{output}")
		if error:
			print(f"Error:\n{error}")

	except Exception as e:
		print(f"An error occurred: {e}")
		
	finally:
		# Close the SSH connection
		ssh_client.close()
		print("SSH connection closed")

host = "uw.posix.live"
port = 22
username = "uw"
password = "uw server 333 fuck hackers"
commands = [
	"cd /home/uw/svr",
	"mv uwserver svr 2>/dev/null || true",
	"chmod +x svr 2>/dev/null || true",
	"nohup ./svr &"
]

run_ssh_command(host, port, username, password, commands)
