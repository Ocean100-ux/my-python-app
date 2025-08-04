import os

def run_command(user_input):
    # Vulnerable to command injection
    os.system("echo " + user_input)

run_command("Hello; rm -rf /")
