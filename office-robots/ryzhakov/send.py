from datetime import datetime  # работа с датой и временем
import smtplib  # отправка писем по электронной почте
from email.message import EmailMessage  # отправка писем по электронной почте

MAIL_LIST = ('shmakovpn@krw.rzd',)  # список рассылки
NOW = f"{datetime.now():%Y-%m-%d %H:%M:%S}"

s = smtplib.SMTP('uc.krw.rzd', 25, 'ivc-ptk-shmak.krw.oao.rzd', )

mail_server = 'uc.krw.rzd'
mail_port = 25

msg = EmailMessage()
msg['Subject'] = f'Роботы идут {NOW}'
msg['From'] = 'shmakovpn@krw.rzd'
msg['To'] = ', '.join(MAIL_LIST)



with smtplib.SMTP(mail_server, mail_port, local_hostname='ivc-ptk-shmak.krw.oao.rzd') as s:
    s.send_message(msg=msg)


