from send_email.celery import app
from .servise import send


@app.task
def send_spam_email(user_email):
    send(user_email)