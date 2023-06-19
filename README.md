<p align="center">
      <img src="https://images.velog.io/images/sensemint_/post/753eeeb7-1039-4809-9be5-76515b646448/celery.png" width="300" height="100">
</p>

<p align="center">
      <img src="https://img.shields.io/badge/Django-4.1.3-blue">
      <img alt="Static Badge" src="https://img.shields.io/badge/Celery-5.3.1-orange">
      <img src="https://img.shields.io/badge/License-MIT-brightgreen">
</p>

## About the project
This repository contains a Django project for sending emails using the SMTP protocol. The project allows users to subscribe to an email newsletter and sends them spam emails. Redis is used as a message broker and result backend for the Celery task queue.

## Documentation
The project structure consists of two main Django apps: "main" and "send_email." The "main" app handles email subscription forms, views, models, templates, and tasks related to sending spam emails. The "send_email" app contains the project's main settings, URL configurations, and other Django-related files.

The project's settings are defined in the settings.py file, including the secret key, debug mode, database configuration, email settings for SMTP, Celery configuration.

The email subscription form is implemented using Django's class-based views, specifically the CreateView class. The form data is saved to the "Contact" model, and upon form submission, a spam email is sent to the provided email address using the send_spam_email Celery task.

Overall, this Django project provides a basic implementation for email subscription and spam email sending using SMTP and Celery.

## Developers

- [Vitaliy Zhankov] (https://github.com/ZhankovVG)

## P.S. Thank you for reading and visiting my repository, have a nice day!
