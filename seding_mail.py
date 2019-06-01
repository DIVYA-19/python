import smtplib
sender = "your_mail@gmail.com"
receiver = "receiver_mail@gmail.com"
password = password_of_your_mail
smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.starttls() #for secure connection
smtpserver.login(sender,password)
msg = 'Subject:Got it :) \njust a demo yar....' #mail content
smtpserver.sendmail(sender,receiver,msg)
print('sent')
smtpserver.close()
