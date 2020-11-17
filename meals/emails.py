import smtplib
import ssl

#emailtype must be the type of email you wish to send: currently the three options are "Transaction completed", "Swipe purchased", and "Message waiting"
#user_receiving must be the user email address of the user who should receive the email
def sendemail(emailtype,user_receiving):
    password = "ABCDEFG!!"
    context = ssl.create_default_context()
    reviewurl = "blank for now" #need to obtain seller review page url
    with smtplib.SMTP_SSL("smtp.case.edu", 25, context = context) as server:
        # server.login("MealSwipers@gmail.com", password)
        if(emailtype == "Transaction completed"):
            message = "Your recent transaction through MealSwipers has been completed, please submit a review here: "
            message.append(reviewurl)
            server.sendmail("MealSwipers@gmail.com", user_receiving, message)
        if(emailtype == "Swipe purchased"):
            message = "Your recent post on MealSwipers has been purchased.  Please log in to MealSwipers to continue the meal swipe transaction."
            server.sendmail("MealSwipers@gmail.com", user_receiving, message)
        if(emailtype == "Message waiting"):
            message = "You have a waiting message on MealSwipers!  Please log in to MealSwipers to continue the meal swipe transaction."
            server.sendmail("MealSwipers@gmail.com", user_receiving, message)

if __name__ == '__main__':
    sendemail('Transaction completed', 'ajd173@case.edu')