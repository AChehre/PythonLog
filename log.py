from sys import argv
from datetime import datetime
import os.path


class FileLogProvider:

    _log_file_path = ''

    def __init__(self, log_file_path):
        self._log_file_path = log_file_path

    def log(self, message):
        num_lines = FileUtility.line_count(self._log_file_path)
        target = open(self._log_file_path, 'a+')
        target.write('[' + str(num_lines) + '] [' + str(datetime.now()) + '] ' + message + ';\n')
        target.close()


class FileUtility:
    @staticmethod
    def line_count(file_path):
        if os.path.isfile(file_path):
            return sum(1 for line in open(file_path))
        else:
            return 0


log_file_path = r'C:\Users\Administrator\OneDrive\Public\log\log.txt'
logger = FileLogProvider(log_file_path)
argument_message = ' '.join(argv[1:])
logger.log(argument_message)
