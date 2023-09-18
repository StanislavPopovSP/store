import uuid
from datetime import timedelta

from celery import shared_task
from django.utils.timezone import now  # Можно из джанго взять текущее время

from users.models import EmailVerification, User


# Не будем передавать целый объект пользователя, это слишком накладно и в месседжер брокер это лучше не делать
@shared_task
def settings_email_verification(user_id):
    """Общая настройка перед отправкой письма на электронную почту"""
    # Будем формировать логику, которая отправляет электронное письмо, на адрес электронной почты пользователя, с просьбой подтвердить адрес с его электронной почтой
    user = User.objects.get(id=user_id)
    expiration = now() + timedelta(hours=48)
    code = uuid.uuid4()
    # Будет создаваться каждый раз EmailVerification при регистрации нового пользователя
    record = EmailVerification.objects.create(code=code, user=user, expiration=expiration)
    record.send_verification_email()
