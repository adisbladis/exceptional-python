from functools import wraps


class NoExceptionError(Exception):
    pass


def exceptional(f):

    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            result = f(*args, **kwargs)
        except Exception:
            raise
        else:
            raise NoExceptionError(result)

    return wrapper


class ExceptionalClass(object):

    def __getattribute__(self, name):
        real = super(ExceptionalClass, self).__getattribute__(name)
        if hasattr(real, '__call__'):
            return exceptional(real)
        return real
