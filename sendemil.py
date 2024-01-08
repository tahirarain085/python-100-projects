import smtplib as st 

obj = st.SMTP("smtp.gmail.com",534)
obj.ehlo()
obj.starttls()
obj.login("your email","your password")
subject = "test email "
body = "I am learning python from various platforms to excell on this language "
meassage = f"Subject: {subject}\n\n{body}"

listaddress = ["tahirarain085@gmail.com","tahirarainwp@gmail.com"]

sendemail = obj.sendmail("tahirarainwp@gmail.com",listaddress,meassage)
print("sent email successfully! ")
obj.quit()
