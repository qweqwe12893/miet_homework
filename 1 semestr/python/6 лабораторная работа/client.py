import socket
import threading
from time import sleep

# запуск сервера в отдельном потоке
def run_server():
    import subprocess
    subprocess.run(['python', 'server.py'])

server_thread = threading.Thread(target=run_server)
server_thread.start()



host = '127.0.0.1'
port = 50007

while True:
    sleep(1)
    try:
        email = input("Введите email получателя: ")
        message = input("Введите сообщение: ")
        data = f"{email}\n{message}"

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall(data.encode('utf-8'))
            data = s.recv(1024)
        if data.decode('utf-8') == 'OK':
            print("Сообщение успешно отправлено")
            break
        elif data.decode('utf-8') == 'invalid email':
            raise Exception("Вы ввели некорректный email")
        elif data.decode('utf-8') == 'invalid input':
             raise Exception('Введено недостаточное количество данных')
        else:
             raise Exception("Сервер не подтвердил отправку")
        
    except Exception as e:
            print(f"Упс... возникла ошибка. {str(e)}. \nПопробуйте отправить сообщение заново.\n")