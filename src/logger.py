import sys

CLEAR = '\33c'
RESET = '\33[0m'
RED = '\33[91m'
GREEN = '\33[92m'
YELLOW = '\33[93m'

class Exit:

    @classmethod
    def success(cls, msg):
        print(cls._format_msg(GREEN, 'SUCCESS', msg))
        sys.exit(0)

    @classmethod
    def warning(cls, msg):
        print(cls._format_msg(YELLOW, 'WARNING', msg))
        sys.exit(1)

    @classmethod
    def error(cls, msg, ex):
        print(cls._format_msg(RED, 'ERROR', msg))
        raise ex

    @staticmethod
    def _format_msg(color, tp, msg):
        return f'{CLEAR}{color}{tp}: {RESET}{msg}\n'
