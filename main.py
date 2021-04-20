import smtplib
import textwrap as tw
import os
sender_email = #sender_email
sender_name = #sender_name
recipient_email = #recipient_email
recipient_name = #recipient_name
headers = tw.dedent("""{}
{}
{}
{}""".format ('From:'+ sender_email, 'To:'+ recipient_email, 'Subject: Важно!', 'Content-Type: text/plain; charset="UTF-8";'))
letter_template = """

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%! 
%website% — это новая версия онлайн-курса по программированию. Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 
Как будет проходить ваше обучение на %website%? → Попрактикуешься на реальных кейсах. Задачи от тимлидов со стажем от 10 лет в программировании.→ Будешь учиться без стресса и бессонных ночей. Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.→ Подготовишь крепкое резюме.Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. Регистрируйся → %website%  На модули, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""
letter = letter_template.replace ('%website%','dvmn.org')
letter = letter.replace ('%friend_name%', recipient_name)
letter = letter.replace('%my_name%', sender_name)
message = headers + letter
coded_message = message.encode("UTF-8")
server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
login = os.getenv("LOGIN") #LOGIN from .env
password = os.getenv("PASSWORD") #PASSWORD from .env
server.login(login, password)
server.sendmail(sender_email, recipient_email, coded_message)
server.quit()