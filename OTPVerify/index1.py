#OPT verification................................................................
import os
import math
import random
import smtplib


degits = "0123456789"
otp = ""

for i in range(6):
    otp += degits[math.floor(random.random()*10)]
    msg = "Your OTP verification code is " + otp 
    sending = smtplib.SMTP('smtp.gmail.com', 587)
sending.starttls()
sending.login("mehtapooja38170@gmail.com", "yiqgmbgycbbunitr")
emailId = input("please enter your email:  ")
sending.sendmail('&&&&&&&&&&&', emailId,  msg)
a = input("plaese enter your OTP  >>:  ")
if a == otp:
    print("Yes, Your OTP is Verified")

else:
    print("Please check your OTP again")