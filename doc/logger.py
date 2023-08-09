import sys


class Exit:
    CL = '\33c'
    RS = '\33[0m'
    RD = '\33[91m'
    GR = '\33[92m'
    YL = '\33[93m'

    @classmethod
    def success(cls, msg):
        sys.exit(f'{cls.CL + cls.GR}SUCCESS: {cls.RS + msg}\n')

    @classmethod
    def warning(cls, msg):
        sys.exit(f'{cls.CL + cls.YL}WARNING: {cls.RS + msg}\n')

    @classmethod
    def error(cls, msg):
        sys.exit(f'{cls.CL + cls.RD}ERROR: {cls.RS + msg}\n')
