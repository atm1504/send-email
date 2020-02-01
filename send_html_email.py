import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas


# Enter your credentials here
send_from = input("Enter the email from which you want to send email: ").rstrip()
password=input("Enter password: ")

def sendemail(to, sub, body):
    msg = MIMEMultipart()
    msg['From'] = to
    msg['To'] = to
    msg['Subject'] = sub
    msg.attach(MIMEText(body, "html"))
    mailserver = smtplib.SMTP('smtp.gmail.com',587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login(send_from, password)
    mailserver.sendmail(to,to,msg.as_string())
    mailserver.quit()

#------------------------------------------------- Write the email in this region-----------------------------#

# List of receivers
to = ["somenath1435@gmail.com", "atm1504.in@gmail.com", "1801me07@iitp.ac.in"]
# Subject of the email
sub = "Test email"
# Body of the email
body2 = """<h3>This is a test email. Please ignore</h3>
<img src='https://anwesha.info/img/pronite/kk.jpg'>
 """

#---------------- Data handling part-----------------
df = pandas.read_csv('testsheet1.csv')
githubs=df.Github
names=df.Name
emails = df.Email

for i in range(1,len(emails)):
    email = str(emails[i])
    name = str(names[i])
    github = str(githubs[i])
    body1="Hi <h4>"+ name+ "</h4> - <h4>"+ github + "</h4> we feel greatful to congratulate you for your performance in NWoC 2019.<br> "
    body = body1 + body2
    # print(body)
    try:
        sendemail(emails[i], sub, body)
        print("Email sent to - ", emails[i])
    except Exception as e:
        print(e, "Failed to send email to - " + emails[i])
print("Task completed")
# for x in to:
#     sendemail(x, sub, body)
