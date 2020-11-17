# import smtplib
# import ssl

# #emailtype must be the type of email you wish to send: currently the three options are "Transaction completed", "Swipe purchased", and "Message waiting"
# #user_receiving must be the user email address of the user who should receive the email
# def sendemail(emailtype,user_receiving):
#     password = "ABCDEFG!!"
#     context = ssl.create_default_context()
#     reviewurl = "blank for now" #need to obtain seller review page url
#     with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as server:
#         server.login("MealSwipers@gmail.com", password)
#         if(emailtype == "Transaction completed"):
#             message = "Your recent transaction through MealSwipers has been completed, please submit a review here: "
#             message.append(reviewurl)
#             server.sendmail("MealSwipers@gmail.com", user_receiving, message)
#         if(emailtype == "Swipe purchased"):
#             message = "Your recent post on MealSwipers has been purchased.  Please log in to MealSwipers to continue the meal swipe transaction."
#             server.sendmail("MealSwipers@gmail.com", user_receiving, message)
#         if(emailtype == "Message waiting"):
#             message = "You have a waiting message on MealSwipers!  Please log in to MealSwipers to continue the meal swipe transaction."
#             server.sendmail("MealSwipers@gmail.com", user_receiving, message)

# if __name__ == '__main__':
#     sendemail('Transaction completed', 'ajd173@case.edu')



import smtplib

sender = 'from@fromdomain.com'
receivers = ['jok10@case.edu','jok10@case.edu']

message = """From: NRV Area Office (Wade Commons) <nrvareaoffice@case.edu>
To: Tevin <tkm28@case.edu>
MIME-Version: 1.0
Content-type: text/html
Subject: [HARLD] You've received a package! (PK1211681)

<p>You have a package waiting at NRV Area Office (Wade Commons)! Bring your CaseOneCard to the office to pick it up.</p>

<p>Here are some details:</p>

<table class="">
    <tbody>
        <tr><th align="right" class="">Type:</th><td class="">I totally made this up</td></tr>
        <tr><th align="right" class="">Delivery Date:</th><td class="">9/29/2019 10:54:00pM</td></tr>
        <tr><th align="right" class="">Carrier:</th><td class="">Looks like a legit package</td></tr>
        <tr><th align="right" class="">Origin:</th><td class="">This is a real ass package</td></tr>
        <tr><th align="right" class="">Bruh:</th><td class="">Do you really have a package?</td></tr>
    </tbody>
</table>

<p class="">
You can always access your waiting packages and mail in your <a href="https://housing.case.edu/myhousing" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://housing.case.edu/myhousing&amp;source=gmail&amp;ust=1593045913431000&amp;usg=AFQjCNGe4d0EdhHfdKq6WuBq6qHr349neA">myHousing</a>.
</p>

<hr style="color:#626262;background-color:#626262" color="#626262">

<table>
    <tbody>
        <tr>
            <td style="font-size:0.85em;font-family:sans-serif">
                <a href="https://case.edu/housing/" style="text-decoration:none;color:#0a304e" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://case.edu/housing/&amp;source=gmail&amp;ust=1593045913431000&amp;usg=AFQjCNGDF1Oki8R1a5sBJL2tRylRlKeFBw">Office of University Housing</a><br><a href="mailto:housing@case.edu" style="text-decoration:none;color:#626262" target="_blank">housing@case.edu</a><br><a href="tel:2163683780" style="text-decoration:none;color:#626262" target="_blank">216.368.3780</a></td><td style="padding-left:40px"><a href="https://www.case.edu/" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.case.edu/&amp;source=gmail&amp;ust=1593045913431000&amp;usg=AFQjCNEyBbjnAnQDHHIRYn5bTqFF9157jQ"><img src="https://ci6.googleusercontent.com/proxy/aFH6eE-byps5MNUj0RS7mF6B7ivV8yxzUiQlgzI_6e3wZ1xfew7qkhwmuAWv6ABxp-0hYpH9SXsoflP-dFPkfMEp2eR-zodoOQ=s0-d-e1-ft#https://my.case.edu/Public/Branding/HarldEmailLogo.png" width="250" height="60" alt="Case Western Reserve University logo" class="CToWUd"></a>
            </td>
        </tr>
    </tbod>
</table>
"""

try:
   smtpObj = smtplib.SMTP('alt1.gmail-smtp-in.l.google.com.')
   smtpObj.sendmail(sender, receivers, message)
   print ("Successfully sent email")
except smtplib.SMTPException:
   print ("Error: unable to send email")