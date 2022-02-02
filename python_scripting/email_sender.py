import smtplib
from email.message import EmailMessage

email = EmailMessage()
email["from"] = "Kevin Stevens"
email["to"] = "kevin.alan.stevens@gmail.com"
email["subject"] = "Test from Python"

email.set_content("I am a Python developer!")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()  # encryption mechanism
    smtp.login("**************@gmail.com", "**********")
    smtp.send_mesage(email)
    print("All good!")

