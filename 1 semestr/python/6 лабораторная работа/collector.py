import imaplib
import email
from email.header import decode_header
import time
import re

# Конфигурация для почты
EMAIL = "sadjeffff@gmail.com"
PASSWORD = "tvcsepxpukqvttfn"
IMAP_SERVER = "imap.gmail.com" 
CHECK_FREQUENCY = 60  



def check_email():
    mail = imaplib.IMAP4(IMAP_SERVER)
    mail.login(EMAIL, PASSWORD)
    
    mail.select("inbox")  # входящие

    status, messages = mail.search(None, 'UNSEEN')
    message_ids = messages[0].split()

    for msg_id in message_ids:
        # Получаем сообщение
        res, msg = mail.fetch(msg_id, '(RFC822)')
        msg_bytes = msg[0][1]
        msg = email.message_from_bytes(msg_bytes)

        # Получаем тему письма
        subject, encoding = decode_header(msg["Subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding if encoding else 'utf-8')

        # Проверяем формат темы
        if re.match(r'\[Ticket #\d+\] Mailer', subject):
            # Логируем в success_request.log
            with open("success_request.log", "a", encoding='utf-8') as success_log:
                success_log.write(f"ID: {msg_id.decode()}, Content: {msg.get_payload(decode=True).decode('utf-8')}\n")
        else:
            # Логируем в error_request.log
            with open("error_request.log", "a", encoding='utf-8') as error_log:
                error_log.write(f"Content: {msg.get_payload(decode=True).decode('utf-8')}\n")

    # Закрываем соединение
    mail.logout()

# Бесконечный цикл для проверки почты с заданной частотой
while True:
    check_email()
    time.sleep(CHECK_FREQUENCY)