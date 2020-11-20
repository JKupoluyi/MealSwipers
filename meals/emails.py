import smtplib
import ssl

#emailtype must be the type of email you wish to send: currently the three options are "Transaction completed", "Swipe purchased", and "Message waiting"
#user_receiving must be the user email address of the user who should receive the email
def sendemail(emailtype,user_receiving):
    message = ""
    sender = 'from@fromdomain.com'
    receivers = [user_receiving]
    if(emailtype == "Transaction completed"):
        message = "Your recent transaction through MealSwipers has been completed, please submit a review here: "
        try:
            smtpObj = smtplib.SMTP('alt1.gmail-smtp-in.l.google.com.')
            smtpObj.sendmail(sender, receivers, message)
            print ("Successfully sent email")
        except smtplib.SMTPException:
            print ("Error: unable to send email")
    if(emailtype == "Swipe purchased"):
        message = "Your recent post on MealSwipers has been purchased.  Please log in to MealSwipers to continue the meal swipe transaction."
        try:
            smtpObj = smtplib.SMTP('alt1.gmail-smtp-in.l.google.com.')
            smtpObj.sendmail(sender, user_receiving, message)
            print ("Successfully sent email")
        except smtplib.SMTPException:
            print ("Error: unable to send email")
    if(emailtype == "Message waiting"):
        message = "You have a waiting message on MealSwipers!  Please log in to MealSwipers to continue the meal swipe transaction."
        try:
            smtpObj = smtplib.SMTP('alt1.gmail-smtp-in.l.google.com.')
            smtpObj.sendmail(sender, receivers, message)
            print ("Successfully sent email")
        except smtplib.SMTPException:
            print ("Error: unable to send email")

if __name__ == '__main__':
    sendemail('Transaction completed', 'djt69@case.edu')
