import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path  # use pathlib instead of os.path

html = Template(Path("index.html").read_text())
email = EmailMessage()
email["from"] = "Kevin Stevens"
email["to"] = "kevin.alan.stevens@gmail.com"
email["subject"] = "Test from Python"

email.set_content(html.substitute({"name": "Kevin"}), "html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()  # encryption mechanism
    smtp.login("**************@gmail.com", "**********")
    smtp.send_mesage(email)
    print("All good!")

