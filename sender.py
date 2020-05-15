from message import sender, my_password, body_of_promotion_message, body_of_confirmation_message, msg_subject
from getmails import from_csv
import yagmail


attach1 = './MONK-AI Webinar IEEE-RITB.pdf'

mails = from_csv()


yag = yagmail.SMTP(user = sender, password = my_password,  host='smtp.gmail.com')
for send_to in mails:
    yag.send(
        to = send_to,
        subject = msg_subject,
        contents = body_of_promotion_message,
        attachments = attach1

    )
    print("sent to : ", send_to)

print("Successful")
