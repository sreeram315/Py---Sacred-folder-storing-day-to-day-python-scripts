import smtplib

text = "You are being watched"

m1 = smtplib.SMTP ('smtp.gmail.com',587)

m1.ehlo()

m1.starttls()

m1.login('sreerammaram2@gmail.com','sreeramM31@')

m1.sendmail('amitabhachan@gmail.com','sreerammaram2@gmail.com')

m1.close()