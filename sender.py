from message import sender, my_password, body_of_promotion_message, body_of_confirmation_message, msg_subject

import yagmail


attach1 = './MONK-AI Webinar IEEE-RITB.pdf'


#mails = ['mk6386223@gmail.com', 'sinchu.sr@gmail.com', 'venugopal.dhananjaya@gmail.com', 'ieeeritbexecom@gmail.com']

mails = ['99sinchanabhat@gmail.com', 'ccmm10101010@gmail.com']

yag = yagmail.SMTP(user = sender, password = my_password )
for send_to in mails:
    yag.send(
        to = send_to,
        subject = msg_subject,
        contents = body_of_confirmation_message,
        attachments = attach1

    )


print("Successful")
