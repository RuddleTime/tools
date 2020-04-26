import smtplib
import logging

from credentials import credentials


logging.basicConfig(level=logging.INFO)


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


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    # Upgrading to more secure connection
    server.starttls()
    server.ehlo()
    server.login(gmail_user, gmail_password)
    logging.info("Sending email to {0}".format(email_params['to']))
    server.sendmail(
        email_params['sent_from'],
        email_params['to'],  
        email_text
    )
    server.close()


if __name__ == '__main__':
    send_email()

