# Abstração
class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')

    def log_error(self, msg):
        return self._log(f'Error: {msg}.')

    def log_success(self, msg):
        return self._log(f'Success: {msg}.')


class LogFileMixin(Log):
    def _log(self, msg):
        print(msg)


class LogPrintMixin(Log):
    def _log(self, msg):
        print(msg)


if __name__ == '__main__':
    log1 = LogFileMixin()
    log1._log('Este é meu log.')
