from pathlib import Path


class MyOpen:
    def __init__(self, file_path, mode):
        self.file_path_ = file_path
        self.mode = mode
        self._file = None

    def __enter__(self):
        print('ABRINDO ARQUIVO')
        self._file = open(self.file_path_, self.mode, encoding='utf8')
        return self._file

    def __exit__(self, class_exception, exception_, traceback_):
        print('FECHANDO ARQUIVO')
        self._file.close()
        return True


file_path = Path('./ex032_context_manager.txt')

with MyOpen(file_path, 'a+') as file:
    file.write('Teste 1\n')
    file.write('Teste 2\n')
    file.write(file.__repr__())
    file.write('\n')
