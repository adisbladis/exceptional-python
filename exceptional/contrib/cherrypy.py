from .. import ExceptionalClass, NoExceptionError
from functools import wraps


class ExceptionalCherry(ExceptionalClass):

    def __getattribute__(self, name):
        real = super(ExceptionalCherry, self).__getattribute__(name)
        if hasattr(real, '__call__'):

            @wraps(real)
            def wrapper(*args, **kwargs):
                try:
                    real(*args, **kwargs)
                except NoExceptionError:
                    raise
                except Exception as e:
                    return str(e)

            return wrapper
        return real
