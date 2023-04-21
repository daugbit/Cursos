# Abstração
from pathlib import Path
from time import localtime, strftime

LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')

    def log_error(self, msg):
        return self._log(f'ERROR: {msg}')

    def log_success(self, msg):
        return self._log(f'SUCCESS: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        dt = strftime('%d %b %Y %H:%M:%S', localtime())
        formated_msg = f'{dt} - {msg} ({self.__class__.__name__})'
        print('Salvando no log:', formated_msg)
        with open(LOG_FILE, 'a', encoding='utf-8') as file:
            file.write(f'{formated_msg}\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(msg)


if __name__ == '__main__':
    log1 = LogFileMixin()
    log1.log_error('Este é meu log de erro.')
    log1.log_success('Este é meu log de sucesso.')

