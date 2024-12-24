#OTP verification with email automation
#sending a sample email using python
# Import necessary libraries
import random
import math
import smtplib  # For sending email, need smtplib (Simple Mail Transfer Protocol)

# Define the digits to be used in the OTP
digits = "0123456789"
OTP = ""

# Generate a 6-digit OTP
for i in range(6):
    OTP += digits[math.floor(random.random() * 10)]
otp = OTP + " is your OTP"  # Append a message to the OTP
msg = otp  # Assign the message to be sent

# Set up the SMTP server
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()  # Start TLS for security
s.login("thadkapallysaikiran2001@gmail.com", "orqg qsbe qnrs xmxg")  # Log in to the email account

# Get the recipient email address from user input
user = "thadkapallysaikiran2001@gmail.com"
emailid = input("Enter the email address to send OTP: ")

# Send the email with the OTP
s.sendmail(user, emailid, msg)

# Verify the OTP entered by the user
a = input("Enter your OTP: ")
if a == OTP:
    print("OTP Correct")
else:
    print("Failure: wrong OTP")


'''
Output:
Enter the email address to send OTP: ssagnon3001@gmail.com
Enter your OTP: 868486
OTP Correct
'''










