from abc import ABC, abstractmethod


class Notification(ABC):
    def __init__(self, msg) -> None:
        self.msg = msg

    @abstractmethod
    def send(self) -> bool: ...


class EmailNotification(Notification):
    def send(self) -> bool:
        print(f'Enviando e-mail de notificação... {self.msg}')
        return True


class SmsNotification(Notification):
    def send(self) -> bool:
        print(f'Enviando SMS de notificação... {self.msg}')
        return False


def notificate(notification: Notification):
    notification_sent = notification.send()

    if notification_sent:
        print('Notificação enviada com sucesso!')
    else:
        print('Não foi possível enviar a notificação.')


notif_1 = EmailNotification('testando e-mail')
notif_2 = SmsNotification('testando SMS')

notificate(notif_1)
print()
notificate(notif_2)
