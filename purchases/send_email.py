import smtplib


def send_email(email_receiver, subject, text):
    # wdfjlrrmhebayvts


    email = "vlangat439@gmail.com"
    password = "wdfjlrrmhebayvts"
    # subject = "hello there"
    # text = "Good morning"
    # email_receiver = "kimutaiketer033@gmail.com"
    sender_email = email
    receiver_email = email_receiver
    password = password

    subject = subject
    text = text

    message = 'Subject: {}\n\n{}'.format(subject, text)

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message, subject)
    print("Email Sent Successfully!")


send_email()
# import smtplib
# email = "vlangat439@gmail.com"
# password = "golden@254Kim"
# email_receiver = "kimutaiketer033@gmail.com"
#
#
# def sendmail():
#     server = smtplib.SMTP("smtp.gmail.com", 465)
#     server.log(email, password)
#     server.sendmail(email, email_receiver, "Hello how are you?")
#     server.quit()
#
#
# sendmail()