import smtplib

from credentials import credentials

gmail_user = "christina.mary.ruddle@gmail.com"
gmail_password = credentials['gmail']


email_params = {
    'sent_from': "python",
    'to': "ruddlec@tcd.ie",
    'subject': 'Rivers and Roads',
    'body': 'Careful and round'
}

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (
    email_params['sent_from'],
    email_params['to'],
    email_params['subject'],
    email_params['body']
)


server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
# Upgrading to more secure connection
server.starttls()
server.ehlo()
server.login(gmail_user, gmail_password)
server.sendmail(
    email_params['sent_from'],
    email_params['to'],  
    email_text
)
server.close()



