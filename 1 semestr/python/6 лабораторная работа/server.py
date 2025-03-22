import socket
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from fnmatch import fnmatch
from random import randint


def validate_email(email):
    return fnmatch(email, '?*@?*.?*')


def send_email(frm, to, smtp_server, smtp_port, user, password, text):
    
    msg = MIMEMultipart()  # создание объекта сообщения
    subject = f"[Ticket #{randint(0, 10**7)}] Mailer"
    msg['From'] = frm
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(text, "plain"))
    
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls() # установка шифрования TLS
            server.login(user, password)
            server.send_message(msg)
    except Exception as e:
        print(f"Не удалось отправить письмо: {e}")




host = '127.0.0.1'
port = 50007
adm = 'sadjeffff@gmail.com'
pswr = 'tvcsepxpukqvttfn'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen(1)

    connection, addr = s.accept()
    
    print(f'Соединение установлено: {addr}')
    
    data = ''
    recived = connection.recv(1024).decode('utf-8')
    while data:
        data += recived
        recived = connection.recv(1024).decode('utf-8')
    print(data)
    if data:
        inp_email, message = data.split('\n', 1)

        if validate_email(inp_email):
                
                send_email(adm, adm, 'smtp.gmail.com', \
                            587, adm, pswr, message)
                connection.send('OK'.encode('utf-8'))

                if inp_email != adm:
                    send_email(adm, inp_email, 'smtp.gmail.com', \
                            587, adm, pswr, message)
                    connection.send('OK'.encode('utf-8'))

        else:
            connection.send('invalid email'.encode('utf-8'))
                
    else:
        connection.send('invalid input'.encode('utf-8'))
        
    
    print('exitedd')

            
            