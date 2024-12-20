from flask_mail import Mail, Message

mail = Mail()

def send_notification(user_email, message):
    msg = Message(
        subject="Professional Status Upgrade",
        sender="noreply@example.com",
        recipients=[user_email],
        body=message
    )
    mail.send(msg)
